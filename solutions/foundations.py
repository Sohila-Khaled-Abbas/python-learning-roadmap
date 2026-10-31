"""Original reference solutions; attempt exercises/foundations.py first."""
from decimal import Decimal, InvalidOperation
import re


def pipeline_message(stage, rows):
    return f'{stage}: {rows} rows'


def to_piastres(text):
    """Accept a finite decimal EGP string with at most two fractional places."""
    if not isinstance(text, str) or not re.fullmatch(r'[+-]?\d+(?:\.\d{1,2})?', text.strip()):
        raise ValueError('amount must be a decimal string with at most two places')
    try:
        amount = Decimal(text.strip())
        if not amount.is_finite():
            raise ValueError('amount must be finite')
        return int(amount * 100)
    except InvalidOperation as exc:
        raise ValueError('invalid EGP amount') from exc


def net_revenue(gross, discount):
    if gross < 0 or not 0 <= discount <= gross:
        raise ValueError('invalid gross/discount')
    return gross - discount


def classify_copy(record, category):
    result = dict(record)
    result['category'] = category
    return result


def mean_or_none(values):
    return sum(values) / len(values) if values else None


def page_count(rows, size):
    if rows < 0 or size <= 0:
        raise ValueError('invalid pagination inputs')
    return (rows + size - 1) // size


def amount_status(value):
    if value is None:
        return 'missing'
    if value < 0:
        return 'invalid'
    return 'zero' if value == 0 else 'valid'


def valid_total(values):
    return sum(v for v in values if v is not None and v >= 0)


def latest(items, n):
    if n < 0:
        raise ValueError('n must be nonnegative')
    return list(items[-n:]) if n else []


def totals_by_category(records):
    result = {}
    for row in records:
        category = row['category']
        result[category] = result.get(category, 0) + row['amount']
    return result


def missing_ids(observed, reference):
    return sorted(set(observed) - set(reference))


def parse_count(value):
    if isinstance(value, bool) or not re.fullmatch(r'\d+', str(value).strip()):
        raise ValueError('count must be a nonnegative integer')
    return int(str(value).strip())
