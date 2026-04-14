/**
 * Level-3 hub tabs: filter topic cards by data-subcategory.
 */
(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('[data-category-hub]').forEach(function (hub) {
            var tabs = hub.querySelectorAll('.category-hub-tab');
            var rootSel = hub.getAttribute('data-hub-root');
            var root = hub.closest('main') || document;
            if (rootSel) {
                var scoped = document.querySelector(rootSel);
                if (scoped) root = scoped;
            }
            var cards = root.querySelectorAll('.topic-card[data-subcategory]');

            tabs.forEach(function (tab) {
                tab.addEventListener('click', function () {
                    var key = tab.getAttribute('data-filter') || 'all';
                    tabs.forEach(function (t) {
                        t.classList.toggle('is-active', t === tab);
                    });
                    cards.forEach(function (card) {
                        var sc = card.getAttribute('data-subcategory') || 'all';
                        var show = key === 'all' || sc === key;
                        card.style.display = show ? '' : 'none';
                    });
                });
            });
        });
    });
})();
