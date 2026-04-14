(function(){
  document.addEventListener('DOMContentLoaded', function(){
    var article = document.querySelector('.topic-detail');
    if (!article) return;
    if (article.querySelector('.editorial-note')) return;
    var box = document.createElement('section');
    box.className = 'editorial-note';
    box.style.cssText = 'margin-top:2rem;padding:1rem 1.2rem;border:1px solid #d8dea0;border-radius:8px;background:#fbfce8;font-size:0.95rem;';
    box.innerHTML = '<h3 style="margin-top:0;">Editorial & Source Notes</h3><p>Reviewed by SkytrailGroup Mathematics Editorial Team. Content is updated periodically for accuracy and clarity.</p><ul><li>Primary references: standard university-level textbooks and peer-reviewed educational materials.</li><li>Last editorial check: 2026-04-14.</li></ul>';
    article.appendChild(box);
  });
})();
