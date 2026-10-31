export const STORAGE_KEY='sohila-python-roadmap-v1';
export const STATUSES=['todo','learning','done'];
export function cleanProgress(raw,topicIds){
  if(!raw||raw.schema_version!==1||raw.roadmap!=='python-learning-roadmap'||!raw.topics||typeof raw.topics!=='object'||Array.isArray(raw.topics))throw new Error('This is not a Python roadmap progress backup.');
  const allowed=new Set(topicIds),topics={};
  for(const [id,value] of Object.entries(raw.topics)){
    if(!allowed.has(id))throw new Error('Backup contains an unknown topic: '+id);
    if(!value||!STATUSES.includes(value.status)||typeof value.notes!=='string'||value.notes.length>5000)throw new Error('A topic has an invalid status or note.');
    topics[id]={status:value.status,notes:value.notes};
  }
  return {schema_version:1,roadmap:'python-learning-roadmap',topics};
}
export function emptyProgress(){return {schema_version:1,roadmap:'python-learning-roadmap',topics:{}};}
export function nextTopic(topics,progress){
  const done=id=>progress.topics[id]?.status==='done';
  return topics.find(t=>progress.topics[t.id]?.status==='learning')||topics.find(t=>!done(t.id)&&t.requires.every(done))||topics.find(t=>!done(t.id))||null;
}
export function matchesTopic(topic,query,status,progress){
  const actual=progress.topics[topic.id]?.status||'todo';
  return (status==='all'||actual===status)&&[topic.title,topic.summary,topic.bridge,topic.phase,topic.id,...topic.learn].join(' ').toLowerCase().includes(query.trim().toLowerCase());
}
