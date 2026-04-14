/**
 * Professional curriculum knowledge network (vis-network + JSON graph).
 */
(function () {
    'use strict';

    var RELATION_COLORS = {
        foundation: { color: '#5a6b4a', highlight: '#2e3105' },
        prerequisite: { color: '#8b7355', highlight: '#2e3105' },
        extends: { color: '#9aa64a', highlight: '#2e3105' },
        applies: { color: '#6b8e9e', highlight: '#2e3105' },
        related: { color: '#b7bb7e', highlight: '#2e3105' }
    };

    function edgeColor(relation) {
        var p = RELATION_COLORS[relation] || RELATION_COLORS.related;
        return { color: p.color, highlight: p.highlight };
    }

    function fetchGraphJson() {
        var urls = ['/js/knowledge_graph.json', 'js/knowledge_graph.json', '../js/knowledge_graph.json'];
        function attempt(i) {
            if (i >= urls.length) return Promise.reject(new Error('Knowledge graph JSON not found'));
            return fetch(urls[i])
                .then(function (r) {
                    if (!r.ok) return attempt(i + 1);
                    return r.json();
                })
                .catch(function () {
                    return attempt(i + 1);
                });
        }
        return attempt(0);
    }

    function buildData(raw) {
        if (typeof vis === 'undefined') {
            console.warn('vis-network not loaded; knowledge graph skipped');
            return null;
        }
        var nodes = new vis.DataSet(
            raw.nodes.map(function (n) {
                var o = {
                    id: n.id,
                    label: n.label,
                    title: n.title || n.label,
                    group: n.group || 'discipline'
                };
                if (n.href) o.href = n.href;
                return o;
            })
        );
        var edges = new vis.DataSet(
            raw.edges.map(function (e, i) {
                return {
                    id: 'e-' + i,
                    from: e.from,
                    to: e.to,
                    label: e.relation || '',
                    arrows: 'to',
                    color: edgeColor(e.relation),
                    font: { size: 11, align: 'middle', strokeWidth: 0 },
                    smooth: { type: 'dynamic', roundness: 0.35 }
                };
            })
        );
        return { nodes: nodes, edges: edges };
    }

    function networkOptions(physicsEnabled) {
        return {
            physics: {
                enabled: physicsEnabled !== false,
                stabilization: { iterations: 220 },
                barnesHut: {
                    gravitationalConstant: -5200,
                    centralGravity: 0.18,
                    springLength: 140,
                    springConstant: 0.035,
                    damping: 0.58
                }
            },
            interaction: { hover: true, tooltipDelay: 120, navigationButtons: true, keyboard: true },
            layout: { improvedLayout: true },
            nodes: {
                shape: 'dot',
                scaling: { min: 12, max: 36 },
                font: { size: 15, face: 'Helvetica Neue, Arial, sans-serif', color: '#2e3105' },
                borderWidth: 2,
                shadow: true
            },
            edges: { width: 2, selectionWidth: 3 },
            groups: {
                root: { color: { background: '#2e3105', border: '#dee777', highlight: '#1a1c03' }, font: { color: '#fdffe9', size: 18 } },
                foundation: { color: { background: '#b7bb7e', border: '#2e3105' } },
                discipline: { color: { background: '#dee777', border: '#2e3105' } },
                topic: { color: { background: '#fffcc0', border: '#5a5d3a' }, font: { size: 14 } },
                cross: { color: { background: '#e8ead0', border: '#6b8e9e' }, shape: 'diamond' }
            }
        };
    }

    function mount(container, data, opts) {
        var physicsOn = opts.physics !== false;
        var net = new vis.Network(container, data, networkOptions(physicsOn));

        net.on('click', function (ctx) {
            if (!ctx.nodes.length) return;
            var id = ctx.nodes[0];
            var node = data.nodes.get(id);
            if (node && node.href) {
                window.location.href = node.href;
            }
        });

        return net;
    }

    function addToolbar(container, network, physicsInitiallyOn) {
        var bar = document.createElement('div');
        bar.className = 'kg-toolbar';
        bar.style.cssText =
            'display:flex;flex-wrap:wrap;gap:0.5rem;align-items:center;margin-bottom:0.75rem;justify-content:center;';
        var physicsOn = physicsInitiallyOn !== false;
        var physicsBtn = document.createElement('button');
        physicsBtn.type = 'button';
        physicsBtn.className = 'academic-button academic-button-secondary';
        physicsBtn.style.cssText = 'padding:6px 14px;font-size:0.85rem;cursor:pointer;';
        physicsBtn.textContent = physicsOn ? 'Pause physics' : 'Resume physics';
        physicsBtn.addEventListener('click', function () {
            physicsOn = !physicsOn;
            network.setOptions({ physics: { enabled: physicsOn } });
            physicsBtn.textContent = physicsOn ? 'Pause physics' : 'Resume physics';
        });
        var fitBtn = document.createElement('button');
        fitBtn.type = 'button';
        fitBtn.className = 'academic-button academic-button-secondary';
        fitBtn.style.cssText = 'padding:6px 14px;font-size:0.85rem;cursor:pointer;';
        fitBtn.textContent = 'Fit view';
        fitBtn.addEventListener('click', function () {
            network.fit({ animation: { duration: 380, easingFunction: 'easeInOutQuad' } });
        });
        bar.appendChild(physicsBtn);
        bar.appendChild(fitBtn);
        container.parentNode.insertBefore(bar, container);
    }

    function initMount(el) {
        var physics = el.getAttribute('data-kg-physics') !== 'off';
        var toolbar = el.getAttribute('data-kg-toolbar') === 'true';
        fetchGraphJson()
            .then(function (raw) {
                var data = buildData(raw);
                if (!data) return;
                var net = mount(el, data, { physics: physics });
                if (toolbar) addToolbar(el, net, physics);
            })
            .catch(function () {
                el.innerHTML =
                    '<p style="padding:2rem;text-align:center;color:#5a5d3a;">Could not load knowledge graph data. Run the local preview server from the project root (<code>npm run serve</code>) and open this site over HTTP.</p>';
            });
    }

    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('[data-kg-role="mount"]').forEach(initMount);
    });
})();
