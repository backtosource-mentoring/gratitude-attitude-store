(function(){
  var d=document,h=d.querySelector('.site-header'),darkTop=!!d.querySelector('main > section:first-child.dark, main > section:first-child.hero');
  function onScroll(){var y=window.scrollY;if(h)h.classList.toggle('solid',!darkTop||y>40);var sb=d.querySelector('.sticky-buy');if(sb)sb.classList.toggle('show',y>520);}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  var mb=d.querySelector('.menu-btn'),nav=d.querySelector('.nav');
  if(mb&&nav){mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o);});
    nav.addEventListener('click',function(e){if(e.target.tagName==='A'){nav.classList.remove('open');mb.setAttribute('aria-expanded','false');}});}
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
    d.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});}
  else d.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});
  var chips=d.querySelectorAll('.chip');
  chips.forEach(function(c){c.addEventListener('click',function(){var g=c.getAttribute('data-g');
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===c);});
    d.querySelectorAll('.tile[data-g]').forEach(function(t){t.hidden=!(g==='all'||t.getAttribute('data-g')===g);});});});
  d.querySelectorAll('a[data-buy]').forEach(function(a){a.addEventListener('click',function(){
    try{if(window.gtag)gtag('event','amazon_click',{item:a.getAttribute('data-buy')});if(window.plausible)plausible('Amazon Click',{props:{item:a.getAttribute('data-buy')}});}catch(e){}});});
})();
(function(){
  var d=document;
  d.querySelectorAll('a[data-back]').forEach(function(a){a.addEventListener('click',function(e){
    try{if(d.referrer&&new URL(d.referrer).host===location.host&&history.length>1){e.preventDefault();history.back();}}catch(x){}});});
  var prev=d.querySelector('a[data-key=prev]'),next=d.querySelector('a[data-key=next]');
  if(prev||next){d.addEventListener('keydown',function(e){
    var t=e.target.tagName;if(t==='INPUT'||t==='TEXTAREA'||e.metaKey||e.ctrlKey||e.altKey)return;
    if(e.key==='ArrowLeft'&&prev)location.href=prev.href;
    if(e.key==='ArrowRight'&&next)location.href=next.href;});}
})();
