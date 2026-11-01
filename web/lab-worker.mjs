import {challenges} from './lab-curriculum.mjs';

// Pinned official release. Download only when the learner starts a run.
const INDEX_URL='https://cdn.jsdelivr.net/pyodide/v314.0.7/full/';
let runtimePromise;
async function runtime(){
  if(!runtimePromise)runtimePromise=(async()=>{
    const {loadPyodide}=await import(INDEX_URL+'pyodide.mjs');
    const py=await loadPyodide({indexURL:INDEX_URL});
    const response=await fetch(new URL('./lab-runner.py',import.meta.url));
    if(!response.ok)throw new Error('The learning runner could not load.');
    py.runPython(await response.text());
    return py;
  })();
  return runtimePromise;
}
self.onmessage=async({data})=>{
  const {requestId,exerciseId,code,stdin,csv,mode}=data;
  try{
    const exercise=challenges.find(c=>c.id===exerciseId);
    if(!exercise)throw new Error('Unknown exercise.');
    self.postMessage({requestId,type:'phase',phase:'loading'});
    const py=await runtime();
    if(exercise.packages?.length){
      self.postMessage({requestId,type:'phase',phase:'packages'});
      await py.loadPackage(exercise.packages);
    }
    self.postMessage({requestId,type:'phase',phase:'running'});
    const execute=py.globals.get('execute_lab');
    let result;
    try{result=JSON.parse(execute(JSON.stringify({code,stdin,csv,mode,checks:exercise.checks})));}
    finally{execute.destroy();}
    self.postMessage({requestId,type:'result',result});
  }catch(error){self.postMessage({requestId,type:'fatal',message:error.message||String(error)});}
};
