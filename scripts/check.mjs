import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
const root=path.resolve(new URL('..',import.meta.url).pathname);
const d=JSON.parse(await fs.readFile(path.join(root,'data/roadmap.json'),'utf8'));
const ids=new Set(d.topics.map(t=>t.id)),phases=new Set(d.phases.map(p=>p.id)),resources=new Set(d.resources.map(r=>r.id));
assert.equal(ids.size,d.topics.length,'topic IDs must be unique');
assert.equal(resources.size,d.resources.length,'resource IDs must be unique');
assert.equal(d.topics.length,30);assert.equal(d.weeks.length,12);
assert.equal(d.topics.reduce((sum,t)=>sum+t.hours,0),84);
const visited=new Set(),visiting=new Set();
function visit(id){assert(!visiting.has(id),'prerequisite cycle');if(visited.has(id))return;visiting.add(id);const t=d.topics.find(x=>x.id===id);t.requires.forEach(visit);visiting.delete(id);visited.add(id);}
for(const t of d.topics){assert(phases.has(t.phase));assert(t.learn.length&&t.exercise&&t.gate);for(const id of t.requires)assert(ids.has(id));for(const id of t.resources)assert(resources.has(id));await fs.access(path.join(root,t.note_path));visit(t.id);}
for(const w of d.weeks)for(const id of w.topics)assert(ids.has(id));
const chapterTopics=d.topics.filter(t=>t.chapter);assert.equal(chapterTopics.length,12);let last=0;
for(const [index,t] of chapterTopics.entries()){assert.equal(t.chapter.number,index+1);assert(t.chapter.start>last);last=t.chapter.start;}
for(const r of d.resources){const url=new URL(r.url);assert.equal(url.protocol,'https:');assert(r.origin&&r.verification);}
const html=await fs.readFile(path.join(root,'dist/index.html'),'utf8');
for(const match of html.matchAll(/(?:src|href)="([^"#]+)"/g)){const u=match[1];if(/^(https:|data:)/.test(u))continue;assert(!u.startsWith('/'),'asset paths must work under GitHub project subpaths');await fs.access(path.join(root,'dist',u));}
for(const name of ['app.mjs','core.mjs','styles.css','social-card.png','sitemap.xml','robots.txt','data/roadmap.json'])await fs.access(path.join(root,'dist',name));
// Verify internal Markdown links (including generated notes) without requiring the network.
async function scan(dir){for(const entry of await fs.readdir(dir,{withFileTypes:true})){if(['.git','dist','.openai','output','__pycache__'].includes(entry.name))continue;const file=path.join(dir,entry.name);if(entry.isDirectory()){await scan(file);continue;}if(!file.endsWith('.md'))continue;const text=await fs.readFile(file,'utf8');for(const match of text.matchAll(/\]\(([^)\s]+)\)/g)){const u=match[1];if(/^(https?:|#|mailto:)/.test(u))continue;await fs.access(path.resolve(path.dirname(file),u.split('#')[0]));}}}
await scan(root);
console.log(`Validated ${d.topics.length} topics, ${d.resources.length} sources, chapter timestamps, prerequisite graph, local links and Pages assets.`);
