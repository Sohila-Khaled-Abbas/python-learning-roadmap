import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {youtubeMedia,mediaPreview} from '../web/media.mjs';
import {cleanProgress} from '../web/core.mjs';
test('video URL normalization strips tracking and creates a privacy-enhanced player',()=>{
  const m=youtubeMedia('https://youtu.be/XKQaCF_Om8o?si=tracking&utm_source=chatgpt.com');
  assert.equal(m.url,'https://www.youtube.com/watch?v=XKQaCF_Om8o');
  assert.equal(m.kind,'video');assert(m.embed.startsWith('https://www.youtube-nocookie.com/embed/XKQaCF_Om8o?'));
  assert(!m.embed.includes('autoplay'));assert(!m.embed.includes('tracking'));
});
test('playlist URLs retain playlist identity instead of being treated as videos',()=>{
  const m=youtubeMedia('https://www.youtube.com/playlist?list=PLQ1FVkQVumFJpSpiVrgCF0UQxTGrmVnRk&si=tracking');
  assert.equal(m.kind,'playlist');assert(m.embed.includes('embed/videoseries?list=PLQ1FVkQVumFJpSpiVrgCF0UQxTGrmVnRk'));
});
test('untrusted hosts, credentials and invalid IDs never create iframe sources',()=>{
  for(const value of ['javascript:alert(1)','https://youtube.com.evil.example/watch?v=XKQaCF_Om8o','https://user:pass@youtube.com/watch?v=XKQaCF_Om8o','https://www.youtube.com/watch?v=bad'])assert.equal(youtubeMedia(value),null);
});
test('preview contains no iframe before a deliberate load action and escapes metadata',()=>{
  const html=mediaPreview({title:'<script>alert(1)</script>',url:'https://youtu.be/XKQaCF_Om8o'});
  assert(!html.includes('<iframe'));assert(!html.includes('<script>'));assert(html.includes('data-load-media'));assert(html.includes('Open on YouTube'));
});
test('all eleven supplied resources are represented once and old progress IDs survive enrichment',()=>{
  const d=JSON.parse(fs.readFileSync(new URL('../data/roadmap.json',import.meta.url)));
  const ids=['XKQaCF_Om8o','Rq5gJVxz55Q','PLWd4nYaF_Vx7Db9uFWf_Df-UrP8ArF4L_','6aoIQ4bz49w','PLiEts138s9P0w-WX4Rmml-_zhnBkXLWtc','PL6-3IRz2XF5UM-FWfQeF1_YhMMa12Eg3s','A9kSngn7254','KxvKCSwlUv8','iXYeb2artTE','PLQ1FVkQVumFIEH7dYP_2L6vi_LyjlVsGm','PLQ1FVkQVumFJpSpiVrgCF0UQxTGrmVnRk'];
  for(const id of ids)assert.equal(d.resources.filter(r=>youtubeMedia(r.url)?.id===id).length,1,id);
  const old={schema_version:1,roadmap:'python-learning-roadmap',topics:{functions:{status:'done',notes:'existing evidence'},quality:{status:'learning',notes:'keep'}}};
  assert.deepEqual(cleanProgress(old,d.topics.map(t=>t.id)),old);
});
