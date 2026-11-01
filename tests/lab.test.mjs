import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {challenges,guidedChallenges,challengeForTopic} from '../web/lab-curriculum.mjs';
import {PythonLab,cleanLab,emptyLab,allChecksPassed} from '../web/lab-core.mjs';

test('challenge links resolve to real lessons and every exercise has an exit contract',()=>{
  const roadmap=JSON.parse(fs.readFileSync(new URL('../data/roadmap.json',import.meta.url),'utf8'));
  const ids=new Set(roadmap.topics.map(t=>t.id));
  assert.equal(guidedChallenges.length,13);assert.equal(new Set(challenges.map(c=>c.id)).size,challenges.length);
  for(const c of challenges){for(const topic of c.topics)assert.ok(ids.has(topic),topic);assert.ok(c.hints.length&&c.starter&&c.contract);}
  assert.equal(challengeForTopic('http').id,'api-rate');assert.equal(challengeForTopic('unknown').id,'playground');
});
test('backups preserve drafts and reference use, reject bad input, and never alter roadmap progress',()=>{
  const saved=emptyLab();saved.drafts['first-script']='print("أهلاً")';saved.passed['first-script']={code:'print(42)',at:'2026-11-01',reference:true};saved.revealed=['first-script'];
  assert.deepEqual(cleanLab(JSON.parse(JSON.stringify(saved))),saved);
  assert.throws(()=>cleanLab({...saved,drafts:{unknown:'print(1)'}}));
  assert.throws(()=>cleanLab({...saved,drafts:[]}));
  assert.throws(()=>cleanLab({...saved,drafts:{'first-script':'x'.repeat(30001)}}));
  assert.throws(()=>cleanLab({schema_version:1,roadmap:'python-learning-roadmap',topics:{}}));
  assert.equal(allChecksPassed({error:null,checks:[{passed:true}]},1),true);
  assert.equal(allChecksPassed({error:null,checks:[]},0),false);
  assert.equal(allChecksPassed({error:'failed',checks:[{passed:true}]},1),false);
});
function fakeWorker(){return {terminated:false,postMessage(message){this.message=message;},terminate(){this.terminated=true;},send(data){this.onmessage({data:{requestId:this.message.requestId,...data}});}};}
test('stop terminates a busy worker and a stale result cannot overwrite the next run',()=>{
  const workers=[],results=[];const lab=new PythonLab({workerFactory:()=>{const w=fakeWorker();workers.push(w);return w;},onResult:r=>results.push(r)});
  const payload={code:'print(1)',exerciseId:'playground'};
  assert.equal(lab.run(payload),true);assert.equal(lab.run(payload),false);
  lab.stop();assert.equal(workers[0].terminated,true);
  lab.run(payload);workers[0].send({type:'result',result:'stale'});assert.deepEqual(results,[]);
  workers[1].send({type:'result',result:'fresh'});assert.deepEqual(results,['fresh']);assert.equal(lab.busy,false);lab.stop();
});
test('execution timeout kills a looping worker and permits a new run',async()=>{
  const workers=[],errors=[];const lab=new PythonLab({workerFactory:()=>{const w=fakeWorker();workers.push(w);return w;},onError:e=>errors.push(e),runLimit:15});
  lab.run({code:'while True: pass',exerciseId:'playground'});workers[0].send({type:'phase',phase:'running'});
  await new Promise(resolve=>setTimeout(resolve,40));
  assert.equal(workers[0].terminated,true);assert.equal(lab.busy,false);assert.equal(errors.length,1);
  assert.equal(lab.run({code:'print(42)',exerciseId:'playground'}),true);assert.equal(workers.length,2);lab.stop();
});
