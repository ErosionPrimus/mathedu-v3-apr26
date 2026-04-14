(function(){
  var KEY = 'stg_cookie_consent_v1';
  function loadScript(src, attrs){
    var s = document.createElement('script');
    s.src = src;
    s.async = true;
    if (attrs){ Object.keys(attrs).forEach(function(k){ s.setAttribute(k, attrs[k]); }); }
    document.head.appendChild(s);
  }
  function enableTracking(){
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('consent', 'default', { ad_storage: 'granted', analytics_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' });
    gtag('js', new Date());
    gtag('config', 'G-08L01JDD3F');
    loadScript('https://www.googletagmanager.com/gtag/js?id=G-08L01JDD3F');
    loadScript('https://www.googletagmanager.com/gtm.js?id=GTM-T34MKQC7');
    loadScript('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7040270645748987', { crossorigin: 'anonymous' });
  }
  function save(status){ localStorage.setItem(KEY, status); }
  function buildBanner(){
    var bar = document.createElement('div');
    bar.id = 'stg-consent-banner';
    bar.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#1f2408;color:#fff;padding:14px 16px;display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap;font-size:14px;';
    bar.innerHTML = '<span>We use cookies for analytics and ads personalization. You can accept or reject non-essential cookies.</span><span><button id="stg-accept" style="margin-right:8px;padding:6px 10px;">Accept</button><button id="stg-reject" style="padding:6px 10px;">Reject</button></span>';
    document.body.appendChild(bar);
    document.getElementById('stg-accept').onclick = function(){ save('accepted'); enableTracking(); bar.remove(); };
    document.getElementById('stg-reject').onclick = function(){ save('rejected'); bar.remove(); };
  }
  document.addEventListener('DOMContentLoaded', function(){
    var state = localStorage.getItem(KEY);
    if (state === 'accepted') {
      enableTracking();
    } else if (!state) {
      buildBanner();
    }
  });
})();
