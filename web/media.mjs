export function youtubeMedia(value){
  let u;try{u=new URL(value);}catch{return null;}
  if(u.protocol!=='https:'||u.username||u.password||!['youtube.com','www.youtube.com','youtu.be','www.youtube-nocookie.com'].includes(u.hostname))return null;
  const playlist=u.searchParams.get('list');
  if(playlist&&/^[A-Za-z0-9_-]{12,100}$/.test(playlist))return {kind:'playlist',id:playlist,url:`https://www.youtube.com/playlist?list=${playlist}`,embed:`https://www.youtube-nocookie.com/embed/videoseries?list=${playlist}&playsinline=1&rel=0`};
  const id=u.hostname==='youtu.be'?u.pathname.split('/')[1]:u.pathname.startsWith('/embed/')?u.pathname.split('/')[2]:u.searchParams.get('v');
  if(!/^[A-Za-z0-9_-]{11}$/.test(id||''))return null;
  return {kind:'video',id,url:`https://www.youtube.com/watch?v=${id}`,embed:`https://www.youtube-nocookie.com/embed/${id}?playsinline=1&rel=0`,poster:`https://i.ytimg.com/vi/${id}/hqdefault.jpg`};
}
export const escapeHTML=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function mediaPreview(resource){
  const m=youtubeMedia(resource.url);if(!m)return '';
  const title=escapeHTML(resource.title),encoded=escapeHTML(resource.url);
  return `<div class="media-preview" data-media-url="${encoded}" data-media-title="${title}"><button class="media-poster ${m.kind}" data-load-media aria-label="Preview ${m.kind}: ${title}">${m.poster?`<img src="${m.poster}" alt="" loading="lazy" width="480" height="360" referrerpolicy="no-referrer">`:'<span class="playlist-graphic" aria-hidden="true">▤</span>'}<span class="media-play" aria-hidden="true">▶</span><span class="media-label">${m.kind==='playlist'?'Explore playlist':'Watch preview'}</span></button><div class="media-player-slot"></div><p class="media-fallback">Loads YouTube on request. <a href="${m.url}" target="_blank" rel="noopener noreferrer">Open on YouTube ↗</a> if the owner restricts embedding.</p></div>`;
}
export function bindMediaPreviews(root=document){
  root.addEventListener('click',event=>{
    const load=event.target.closest('[data-load-media]'),stop=event.target.closest('[data-stop-media]');
    if(stop){const wrap=stop.closest('[data-media-url]');wrap.querySelector('.media-player-slot').replaceChildren();wrap.querySelector('[data-load-media]').hidden=false;wrap.querySelector('[data-load-media]').focus();return;}
    if(!load)return;
    const wrap=load.closest('[data-media-url]'),m=youtubeMedia(wrap.dataset.mediaUrl);if(!m)return;
    // Keep one preview active so browsing a shelf does not start dozens of players.
    for(const active of root.querySelectorAll('[data-media-url]')){active.querySelector('.media-player-slot').replaceChildren();active.querySelector('[data-load-media]').hidden=false;}
    const iframe=document.createElement('iframe');iframe.src=m.embed;iframe.title=wrap.dataset.mediaTitle+' · YouTube '+m.kind;iframe.className='video-frame';iframe.loading='lazy';iframe.referrerPolicy='strict-origin-when-cross-origin';iframe.allow='accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen';iframe.allowFullscreen=true;
    const close=document.createElement('button');close.type='button';close.dataset.stopMedia='';close.className='close-preview';close.textContent='Close preview ×';
    wrap.querySelector('.media-player-slot').append(iframe,close);load.hidden=true;close.focus();
  });
}
