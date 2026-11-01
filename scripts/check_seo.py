"""Validate the generated site as crawlable HTML, independent of JavaScript."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
ORIGIN='https://sohila-khaled-abbas.github.io/python-learning-roadmap/'

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.canonicals=[];self.descriptions=[];self.h1=0;self.links=[];self.structured=[];self.in_json=False;self.buffer='';self.in_title=False;self.title=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='title':self.in_title=True
        if tag=='link' and a.get('rel')=='canonical':self.canonicals.append(a.get('href'))
        if tag=='meta' and a.get('name')=='description':self.descriptions.append(a.get('content'))
        if tag in ('a','link','script','img'):
            value=a.get('href') or a.get('src')
            if value:self.links.append(value)
        if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.buffer=''
    def handle_data(self,data):
        if self.in_json:self.buffer+=data
        if self.in_title:self.title+=data
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script' and self.in_json:self.structured.append(json.loads(self.buffer));self.in_json=False

def check():
    pages=list(OUT.rglob('index.html'));titles=set();canonicals=set()
    for file in pages:
        parser=Page();parser.feed(file.read_text())
        assert parser.h1==1,(file,'one H1 required')
        assert len(parser.canonicals)==1 and parser.canonicals[0].startswith(ORIGIN),(file,'canonical')
        assert parser.canonicals[0] not in canonicals,(file,'duplicate canonical')
        assert parser.title not in titles,(file,'duplicate title')
        assert len(parser.descriptions)==1 and len(parser.descriptions[0])>=50,(file,'description')
        assert parser.structured,(file,'JSON-LD')
        titles.add(parser.title);canonicals.update(parser.canonicals)
        for ref in parser.links:
            parsed=urlparse(ref)
            if parsed.scheme or ref.startswith('#'):continue
            target=(file.parent/unquote(parsed.path)).resolve()
            assert target.is_relative_to(OUT.resolve()),(file,'link escapes site',ref)
            assert target.exists(),(file,'missing internal asset/page',ref)
        if '/lessons/' in file.as_posix() and file.parent.name!='lessons':
            content=file.read_text();assert 'Understand the idea' in content and 'EXIT CHECK' in content
            assert '../../lab/?topic=' + file.parent.name in content, (file, 'lesson must link to contextual practice')
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls={node.text for node in ET.parse(OUT/'sitemap.xml').findall('s:url/s:loc',ns)}
    assert urls==canonicals,('sitemap must match generated canonical pages',urls^canonicals)
    assert len(pages)==47,len(pages)
    assert '<iframe' not in (OUT/'resources/index.html').read_text(),'resource players should load on request'
    print(f'Validated {len(pages)} unique HTML pages, JSON-LD, local links, crawlable lesson content and sitemap coverage.')

if __name__=='__main__':check()
