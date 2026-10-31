"""Offline reference ETL. Fixture commerce data is synthetic; this is not a live API client."""
import argparse
import csv
from datetime import date
import json
import logging
from pathlib import Path
import re
import sqlite3

from solutions.foundations import to_piastres, parse_count

REQUIRED = ('order_id', 'order_date', 'category', 'quantity', 'unit_price_egp')
MAX_SQLITE_INT = 2**63 - 1


def parse_row(row):
    order_id = (row.get('order_id') or '').strip()
    category = (row.get('category') or '').strip()
    if not order_id or not category:
        raise ValueError('missing order_id or category')
    day = (row.get('order_date') or '').strip()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', day):
        raise ValueError('order_date must use YYYY-MM-DD')
    date.fromisoformat(day)
    quantity = parse_count(row.get('quantity', ''))
    price = to_piastres(row.get('unit_price_egp', ''))
    if quantity <= 0 or price < 0:
        raise ValueError('quantity must be positive; unit price must be nonnegative')
    total = quantity * price
    if max(quantity, price, total) > MAX_SQLITE_INT:
        raise ValueError('amount or quantity exceeds SQLite integer capacity')
    return (order_id, day, category, quantity, price, total)


def run(source, database, output):
    source, database, output = Path(source), Path(database), Path(output)
    if source.resolve() == database.resolve():
        raise ValueError('database must not overwrite source')
    reserved = [output / name for name in ('rejects.csv', 'orders.csv', 'summary.json')]
    if any(source.resolve() == p.resolve() or database.resolve() == p.resolve() for p in reserved):
        raise ValueError('input/database collides with a generated output')
    with source.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(REQUIRED):
            raise ValueError('header must exactly match: '+','.join(REQUIRED))
        rows = list(reader)
    # Header is checked before creating the output database.
    database.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    rejects, accepted, inserted, duplicates = [], 0, 0, 0
    with sqlite3.connect(database) as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, order_date TEXT NOT NULL, category TEXT NOT NULL, quantity INTEGER NOT NULL, unit_price_piastres INTEGER NOT NULL, total_piastres INTEGER NOT NULL)')
        for line, row in enumerate(rows, 2):
            try:
                if None in row:
                    raise ValueError('row has more fields than the declared header')
                record = parse_row(row)
                existing = connection.execute('SELECT * FROM orders WHERE order_id = ?', (record[0],)).fetchone()
                if existing is not None:
                    if tuple(existing) != record:
                        raise ValueError('conflicting duplicate order_id; existing row preserved')
                    duplicates += 1
                else:
                    connection.execute('INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)', record)
                    inserted += 1
                accepted += 1
            except ValueError as exc:
                rejects.append(dict(line=line, reason=str(exc), raw_json=json.dumps(row, ensure_ascii=False)))
        loaded = connection.execute('SELECT * FROM orders ORDER BY order_id').fetchall()
    with (output/'rejects.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['line', 'reason', 'raw_json'])
        writer.writeheader(); writer.writerows(rejects)
    with (output/'orders.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['order_id', 'order_date', 'category', 'quantity', 'unit_price_piastres', 'total_piastres'])
        writer.writerows(loaded)
    summary = dict(source_kind='synthetic offline fixture', input_rows=len(rows), accepted=accepted, rejected=len(rejects), inserted=inserted, identical_duplicates=duplicates, stored_rows=len(loaded), stored_total_piastres=sum(row[5] for row in loaded))
    (output/'summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    logging.info('accepted=%s rejected=%s inserted=%s', accepted, len(rejects), inserted)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='data/fixtures/orders.csv')
    parser.add_argument('--database', default='output/orders.sqlite')
    parser.add_argument('--output', default='output')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
    try:
        summary = run(args.input, args.database, args.output)
    except (ValueError, OSError, sqlite3.Error) as exc:
        parser.exit(2, f'Pipeline failed: {exc}\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
