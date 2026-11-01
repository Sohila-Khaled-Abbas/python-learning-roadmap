import {challenges} from './lab-curriculum.mjs';
export const LAB_KEY='sohila-python-lab-v1';
export const MAX_CODE=30000;
export function emptyLab(){return {schema_version:1,drafts:{},passed:{},revealed:[]};}
export function cleanLab(raw){
  if(!raw||raw.schema_version!==1||!raw.drafts||typeof raw.drafts!=='object'||Array.isArray(raw.drafts)||!raw.passed||typeof raw.passed!=='object'||Array.isArray(raw.passed)||!Array.isArray(raw.revealed))throw new Error('This is not a coding-lab backup.');
  const result=emptyLab(),ids=new Set(challenges.map(c=>c.id));
  for(const [id,code] of Object.entries(raw.drafts)){
    if(!ids.has(id)||typeof code!=='string'||code.length>MAX_CODE)throw new Error('Invalid exercise draft.');
    result.drafts[id]=code;
  }
  for(const [id,p] of Object.entries(raw.passed)){
    if(!ids.has(id)||!p||typeof p.code!=='string'||p.code.length>MAX_CODE||typeof p.at!=='string'||typeof p.reference!=='boolean')throw new Error('Invalid exercise history.');
    result.passed[id]={code:p.code,at:p.at,reference:p.reference};
  }
  if(raw.revealed.some(id=>!ids.has(id)))throw new Error('Unknown reference solution.');
  result.revealed=[...new Set(raw.revealed)];return result;
}
export function allChecksPassed(result,expected){return !result.error&&expected>0&&result.checks.length===expected&&result.checks.every(c=>c.passed===true);}
export class PythonLab {
  constructor({workerFactory=()=>new Worker(new URL('./lab-worker.mjs',import.meta.url),{type:'module'}),onState=()=>{},onResult=()=>{},onError=()=>{},loadLimit=120000,runLimit=12000}={}){Object.assign(this,{workerFactory,onState,onResult,onError,loadLimit,runLimit});this.worker=null;this.busy=false;this.requestId=0;}
  arm(limit,message){clearTimeout(this.timer);this.timer=setTimeout(()=>{this.stop();this.onError(message);},limit);}
  run(payload){
    if(this.busy)return false;
    if(typeof payload.code!=='string'||payload.code.length>MAX_CODE)throw new Error('Keep code under 30,000 characters.');
    this.busy=true;this.onState('loading');
    const id=++this.requestId;
    try{
      if(!this.worker){
        const worker=this.worker=this.workerFactory();
        worker.onmessage=({data})=>{
          if(worker!==this.worker||data.requestId!==this.requestId||!this.busy)return;
          if(data.type==='phase'){
            this.onState(data.phase);
            if(data.phase==='running')this.arm(this.runLimit,'The 12-second run limit was reached. Your code is saved. Check for an unbounded loop, then run again.');
            else this.arm(this.loadLimit,'The Python download took too long. Check your connection and retry. Your code is saved.');
          }else if(data.type==='result'){
            clearTimeout(this.timer);this.busy=false;this.onState('ready');this.onResult(data.result);
          }else if(data.type==='fatal'){
            this.stop();this.onError('Python could not run: '+data.message+' Retry Run; the first run needs access to the Pyodide CDN.');
          }
        };
        worker.onerror=()=>{if(worker!==this.worker)return;this.stop();this.onError('The Python worker could not load. Check your connection and retry Run.');};
      }
      this.arm(this.loadLimit,'The Python download took too long. Retry Run when connected.');
      this.worker.postMessage({...payload,requestId:id});
      return true;
    }catch(error){this.stop();this.onError(error.message);return false;}
  }
  stop(){clearTimeout(this.timer);this.worker?.terminate();this.worker=null;this.busy=false;this.requestId++;this.onState('idle');}
}
