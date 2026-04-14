/**
 * Intelligent Academic Interactions
 * High-intelligence animations and effects for academic widgets
 * Based on Cedar Design System with academic styling
 */

(function() {
    'use strict';
    
    // Wait for DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Academic Interactions initialized');
        
        // Initialize all academic interaction modules
        initTheoremInteractions();
        initEquationInteractions();
        initKnowledgeGraph();
        initQuizSystem();
        initAcademicNavigation();
        initScrollAnimations();
        initCitationSystem();
        initResearchInteractions();
    });
    
    /**
     * Theorem Interactions Module
     * Handles proof toggling, step-by-step animations, and theorem interactions
     */
    function initTheoremInteractions() {
        // Find all theorem proof toggles
        const proofToggles = document.querySelectorAll('.theorem-proof-toggle');
        
        proofToggles.forEach(toggle => {
            toggle.addEventListener('click', function() {
                const theoremWidget = this.closest('.theorem-widget');
                const proofWidget = theoremWidget.nextElementSibling;
                
                if (proofWidget && proofWidget.classList.contains('proof-widget')) {
                    // Toggle proof visibility
                    proofWidget.classList.toggle('active');
                    
                    // Update button text
                    const isActive = proofWidget.classList.contains('active');
                    this.innerHTML = isActive ? 
                        '<span>Hide Proof</span> <span>▼</span>' : 
                        '<span>Show Proof</span> <span>▶</span>';
                    
                    // Animate proof steps if showing
                    if (isActive) {
                        animateProofSteps(proofWidget);
                    }
                    
                    // Add subtle animation to theorem widget
                    theoremWidget.style.animation = 'none';
                    setTimeout(() => {
                        theoremWidget.style.animation = 'academicPulse 0.5s ease';
                    }, 10);
                }
            });
        });
        
        // Add hover effects to theorem widgets
        const theoremWidgets = document.querySelectorAll('.theorem-widget');
        theoremWidgets.forEach(widget => {
            widget.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-6px)';
                this.style.boxShadow = 'var(--academic-shadow-lg)';
            });
            
            widget.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = 'var(--academic-shadow-sm)';
            });
        });
    }
    
    /**
     * Animate proof steps with intelligent sequencing
     * @param {HTMLElement} proofWidget - The proof widget element
     */
    function animateProofSteps(proofWidget) {
        const proofSteps = proofWidget.querySelectorAll('.proof-step');
        
        // Reset all steps
        proofSteps.forEach(step => {
            step.style.opacity = '0';
            step.style.transform = 'translateX(-20px)';
        });
        
        // Animate steps sequentially
        proofSteps.forEach((step, index) => {
            setTimeout(() => {
                step.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
                step.style.opacity = '1';
                step.style.transform = 'translateX(0)';
                
                // Add subtle highlight effect
                step.style.backgroundColor = 'rgba(255, 252, 192, 0.2)';
                setTimeout(() => {
                    step.style.backgroundColor = '';
                }, 300);
                
            }, index * 200); // 200ms delay between steps
        });
    }
    
    /**
     * Equation Interactions Module
     * Handles equation solving, variable highlighting, and solution toggling
     */
    function initEquationInteractions() {
        const equationWidgets = document.querySelectorAll('.equation-widget');
        
        equationWidgets.forEach(widget => {
            // Add click interaction to show solution
            widget.addEventListener('click', function() {
                const solution = this.querySelector('.equation-solution');
                if (solution) {
                    solution.classList.toggle('active');
                    
                    // Add visual feedback
                    this.style.backgroundColor = 'var(--academic-light)';
                    setTimeout(() => {
                        this.style.backgroundColor = '';
                    }, 500);
                }
            });
            
            // Add hover effects
            widget.addEventListener('mouseenter', function() {
                const equation = this.querySelector('span');
                if (equation) {
                    equation.style.transition = 'all 0.3s ease';
                    equation.style.transform = 'scale(1.05)';
                    equation.style.color = 'var(--academic-secondary)';
                }
            });
            
            widget.addEventListener('mouseleave', function() {
                const equation = this.querySelector('span');
                if (equation) {
                    equation.style.transform = 'scale(1)';
                    equation.style.color = '';
                }
            });
        });
        
        // Add variable highlighting for equations
        highlightEquationVariables();
    }
    
    /**
     * Highlight variables in equations with intelligent color coding
     */
    function highlightEquationVariables() {
        const equations = document.querySelectorAll('.equation-widget');
        const variableColors = {
            'x': '#dee777',
            'y': '#b7bb7e',
            'z': '#2e3105',
            'a': '#fffcc0',
            'b': '#5a5d3a',
            'c': '#fdffe9'
        };
        
        equations.forEach(equation => {
            const text = equation.textContent;
            Object.keys(variableColors).forEach(variable => {
                if (text.includes(variable)) {
                    const regex = new RegExp(`(${variable})`, 'g');
                    const highlightedText = text.replace(regex, 
                        `<span style="color: ${variableColors[variable]}; font-weight: 700;">$1</span>`);
                    equation.innerHTML = highlightedText;
                }
            });
        });
    }
    
    /**
     * Knowledge Graph Module
     * Creates interactive knowledge graph with animated connections
     */
    function initKnowledgeGraph() {
        const knowledgeGraph = document.querySelector('.knowledge-graph-widget:not([data-vis-network])');
        if (!knowledgeGraph) return;
        
        // Create knowledge nodes
        const knowledgeNodes = [
            { id: 1, label: 'Algebra', x: '30%', y: '30%' },
            { id: 2, label: 'Geometry', x: '70%', y: '30%' },
            { id: 3, label: 'Calculus', x: '50%', y: '50%' },
            { id: 4, label: 'Statistics', x: '30%', y: '70%' },
            { id: 5, label: 'Logic', x: '70%', y: '70%' }
        ];
        
        // Create connections between nodes
        const connections = [
            { from: 1, to: 3 },
            { from: 2, to: 3 },
            { from: 3, to: 4 },
            { from: 3, to: 5 },
            { from: 1, to: 2 }
        ];
        
        // Create nodes with animations
        knowledgeNodes.forEach((node, index) => {
            setTimeout(() => {
                createKnowledgeNode(node, index);
            }, index * 300);
        });
        
        // Create connections after nodes are created
        setTimeout(() => {
            connections.forEach(connection => {
                createKnowledgeConnection(connection);
            });
        }, knowledgeNodes.length * 300);
        
        /**
         * Create a knowledge node with animation
         * @param {Object} node - Node configuration
         * @param {number} index - Node index for animation delay
         */
        function createKnowledgeNode(node, index) {
            const nodeElement = document.createElement('div');
            nodeElement.className = 'knowledge-node';
            nodeElement.id = `knowledge-node-${node.id}`;
            nodeElement.textContent = node.label;
            nodeElement.style.left = node.x;
            nodeElement.style.top = node.y;
            nodeElement.style.opacity = '0';
            nodeElement.style.transform = 'scale(0)';
            
            // Add click interaction
            nodeElement.addEventListener('click', function() {
                highlightKnowledgeConnections(node.id);
                showNodeInfo(node);
            });
            
            knowledgeGraph.appendChild(nodeElement);
            
            // Animate node appearance
            setTimeout(() => {
                nodeElement.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
                nodeElement.style.opacity = '1';
                nodeElement.style.transform = 'scale(1)';
            }, 50);
        }
        
        /**
         * Create connection between nodes
         * @param {Object} connection - Connection configuration
         */
        function createKnowledgeConnection(connection) {
            const fromNode = document.getElementById(`knowledge-node-${connection.from}`);
            const toNode = document.getElementById(`knowledge-node-${connection.to}`);
            
            if (!fromNode || !toNode) return;
            
            const connectionElement = document.createElement('div');
            connectionElement.className = 'knowledge-connection';
            connectionElement.style.opacity = '0';
            
            // Calculate connection position and angle
            const fromRect = fromNode.getBoundingClientRect();
            const toRect = toNode.getBoundingClientRect();
            const graphRect = knowledgeGraph.getBoundingClientRect();
            
            const x1 = fromRect.left - graphRect.left + fromRect.width / 2;
            const y1 = fromRect.top - graphRect.top + fromRect.height / 2;
            const x2 = toRect.left - graphRect.left + toRect.width / 2;
            const y2 = toRect.top - graphRect.top + toRect.height / 2;
            
            const length = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
            
            connectionElement.style.width = `${length}px`;
            connectionElement.style.height = '2px';
            connectionElement.style.left = `${x1}px`;
            connectionElement.style.top = `${y1}px`;
            connectionElement.style.transform = `rotate(${angle}deg)`;
            connectionElement.style.transformOrigin = '0 0';
            
            knowledgeGraph.appendChild(connectionElement);
            
            // Animate connection appearance
            setTimeout(() => {
                connectionElement.style.transition = 'opacity 1s ease';
                connectionElement.style.opacity = '0.3';
            }, 1000);
        }
    }
    
    /**
     * Highlight connections for a specific node
     * @param {number} nodeId - ID of the node to highlight connections for
     */
    function highlightKnowledgeConnections(nodeId) {
        // Reset all nodes
        document.querySelectorAll('.knowledge-node').forEach(node => {
            node.style.backgroundColor = 'var(--academic-primary)';
            node.style.transform = 'scale(1)';
        });
        
        // Highlight selected node
        const selectedNode = document.getElementById(`knowledge-node-${nodeId}`);
        if (selectedNode) {
            selectedNode.style.backgroundColor = 'var(--academic-secondary)';
            selectedNode.style.color = 'var(--academic-bg)';
            selectedNode.style.transform = 'scale(1.2)';
            
            // Add pulse animation
            selectedNode.style.animation = 'academicPulse 1s infinite';
            
            // Reset after 2 seconds
            setTimeout(() => {
                selectedNode.style.backgroundColor = 'var(--academic-primary)';
                selectedNode.style.color = 'var(--academic-secondary)';
                selectedNode.style.transform = 'scale(1)';
                selectedNode.style.animation = '';
            }, 2000);
        }
    }
    
    /**
     * Show information for a knowledge node
     * @param {Object} node - Node to show info for
     */
    function showNodeInfo(node) {
        // Create or update info display
        let infoDisplay = document.querySelector('.node-info-display');
        if (!infoDisplay) {
            infoDisplay = document.createElement('div');
            infoDisplay.className = 'node-info-display';
            infoDisplay.style.cssText = `
                position: fixed;
                top: 100px;
                right: 20px;
                background: var(--academic-bg);
                border: 2px solid var(--academic-primary);
                border-radius: 12px;
                padding: 20px;
                max-width: 300px;
                box-shadow: var(--academic-shadow-lg);
                z-index: 1001;
                opacity: 0;
                transform: translateY(-20px);
                transition: all 0.3s ease;
            `;
            document.body.appendChild(infoDisplay);
        }
        
        // Update content
        infoDisplay.innerHTML = `
            <h3 style="color: var(--academic-secondary); margin-bottom: 10px;">${node.label}</h3>
            <p style="color: var(--academic-text); line-height: 1.6;">
                ${getNodeDescription(node.label)}
            </p>
            <button class="close-info" style="
                position: absolute;
                top: 10px;
                right: 10px;
                background: none;
                border: none;
                font-size: 20px;
                cursor: pointer;
                color: var(--academic-text-light);
            ">×</button>
        `;
        
        // Show with animation
        setTimeout(() => {
            infoDisplay.style.opacity = '1';
            infoDisplay.style.transform = 'translateY(0)';
        }, 10);
        
        // Add close button listener
        infoDisplay.querySelector('.close-info').addEventListener('click', function() {
            infoDisplay.style.opacity = '0';
            infoDisplay.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                infoDisplay.remove();
            }, 300);
        });
    }
    
    /**
     * Get description for a knowledge node
     * @param {string} label - Node label
     * @returns {string} - Node description
     */
    function getNodeDescription(label) {
        const descriptions = {
            'Algebra': 'Study of mathematical symbols and rules for manipulating them.',
            'Geometry': 'Branch of mathematics dealing with shapes, sizes, and properties of space.',
            'Calculus': 'Mathematical study of continuous change and motion.',
            'Statistics': 'Science of collecting, analyzing, and interpreting data.',
            'Logic': 'Study of valid reasoning and argumentation.'
        };
        
        return descriptions[label] || 'A fundamental branch of mathematics.';
    }
    
    /**
     * Quiz System Module
     * Interactive quiz with intelligent feedback and scoring
     */
    function initQuizSystem() {
        const quizOptions = document.querySelectorAll('.quiz-option');
        const quizFeedback = document.querySelector('.quiz-feedback');
        
        quizOptions.forEach(option => {
            option.addEventListener('click', function() {
                // Clear previous selections
                quizOptions.forEach(opt => {
                    opt.classList.remove('selected');
                    opt.style.backgroundColor = '';
                });
                
                // Select this option
                this.classList.add('selected');
                this.style.backgroundColor = 'var(--academic-primary)';
                
                // Check answer
                const isCorrect = this.dataset.correct === 'true';
                showQuizFeedback(isCorrect);
                
                // Update progress
                updateQuizProgress();
            });
        });
    }
    
    /**
     * Show feedback for quiz answers
     * @param {boolean} isCorrect - Whether the answer is correct
     */
    function showQuizFeedback(isCorrect) {
        const feedback = document.querySelector('.quiz-feedback');
        if (!feedback) return;
        
        feedback.className = isCorrect ? 'quiz-feedback correct' : 'quiz-feedback incorrect';
        feedback.textContent = isCorrect ? 
            '✓ Correct! Excellent understanding.' : 
            '✗ Incorrect. Review the concepts and try again.';
        
        // Add detailed explanation for incorrect answers
        if (!isCorrect) {
            const explanation = document.createElement('p');
            explanation.style.marginTop = '10px';
            explanation.style.fontSize = '0.9rem';
            explanation.style.color = 'inherit';
            explanation.textContent = 'Hint: Consider the fundamental principles involved.';
            feedback.appendChild(explanation);
        }
    }
    
    /**
     * Update quiz progress indicator
     */
    function updateQuizProgress() {
        const selectedOptions = document.querySelectorAll('.quiz-option.selected');
        const totalOptions = document.querySelectorAll('.quiz-option').length;
        
        // Create or update progress indicator
        let progressIndicator = document.querySelector('.quiz-progress');
        if (!progressIndicator) {
            progressIndicator = document.createElement('div');
            progressIndicator.className = 'quiz-progress';
            progressIndicator.style.cssText = `
                margin-top: 20px;
                text-align: center;
                font-size: 0.9rem;
                color: var(--academic-text-light);
            `;
            document.querySelector('.quiz-widget').appendChild(progressIndicator);
        }
        
        progressIndicator.textContent = `Progress: ${selectedOptions.length}/${totalOptions}`;
        
        // Show completion message
        if (selectedOptions.length === totalOptions) {
            setTimeout(() => {
                const completionMessage = document.createElement('div');
                completionMessage.className = 'quiz-completion';
                completionMessage.style.cssText = `
                    margin-top: 20px;
                    padding: 15px;
                    background: var(--academic-primary);
                    color: var(--academic-secondary);
                    border-radius: 8px;
                    font-weight: 600;
                    text-align: center;
                    animation: fadeIn 0.6s ease;
                `;
                completionMessage.textContent = '🎉 Quiz Completed! Excellent work.';
                document.querySelector('.quiz-widget').appendChild(completionMessage);
            }, 500);
        }
    }
    
    /**
     * Academic Navigation Module
     * Enhanced navigation with smooth scrolling and progress indicators
     */
    function initAcademicNavigation() {
        const navLinks = document.querySelectorAll('.academic-nav-link');
        const sections = document.querySelectorAll('section, .theorem-widget, .research-widget');
        
        // Update active nav link on scroll
        window.addEventListener('scroll', debounce(() => {
            let currentSection = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                
                if (window.scrollY >= sectionTop - 200) {
                    currentSection = section.id;
                }
            });
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${currentSection}`) {
                    link.classList.add('active');
                    link.style.color = 'var(--academic-secondary)';
                    link.style.fontWeight = '700';
                } else {
                    link.style.color = '';
                    link.style.fontWeight = '';
                }
            });
        }, 100));
    }
    
    /**
     * Scroll Animations Module
     * Animate elements on scroll with intelligent sequencing
     */
    function initScrollAnimations() {
        const animateElements = document.querySelectorAll(
            '.theorem-widget, .definition-widget, .example-widget, .research-widget'
        );
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Stagger animations based on element type and position
                    const delay = index * 100;
                    
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        
                        // Add specific animation based on element type
                        if (entry.target.classList.contains('theorem-widget')) {
                            entry.target.style.animation = 'theoremReveal 0.6s ease';
                        } else if (entry.target.classList.contains('research-widget')) {
                            entry.target.style.animation = 'fadeInUp 0.8s ease';
                        }
                    }, delay);
                    
                    // Unobserve after animation
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        });
        
        // Set initial state and observe
        animateElements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            observer.observe(element);
        });
    }
    
    /**
     * Citation System Module
     * Interactive citation system with hover effects and references
     */
    function initCitationSystem() {
        const citationWidgets = document.querySelectorAll('.citation-widget');
        
        citationWidgets.forEach(citation => {
            // Add click to copy reference
            citation.addEventListener('click', function() {
                const author = this.querySelector('.citation-author').textContent;
                const title = this.querySelector('.citation-title').textContent;
                const reference = `${author}. "${title}".`;
                
                // Copy to clipboard
                navigator.clipboard.writeText(reference).then(() => {
                    // Show confirmation
                    const confirmation = document.createElement('div');
                    confirmation.textContent = '✓ Copied to clipboard';
                    confirmation.style.cssText = `
                        position: absolute;
                        top: -30px;
                        left: 0;
                        background: var(--academic-primary);
                        color: var(--academic-secondary);
                        padding: 5px 10px;
                        border-radius: 4px;
                        font-size: 0.8rem;
                        animation: fadeInUp 0.3s ease;
                    `;
                    this.appendChild(confirmation);
                    
                    setTimeout(() => {
                        confirmation.remove();
                    }, 2000);
                });
            });
        });
    }
    
    /**
     * Research Interactions Module
     * Enhanced research paper widgets with metrics and interactions
     */
    function initResearchInteractions() {
        const researchWidgets = document.querySelectorAll('.research-widget');
        
        researchWidgets.forEach(widget => {
            // Add hover expansion for abstract
            const abstract = widget.querySelector('.research-abstract');
            if (abstract) {
                const originalText = abstract.textContent;
                const shortenedText = originalText.length > 200 ? 
                    originalText.substring(0, 200) + '...' : originalText;
                
                abstract.textContent = shortenedText;
                
                if (originalText.length > 200) {
                    abstract.style.cursor = 'pointer';
                    abstract.addEventListener('click', function() {
                        this.textContent = this.textContent.endsWith('...') ? 
                            originalText : shortenedText;
                    });
                }
            }
            
            // Animate metrics on hover
            const metrics = widget.querySelectorAll('.metric-value');
            metrics.forEach(metric => {
                const originalValue = metric.textContent;
                let animated = false;
                
                widget.addEventListener('mouseenter', () => {
                    if (!animated) {
                        animateMetricValue(metric, originalValue);
                        animated = true;
                    }
                });
            });
        });
    }
    
    /**
     * Animate metric value counting
     * @param {HTMLElement} element - Metric element to animate
     * @param {string} targetValue - Target value to count to
     */
    function animateMetricValue(element, targetValue) {
        const target = parseInt(targetValue.replace(/\D/g, ''));
        let current = 0;
        const increment = target / 30; // 30 steps
        const duration = 1000; // 1 second
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, duration / 30);
    }
    
    /**
     * Utility: Debounce function for performance
     * @param {Function} func - Function to debounce
     * @param {number} wait - Wait time in milliseconds
     * @returns {Function} - Debounced function
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    /**
     * Utility: Throttle function for performance
     * @param {Function} func - Function to throttle
     * @param {number} limit - Time limit in milliseconds
     * @returns {Function} - Throttled function
     */
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
    
    // Add CSS for additional animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes theoremReveal {
            0% {
                opacity: 0;
                transform: translateY(30px) rotateX(10deg);
            }
            100% {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }
        
        .active {
            color: var(--academic-secondary) !important;
            font-weight: 700 !important;
        }
        
        .active::after {
            width: 100% !important;
        }
    `;
    document.head.appendChild(style);
    
    // Public API for external integration
    window.AcademicInteractions = {
        initTheoremInteractions,
        initEquationInteractions,
        initKnowledgeGraph,
        initQuizSystem,
        initAcademicNavigation,
        initScrollAnimations,
        initCitationSystem,
        initResearchInteractions,
        debounce,
        throttle
    };
    
})();