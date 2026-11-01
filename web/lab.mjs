import {challenges,guidedChallenges,challengeForTopic,ORDERS_CSV} from './lab-curriculum.mjs';
import {LAB_KEY,MAX_CODE,emptyLab,cleanLab,allChecksPassed,PythonLab} from './lab-core.mjs';
const $=id=>document.getElementById(id);
let saved=emptyLab(),current=challenges[0],hints=0,started=0,submitted=null,tabIndent=true;
let curriculum;
function notice(message){$('lab-notice').hidden=false;$('lab-notice').textContent=message;}
try{const raw=localStorage.getItem(LAB_KEY);if(raw)saved=cleanLab(JSON.parse(raw));}catch{notice('The lab backup could not be read. Drafts are available for this session; export a backup before leaving.');}
function save(){try{localStorage.setItem(LAB_KEY,JSON.stringify(saved));}catch{notice('Browser storage is unavailable or full. Export a lab backup to keep your code.');}}
function saveDraft(){saved.drafts[current.id]=$('python-code').value;save();draftState();}
function draftState(){const past=saved.passed[current.id];$('draft-state').textContent=past?(past.code===$('python-code').value?`This version passed the practice checks${past.reference?' · reference used':''}.`:'Draft changed since the last successful check. Run the checks again.'):'Draft autosaves in this browser.';}
function lines(){$('line-numbers').textContent=Array.from({length:$('python-code').value.split('\n').length},(_,i)=>i+1).join('\n');}
function button(label,handler){const b=document.createElement('button');b.type='button';b.textContent=label;b.onclick=handler;return b;}
function renderPath(){
  const count=guidedChallenges.filter(c=>saved.passed[c.id]).length;
  $('lab-progress-label').textContent=`${count} / ${guidedChallenges.length} checked`;$('lab-progress').max=guidedChallenges.length;$('lab-progress').value=count;
  $('challenge-list').replaceChildren(...challenges.map(c=>{const b=button('',()=>select(c));b.setAttribute('aria-current',String(current.id===c.id));const title=document.createElement('span');title.textContent=c.title;const mark=document.createElement('span');mark.textContent=saved.passed[c.id]?'✓':'↗';b.append(title,mark);return b;}));
  $('challenge-picker').replaceChildren(...challenges.map(c=>{const option=document.createElement('option');option.value=c.id;option.textContent=(saved.passed[c.id]?'✓ ':'')+c.title;return option;}));$('challenge-picker').value=current.id;
}
function lessonLinks(){
  const topics=curriculum?.topics.filter(t=>current.topics.includes(t.id))||[];
  $('challenge-lessons').replaceChildren(...topics.slice(0,3).map(t=>{const a=document.createElement('a');a.href=`../lessons/${t.id}/`;a.textContent=t.title+' ↗';return a;}));
}
function feedback(text,kind=''){$('run-feedback').textContent=text;$('run-feedback').dataset.kind=kind;}
function select(c,{persist=true}={}){
  if(lab.busy)lab.stop();
  if(persist)saveDraft();current=c;hints=0;
  $('challenge-title').textContent=c.title;$('challenge-level').textContent=c.level;$('challenge-time').textContent=c.minutes?`${c.minutes} minute practice`: 'Your own experiment';$('challenge-brief').textContent=c.brief;$('challenge-contract').textContent=c.contract;
  $('python-code').value=saved.drafts[c.id]??c.starter;lines();draftState();$('hint-list').replaceChildren();$('next-hint').disabled=false;$('next-hint').textContent='Reveal a hint +';$('stretch-task').textContent='Try next: '+c.stretch;
  $('reference-details').open=false;$('reference-details').hidden=!c.solution;$('reference-code').textContent='';$('check-python').hidden=!c.checks.length;$('check-results').replaceChildren();$('next-challenge').hidden=true;$('python-output').textContent='Run your code to see the result.';$('run-duration').textContent='';feedback('');lessonLinks();renderPath();
  const url=new URL(location.href);url.searchParams.set('exercise',c.id);history.replaceState(null,'',url);
}
const lab=new PythonLab({
  onState(state){const busy=lab.busy;for(const id of ['run-python','check-python','reset-code','use-reference','challenge-picker'])$(id).disabled=busy;$('stop-python').disabled=!busy;$('python-code').readOnly=busy;
    $('runtime-state').textContent=({idle:'Stopped · ready for a fresh run',loading:'Preparing Python · first download can take a little while…',packages:'Loading the optional pandas package…',running:'Running Python · 12 second limit',ready:'Python ready · variables reset each run'})[state];
  },
  onResult(result){
    $('run-duration').textContent=`${((performance.now()-started)/1000).toFixed(1)}s`;
    $('python-output').textContent=(result.stdout||'No printed output.')+(result.stderr?'\n\nStandard error:\n'+result.stderr:'')+(result.truncated?'\n[Output limited to 16,000 characters per stream.]':'');
    if(result.error){feedback(result.error,'error');return;}
    const expected=submitted.exercise.checks.length;
    if(submitted.mode==='check'&&expected){
      const pass=allChecksPassed(result,expected);
      $('check-results').replaceChildren(...result.checks.map(check=>{const li=document.createElement('li');li.dataset.passed=String(check.passed);const title=document.createElement('strong');title.textContent=(check.passed?'✓ ':'↳ ')+check.name;const detail=document.createElement('span');detail.textContent=check.detail;li.append(title,detail);return li;}));
      feedback(pass?`All ${expected} checks passed. Now try the variation below and explain why your code works.`:`${result.checks.filter(c=>c.passed).length} of ${expected} checks passed. Use the feedback or reveal one hint, then try again.`,pass?'passed':'error');
      if(pass){saved.passed[current.id]={at:new Date().toISOString(),code:submitted.code,reference:saved.revealed.includes(current.id)};save();renderPath();draftState();$('next-challenge').hidden=guidedChallenges.indexOf(current)===guidedChallenges.length-1;}
    }else feedback('Run finished. '+(expected?'Use “Check my work” to try the exercise cases.':'Try a variation and rerun.'));
  },
  onError(message){feedback(message,'error');}
});
function run(mode){
  if(lab.busy)return;
  saveDraft();$('check-results').replaceChildren();$('next-challenge').hidden=true;feedback('');$('python-output').textContent='Preparing your run…';$('run-duration').textContent='';started=performance.now();
  submitted={exercise:current,mode,code:$('python-code').value};
  lab.run({exerciseId:current.id,code:submitted.code,mode,stdin:$('python-stdin').value,csv:$('csv-fixture').value});
}
$('run-python').onclick=()=>run('run');$('check-python').onclick=()=>run('check');$('stop-python').onclick=()=>{lab.stop();feedback('Stopped. Your code is saved; the next run starts a fresh Python worker.');};
$('python-code').oninput=()=>{saveDraft();lines();};$('python-code').onscroll=()=>{$('line-numbers').scrollTop=$('python-code').scrollTop;};
$('python-code').onkeydown=event=>{
  if(event.key==='Enter'&&(event.ctrlKey||event.metaKey)){event.preventDefault();run(event.shiftKey?'check':'run');}
  if(event.key==='Escape'){tabIndent=false;return;}
  if(event.key==='Tab'){
    if(!tabIndent||event.shiftKey){tabIndent=true;return;}
    event.preventDefault();const editor=$('python-code'),start=editor.selectionStart,end=editor.selectionEnd;
    if(editor.value.length+4<=MAX_CODE&&!editor.readOnly){editor.setRangeText('    ',start,end,'end');saveDraft();lines();}
  }
};
$('challenge-picker').onchange=()=>select(challenges.find(c=>c.id===$('challenge-picker').value));
$('next-hint').onclick=()=>{const hint=document.createElement('li');hint.textContent=current.hints[hints++];$('hint-list').append(hint);$('next-hint').disabled=hints>=current.hints.length;$('next-hint').textContent=hints>=current.hints.length?'All hints revealed':'One more hint +';};
$('reference-details').ontoggle=()=>{if(!$('reference-details').open)return;if(!saved.revealed.includes(current.id)){saved.revealed.push(current.id);save();}$('reference-code').textContent=current.solution;};
$('use-reference').onclick=()=>{if(!confirm('Replace this draft with the reference solution? Export or download your draft first to keep it.'))return;$('python-code').value=current.solution;if(!saved.revealed.includes(current.id))saved.revealed.push(current.id);saveDraft();lines();};
$('reset-code').onclick=()=>{if(!confirm('Restore this challenge’s starter? Download or export your draft first to keep it.'))return;$('python-code').value=current.starter;saveDraft();lines();feedback('Starter restored. Your earlier practice history is retained.');};
$('next-challenge').onclick=()=>{const i=guidedChallenges.indexOf(current);if(i>=0&&guidedChallenges[i+1])select(guidedChallenges[i+1]);};
$('csv-fixture').value=ORDERS_CSV;$('restore-dataset').onclick=()=>{if($('csv-fixture').value!==ORDERS_CSV&&!confirm('Restore the original synthetic dataset? Copy any custom CSV first to keep it.'))return;$('csv-fixture').value=ORDERS_CSV;};
function download(content,type,name){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
$('download-code').onclick=()=>download($('python-code').value,'text/x-python',current.id+'.py');
$('export-lab').onclick=()=>{saveDraft();download(JSON.stringify(saved,null,2),'application/json','python-lab-backup.json');};
$('import-lab').onchange=async()=>{const file=$('import-lab').files[0];if(!file)return;try{if(file.size>1500000)throw new Error('Backup must be smaller than 1.5 MB.');const imported=cleanLab(JSON.parse(await file.text()));if(!confirm('Replace lab drafts and practice history in this browser? Export the current lab first to keep it.'))return;lab.stop();saved=imported;save();select(current,{persist:false});notice('Lab backup imported. Roadmap topic statuses were preserved.');}catch(error){notice('Import failed: '+error.message+' Your existing lab was kept.');}finally{$('import-lab').value='';}};
const params=new URLSearchParams(location.search),requested=params.get('exercise'),topic=params.get('topic');
select(challenges.find(c=>c.id===requested)|| (topic?challengeForTopic(topic):challenges[0]),{persist:false});
try{
  const response=await fetch('../data/roadmap.json');if(!response.ok)throw new Error('Catalog unavailable');curriculum=await response.json();lessonLinks();
  const lesson=curriculum.topics.find(t=>t.id===topic);
  if(lesson){$('lesson-context').hidden=false;const a=document.createElement('a');a.href=`../lessons/${lesson.id}/`;a.textContent='From your lesson: '+lesson.title+' ↗';$('lesson-context').replaceChildren(a);
    if(current.id==='playground'&&lesson.code&&!Object.hasOwn(saved.drafts,'playground')){$('python-code').value=lesson.code;lines();}
  }
}catch{notice('Lesson links could not load. The coding challenges and editor are still available.');}
window.addEventListener('pagehide',()=>lab.stop());
