/**
 * Intelligent Academic Widgets System
 * Core JavaScript for academic widgets functionality
 * Based on Cedar Design System colors with academic intelligence
 */

(function() {
    'use strict';
    
    console.log('Intelligent Academic Widgets System initialized');
    
    // Initialize all widget systems
    initTheoremProofSystem();
    initEquationInteractivity();
    initKnowledgeGraphSystem();
    initQuizIntelligence();
    initAcademicNavigation();
    initScrollBasedAnimations();
    
    /**
     * Theorem Proof System
     * Handles proof toggling, step animations, and theorem interactions
     */
    function initTheoremProofSystem() {
        const theoremToggles = document.querySelectorAll('.theorem-proof-toggle');
        
        theoremToggles.forEach((toggle, index) => {
            toggle.addEventListener('click', function() {
                const theoremWidget = this.closest('.theorem-widget');
                const proofWidget = findNextProofWidget(theoremWidget);
                
                if (proofWidget) {
                    const isActive = proofWidget.classList.contains('active');
                    
                    // Toggle proof visibility
                    proofWidget.classList.toggle('active');
                    
                    // Update button state
                    updateToggleButton(this, !isActive);
                    
                    // Animate proof if showing
                    if (!isActive) {
                        animateProofSteps(proofWidget);
                    }
                    
                    // Add visual feedback to theorem
                    highlightTheorem(theoremWidget);
                }
            });
            
            // Add sequential animation delay
            toggle.parentElement.style.setProperty('--animation-delay', `${index * 0.1}s`);
        });
        
        // Add theorem hover effects
        document.querySelectorAll('.theorem-widget').forEach(theorem => {
            theorem.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-8px)';
                this.style.boxShadow = 'var(--academic-shadow-lg)';
                
                // Add subtle glow effect
                const glow = document.createElement('div');
                glow.className = 'theorem-glow';
                glow.style.cssText = `
                    position: absolute;
                    top: -2px;
                    left: -2px;
                    right: -2px;
                    bottom: -2px;
                    background: radial-gradient(circle at center, 
                        var(--color-academic-primary) 0%, 
                        transparent 70%);
                    opacity: 0.1;
                    border-radius: inherit;
                    pointer-events: none;
                    z-index: -1;
                `;
                this.appendChild(glow);
            });
            
            theorem.addEventListener('mouseleave', function() {
                this.style.transform = '';
                this.style.boxShadow = '';
                
                const glow = this.querySelector('.theorem-glow');
                if (glow) glow.remove();
            });
        });
    }
    
    /**
     * Find the next proof widget after a theorem
     * @param {HTMLElement} theoremWidget - The theorem widget element
     * @returns {HTMLElement|null} - The proof widget or null
     */
    function findNextProofWidget(theoremWidget) {
        let nextElement = theoremWidget.nextElementSibling;
        while (nextElement) {
            if (nextElement.classList.contains('proof-widget')) {
                return nextElement;
            }
            nextElement = nextElement.nextElementSibling;
        }
        return null;
    }
    
    /**
     * Update toggle button state
     * @param {HTMLElement} button - The toggle button
     * @param {boolean} isActive - Whether the proof is active
     */
    function updateToggleButton(button, isActive) {
        const icon = button.querySelector('i') || button.querySelector('span:last-child');
        if (icon) {
            if (icon.tagName === 'I') {
                icon.className = isActive ? 'fas fa-chevron-down' : 'fas fa-chevron-right';
            } else {
                icon.textContent = isActive ? '▼' : '▶';
            }
        }
        
        const text = button.querySelector('span:first-child');
        if (text) {
            text.textContent = isActive ? 'Hide Proof' : 'Show Proof';
        }
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
            step.style.transition = 'none';
        });
        
        // Animate steps sequentially with intelligent delays
        proofSteps.forEach((step, index) => {
            setTimeout(() => {
                step.style.transition = 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
                step.style.opacity = '1';
                step.style.transform = 'translateX(0)';
                
                // Add step highlight effect
                step.style.backgroundColor = 'rgba(255, 252, 192, 0.3)';
                setTimeout(() => {
                    step.style.backgroundColor = '';
                }, 500);
                
                // Add step number visualization
                if (!step.querySelector('.step-number')) {
                    const stepNumber = document.createElement('span');
                    stepNumber.className = 'step-number';
                    stepNumber.textContent = index + 1;
                    stepNumber.style.cssText = `
                        position: absolute;
                        left: -30px;
                        top: 0;
                        width: 24px;
                        height: 24px;
                        background: var(--color-academic-primary);
                        color: var(--color-academic-secondary);
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 0.8rem;
                        font-weight: bold;
                    `;
                    step.style.position = 'relative';
                    step.appendChild(stepNumber);
                }
                
            }, index * 200); // Staggered animation
        });
    }
    
    /**
     * Highlight theorem with visual feedback
     * @param {HTMLElement} theoremWidget - The theorem widget element
     */
    function highlightTheorem(theoremWidget) {
        theoremWidget.style.animation = 'none';
        setTimeout(() => {
            theoremWidget.style.animation = 'theoremPulse 0.6s ease';
        }, 10);
        
        // Add CSS for theorem pulse animation
        if (!document.querySelector('#theorem-pulse-animation')) {
            const style = document.createElement('style');
            style.id = 'theorem-pulse-animation';
            style.textContent = `
                @keyframes theoremPulse {
                    0%, 100% { 
                        box-shadow: var(--academic-shadow-md); 
                        transform: translateY(0); 
                    }
                    50% { 
                        box-shadow: 0 0 30px rgba(222, 231, 119, 0.3); 
                        transform: translateY(-2px); 
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    /**
     * Equation Interactivity System
     * Handles equation manipulation, variable highlighting, and solution toggling
     */
    function initEquationInteractivity() {
        const equationWidgets = document.querySelectorAll('.equation-widget');
        
        equationWidgets.forEach((equation, index) => {
            // Add click interaction for solution toggling
            equation.addEventListener('click', function(e) {
                if (e.target.closest('.academic-button')) return;
                
                const solution = this.querySelector('.equation-solution');
                if (solution) {
                    const isActive = solution.classList.contains('active');
                    
                    if (!isActive) {
                        solution.classList.add('active');
                        animateEquationSolution(solution);
                    }
                }
            });
            
            // Add variable highlighting
            highlightEquationVariables(equation);
            
            // Add equation animation
            equation.style.setProperty('--equation-index', index);
            equation.classList.add(`equation-delay-${(index % 5) * 100}`);
        });
        
        // Add CSS for equation animations
        addEquationAnimationStyles();
    }
    
    /**
     * Highlight variables in equations with intelligent color coding
     * @param {HTMLElement} equation - The equation widget element
     */
    function highlightEquationVariables(equation) {
        // Disabled due to conflicts with MathJax rendering
        return;
    }
    
    /**
     * Show information about a mathematical variable
     * @param {string} variable - The variable name
     * @param {HTMLElement} equation - The parent equation widget
     */
    function showVariableInfo(variable, equation) {
        const info = getVariableInfo(variable);
        const tooltip = document.createElement('div');
        tooltip.className = 'variable-tooltip';
        tooltip.innerHTML = `
            <strong>${variable}</strong><br>
            <small>${info.description}</small>
        `;
        tooltip.style.cssText = `
            position: absolute;
            background: var(--color-academic-secondary);
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.9rem;
            z-index: 1000;
            max-width: 200px;
            box-shadow: var(--academic-shadow-lg);
            pointer-events: none;
            transform: translateY(-100%);
            opacity: 0;
            transition: all 0.3s ease;
        `;
        
        equation.appendChild(tooltip);
        
        // Position tooltip
        const rect = equation.getBoundingClientRect();
        tooltip.style.left = '50%';
        tooltip.style.top = '-10px';
        tooltip.style.transform = 'translateX(-50%) translateY(-100%)';
        
        // Show tooltip
        setTimeout(() => {
            tooltip.style.opacity = '1';
            tooltip.style.transform = 'translateX(-50%) translateY(-120%)';
        }, 10);
        
        // Remove tooltip after delay
        setTimeout(() => {
            tooltip.style.opacity = '0';
            tooltip.style.transform = 'translateX(-50%) translateY(-100%)';
            setTimeout(() => tooltip.remove(), 300);
        }, 2000);
    }
    
    /**
     * Get information about a mathematical variable
     * @param {string} variable - The variable name
     * @returns {Object} - Variable information
     */
    function getVariableInfo(variable) {
        const infoMap = {
            'x': { description: 'Independent variable, often representing horizontal coordinate' },
            'y': { description: 'Dependent variable, often representing vertical coordinate' },
            'z': { description: 'Third variable, often representing depth in 3D space' },
            'a': { description: 'Coefficient or constant in equations' },
            'b': { description: 'Coefficient or constant in equations' },
            'c': { description: 'Constant term or coefficient' },
            'n': { description: 'Integer variable, often representing count or index' },
            'i': { description: 'Imaginary unit or index variable' },
            'π': { description: 'Pi, mathematical constant (~3.14159)' },
            'e': { description: 'Euler\'s number, mathematical constant (~2.71828)' },
            'θ': { description: 'Theta, often representing angle in radians' },
            'φ': { description: 'Phi, often representing angle or golden ratio' }
        };
        
        return infoMap[variable.toLowerCase()] || infoMap[variable] || {
            description: 'Mathematical variable or symbol'
        };
    }
    
    /**
     * Animate equation solution reveal
     * @param {HTMLElement} solution - The solution element
     */
    function animateEquationSolution(solution) {
        solution.style.opacity = '0';
        solution.style.transform = 'translateY(20px)';
        solution.style.maxHeight = '0';
        solution.style.overflow = 'hidden';
        
        setTimeout(() => {
            solution.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            solution.style.opacity = '1';
            solution.style.transform = 'translateY(0)';
            solution.style.maxHeight = '500px';
        }, 10);
    }
    
    /**
     * Add CSS styles for equation animations
     */
    function addEquationAnimationStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .equation-delay-100 { animation-delay: 0.1s; }
            .equation-delay-200 { animation-delay: 0.2s; }
            .equation-delay-300 { animation-delay: 0.3s; }
            .equation-delay-400 { animation-delay: 0.4s; }
            
            @keyframes equationGlow {
                0%, 100% { 
                    box-shadow: 0 0 10px rgba(222, 231, 119, 0.2); 
                }
                50% { 
                    box-shadow: 0 0 20px rgba(222, 231, 119, 0.4); 
                }
            }
            
            .equation-widget {
                animation: equationGlow 3s infinite;
            }
        `;
        document.head.appendChild(style);
    }
    
    /**
     * Knowledge Graph System
     * Creates interactive knowledge graph with animated connections
     */
    function initKnowledgeGraphSystem() {
        const knowledgeGraphs = document.querySelectorAll('.knowledge-graph-widget:not([data-vis-network])');
        
        knowledgeGraphs.forEach((graph, index) => {
            setTimeout(() => {
                createKnowledgeGraph(graph);
            }, index * 500);
        });
    }
    
    /**
     * Create an interactive knowledge graph
     * @param {HTMLElement} container - The container element
     */
    function createKnowledgeGraph(container) {
        // Clear placeholder content
        container.innerHTML = '';
        
        // Define mathematical concepts and their connections
        const concepts = [
            { id: 'algebra', name: 'Algebra', x: 30, y: 30, color: '#dee777' },
            { id: 'geometry', name: 'Geometry', x: 70, y: 30, color: '#b7bb7e' },
            { id: 'calculus', name: 'Calculus', x: 50, y: 50, color: '#2e3105' },
            { id: 'statistics', name: 'Statistics', x: 30, y: 70, color: '#fffcc0' },
            { id: 'logic', name: 'Logic', x: 70, y: 70, color: '#5a5d3a' }
        ];
        
        const connections = [
            { from: 'algebra', to: 'calculus' },
            { from: 'geometry', to: 'calculus' },
            { from: 'calculus', to: 'statistics' },
            { from: 'calculus', to: 'logic' },
            { from: 'algebra', to: 'geometry' },
            { from: 'statistics', to: 'logic' }
        ];
        
        // Create connections first (so they appear behind nodes)
        connections.forEach(connection => {
            createConnection(container, connection, concepts);
        });
        
        // Create concept nodes
        concepts.forEach(concept => {
            createConceptNode(container, concept);
        });
        
        // Add animation to connections
        animateConnections(container);
    }
    
    /**
     * Create a concept node in the knowledge graph
     * @param {HTMLElement} container - The container element
     * @param {Object} concept - Concept configuration
     */
    function createConceptNode(container, concept) {
        const node = document.createElement('div');
        node.className = 'knowledge-node';
        node.id = `node-${concept.id}`;
        node.textContent = concept.name;
        node.style.cssText = `
            position: absolute;
            left: ${concept.x}%;
            top: ${concept.y}%;
            transform: translate(-50%, -50%);
            width: 100px;
            height: 100px;
            background: ${concept.color};
            color: ${concept.id === 'calculus' ? 'white' : 'var(--color-academic-secondary)'};
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
            box-shadow: var(--academic-shadow-md);
            transition: all 0.3s ease;
            z-index: 10;
            opacity: 0;
            transform: translate(-50%, -50%) scale(0);
        `;
        
        // Add hover effects
        node.addEventListener('mouseenter', function() {
            this.style.transform = 'translate(-50%, -50%) scale(1.2)';
            this.style.boxShadow = 'var(--academic-shadow-lg)';
            highlightRelatedConnections(this.id);
        });
        
        node.addEventListener('mouseleave', function() {
            this.style.transform = 'translate(-50%, -50%) scale(1)';
            this.style.boxShadow = 'var(--academic-shadow-md)';
            resetConnections();
        });
        
        // Add click interaction
        node.addEventListener('click', function() {
            showConceptDetails(concept);
        });
        
        container.appendChild(node);
        
        // Animate node appearance
        setTimeout(() => {
            node.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            node.style.opacity = '1';
            node.style.transform = 'translate(-50%, -50%) scale(1)';
        }, 100);
    }
    
    /**
     * Create a connection between concepts
     * @param {HTMLElement} container - The container element
     * @param {Object} connection - Connection configuration
     * @param {Array} concepts - Array of concept objects
     */
    function createConnection(container, connection, concepts) {
        const fromConcept = concepts.find(c => c.id === connection.from);
        const toConcept = concepts.find(c => c.id === connection.to);
        
        if (!fromConcept || !toConcept) return;
        
        const connectionEl = document.createElement('div');
        connectionEl.className = 'knowledge-connection';
        connectionEl.dataset.from = connection.from;
        connectionEl.dataset.to = connection.to;
        
        container.appendChild(connectionEl);
        
        // Position connection (will be updated by animation)
        updateConnectionPosition(connectionEl, fromConcept, toConcept);
    }
    
    /**
     * Update connection position
     * @param {HTMLElement} connection - Connection element
     * @param {Object} fromConcept - From concept
     * @param {Object} toConcept - To concept
     */
    function updateConnectionPosition(connection, fromConcept, toConcept) {
        const container = connection.parentElement;
        const containerRect = container.getBoundingClientRect();
        
        const fromX = (fromConcept.x / 100) * containerRect.width;
        const fromY = (fromConcept.y / 100) * containerRect.height;
        const toX = (toConcept.x / 100) * containerRect.width;
        const toY = (toConcept.y / 100) * containerRect.height;
        
        const dx = toX - fromX;
        const dy = toY - fromY;
        const length = Math.sqrt(dx * dx + dy * dy);
        const angle = Math.atan2(dy, dx) * 180 / Math.PI;
        
        connection.style.cssText = `
            position: absolute;
            left: ${fromX}px;
            top: ${fromY}px;
            width: ${length}px;
            height: 3px;
            background: linear-gradient(90deg, 
                var(--color-academic-primary), 
                var(--color-academic-dark));
            transform: rotate(${angle}deg);
            transform-origin: 0 0;
            opacity: 0.3;
            z-index: 1;
        `;
    }
    
    /**
     * Animate connections in the knowledge graph
     * @param {HTMLElement} container - The container element
     */
    function animateConnections(container) {
        const connections = container.querySelectorAll('.knowledge-connection');
        
        connections.forEach((connection, index) => {
            setTimeout(() => {
                connection.style.transition = 'all 0.5s ease';
                connection.style.opacity = '0.5';
                
                // Add flowing animation
                connection.style.background = `
                    linear-gradient(90deg, 
                        transparent, 
                        var(--color-academic-primary), 
                        transparent)
                `;
                connection.style.backgroundSize = '200% 100%';
                connection.style.animation = `flowAnimation 2s linear infinite`;
                connection.style.animationDelay = `${index * 0.3}s`;
            }, index * 200);
        });
        
        // Add flow animation CSS
        if (!document.querySelector('#flow-animation')) {
            const style = document.createElement('style');
            style.id = 'flow-animation';
            style.textContent = `
                @keyframes flowAnimation {
                    0% { background-position: -200% 0; }
                    100% { background-position: 200% 0; }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    /**
     * Highlight connections related to a node
     * @param {string} nodeId - The node ID
     */
    function highlightRelatedConnections(nodeId) {
        const connections = document.querySelectorAll('.knowledge-connection');
        const conceptId = nodeId.replace('node-', '');
        
        connections.forEach(connection => {
            if (connection.dataset.from === conceptId || connection.dataset.to === conceptId) {
                connection.style.opacity = '1';
                connection.style.height = '5px';
                connection.style.background = 'var(--color-academic-primary)';
            }
        });
    }
    
    /**
     * Reset all connections to default state
     */
    function resetConnections() {
        const connections = document.querySelectorAll('.knowledge-connection');
        connections.forEach(connection => {
            connection.style.opacity = '0.5';
            connection.style.height = '3px';
            connection.style.background = `
                linear-gradient(90deg, 
                    transparent, 
                    var(--color-academic-primary), 
                    transparent)
            `;
        });
    }
    
    /**
     * Show detailed information about a concept
     * @param {Object} concept - The concept object
     */
    function showConceptDetails(concept) {
        const details = getConceptDetails(concept.id);
        const modal = createConceptModal(concept, details);
        document.body.appendChild(modal);
        
        // Show modal
        setTimeout(() => {
            modal.style.opacity = '1';
            modal.style.transform = 'translate(-50%, -50%) scale(1)';
        }, 10);
    }
    
    /**
     * Get detailed information about a concept
     * @param {string} conceptId - The concept ID
     * @returns {Object} - Concept details
     */
    function getConceptDetails(conceptId) {
        const detailsMap = {
            'algebra': {
                title: 'Algebra',
                description: 'The study of mathematical symbols and the rules for manipulating these symbols.',
                applications: 'Physics, Engineering, Computer Science',
                keyConcepts: 'Equations, Polynomials, Matrices, Groups'
            },
            'geometry': {
                title: 'Geometry',
                description: 'The branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.',
                applications: 'Architecture, Computer Graphics, Physics',
                keyConcepts: 'Shapes, Angles, Dimensions, Transformations'
            },
            'calculus': {
                title: 'Calculus',
                description: 'The mathematical study of continuous change, in the same way that geometry is the study of shape.',
                applications: 'Physics, Economics, Engineering, Biology',
                keyConcepts: 'Derivatives, Integrals, Limits, Differential Equations'
            },
            'statistics': {
                title: 'Statistics',
                description: 'The discipline that concerns the collection, organization, analysis, interpretation, and presentation of data.',
                applications: 'Data Science, Economics, Medicine, Social Sciences',
                keyConcepts: 'Probability, Distributions, Hypothesis Testing, Regression'
            },
            'logic': {
                title: 'Logic',
                description: 'The study of correct reasoning, especially as it involves the drawing of inferences.',
                applications: 'Computer Science, Philosophy, Mathematics',
                keyConcepts: 'Propositional Logic, Predicate Logic, Proof Theory, Set Theory'
            }
        };
        
        return detailsMap[conceptId] || {
            title: conceptId,
            description: 'Mathematical concept',
            applications: 'Various fields',
            keyConcepts: 'Core principles'
        };
    }
    
    /**
     * Create a modal for concept details
     * @param {Object} concept - The concept object
     * @param {Object} details - Concept details
     * @returns {HTMLElement} - The modal element
     */
    function createConceptModal(concept, details) {
        const modal = document.createElement('div');
        modal.className = 'concept-modal';
        modal.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0.8);
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: var(--academic-shadow-lg);
            z-index: 1000;
            max-width: 500px;
            width: 90%;
            opacity: 0;
            transition: all 0.3s ease;
        `;
        
        modal.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <h3 style="color: var(--color-academic-secondary); margin: 0;">${details.title}</h3>
                <button class="close-modal" style="
                    background: none;
                    border: none;
                    font-size: 1.5rem;
                    cursor: pointer;
                    color: var(--color-academic-text-light);
                ">×</button>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <p>${details.description}</p>
            </div>
            
            <div style="background: var(--color-academic-light); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <strong>Applications:</strong> ${details.applications}
            </div>
            
            <div style="background: rgba(222, 231, 119, 0.1); padding: 1rem; border-radius: 8px;">
                <strong>Key Concepts:</strong> ${details.keyConcepts}
            </div>
            
            <div style="margin-top: 1.5rem; text-align: center;">
                <a href="/${concept.id}/" class="academic-button academic-button-primary" style="margin-right: 1rem; text-decoration: none;">
                    <i class="fas fa-book"></i> Learn More
                </a>
                <a href="/${concept.id}/#examples" class="academic-button academic-button-secondary" style="text-decoration: none;">
                    <i class="fas fa-play"></i> Examples
                </a>
            </div>
        `;
        
        // Add close functionality
        modal.querySelector('.close-modal').addEventListener('click', function() {
            modal.style.opacity = '0';
            modal.style.transform = 'translate(-50%, -50%) scale(0.8)';
            setTimeout(() => modal.remove(), 300);
        });
        
        // Close on background click
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.querySelector('.close-modal').click();
            }
        });
        
        return modal;
    }
    
    /**
     * Quiz Intelligence System
     * Handles quiz interactions, scoring, and adaptive feedback
     */
    function initQuizIntelligence() {
        const quizOptions = document.querySelectorAll('.quiz-option');
        const quizFeedback = document.querySelector('.quiz-feedback');
        
        quizOptions.forEach(option => {
            option.addEventListener('click', function() {
                handleQuizSelection(this, quizFeedback);
            });
        });
        
        // Add quiz timer
        addQuizTimer();
    }
    
    /**
     * Handle quiz option selection
     * @param {HTMLElement} selectedOption - The selected option
     * @param {HTMLElement} feedback - Feedback element
     */
    function handleQuizSelection(selectedOption, feedback) {
        // Clear previous selections
        const allOptions = selectedOption.parentElement.querySelectorAll('.quiz-option');
        allOptions.forEach(opt => {
            opt.classList.remove('selected');
            opt.style.transform = '';
        });
        
        // Select current option
        selectedOption.classList.add('selected');
        selectedOption.style.transform = 'scale(1.05)';
        
        // Check if correct
        const isCorrect = selectedOption.dataset.correct === 'true';
        
        // Show feedback
        if (feedback) {
            showQuizFeedback(feedback, isCorrect, selectedOption.textContent);
        }
        
        // Update quiz progress
        updateQuizProgress();
        
        // Add celebration for correct answer
        if (isCorrect) {
            celebrateCorrectAnswer(selectedOption);
        }
    }
    
    /**
     * Show quiz feedback with intelligent messages
     * @param {HTMLElement} feedback - Feedback element
     * @param {boolean} isCorrect - Whether answer is correct
     * @param {string} selectedText - Selected option text
     */
    function showQuizFeedback(feedback, isCorrect, selectedText) {
        feedback.className = isCorrect ? 'quiz-feedback correct' : 'quiz-feedback incorrect';
        
        const feedbackMessages = {
            correct: [
                'Excellent! Perfect understanding.',
                'Brilliant! You mastered this concept.',
                'Outstanding! Your reasoning is impeccable.',
                'Perfect! Mathematical intuition on point.'
            ],
            incorrect: [
                'Good attempt! Let\'s review the concept.',
                'Interesting approach! Here\'s the correct reasoning...',
                'Close! The correct answer involves different principles.',
                'Good thinking! Let me explain the solution...'
            ]
        };
        
        const messages = isCorrect ? feedbackMessages.correct : feedbackMessages.incorrect;
        const randomMessage = messages[Math.floor(Math.random() * messages.length)];
        
        feedback.innerHTML = `
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <i class="fas fa-${isCorrect ? 'check-circle' : 'times-circle'}" 
                   style="font-size: 1.2rem; color: ${isCorrect ? 'var(--color-academic-primary)' : '#ff6b6b'}"></i>
                <span>${randomMessage}</span>
            </div>
            ${!isCorrect ? `<div style="font-size: 0.9rem; opacity: 0.8; margin-top: 10px;">
                <strong>Hint:</strong> Review the differentiation rules for polynomial terms.
            </div>` : ''}
        `;
        
        feedback.style.display = 'block';
        
        // Auto-hide feedback after delay
        setTimeout(() => {
            feedback.style.opacity = '0';
            setTimeout(() => {
                feedback.style.display = 'none';
                feedback.style.opacity = '1';
            }, 300);
        }, 5000);
    }
    
    /**
     * Celebrate correct answer with animation
     * @param {HTMLElement} option - The correct option element
     */
    function celebrateCorrectAnswer(option) {
        // Add celebration particles
        for (let i = 0; i < 10; i++) {
            createCelebrationParticle(option);
        }
        
        // Add sound effect (simulated)
        const audio = new Audio('data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAZGF0YQQAAAAAAA==');
        audio.volume = 0.1;
        // audio.play().catch(() => {}); // Silently fail if audio not supported
        
        // Add confetti effect
        addConfettiEffect(option);
    }
    
    /**
     * Create celebration particle
     * @param {HTMLElement} parent - Parent element
     */
    function createCelebrationParticle(parent) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: absolute;
            width: 8px;
            height: 8px;
            background: var(--color-academic-primary);
            border-radius: 50%;
            pointer-events: none;
            z-index: 100;
        `;
        
        const rect = parent.getBoundingClientRect();
        particle.style.left = `${rect.left + rect.width/2}px`;
        particle.style.top = `${rect.top + rect.height/2}px`;
        
        document.body.appendChild(particle);
        
        // Animate particle
        const angle = Math.random() * Math.PI * 2;
        const velocity = 2 + Math.random() * 3;
        const vx = Math.cos(angle) * velocity;
        const vy = Math.sin(angle) * velocity;
        
        let x = rect.left + rect.width/2;
        let y = rect.top + rect.height/2;
        
        function animate() {
            x += vx;
            y += vy;
            particle.style.left = `${x}px`;
            particle.style.top = `${y}px`;
            
            particle.style.opacity = parseFloat(particle.style.opacity || 1) - 0.02;
            
            if (parseFloat(particle.style.opacity) > 0) {
                requestAnimationFrame(animate);
            } else {
                particle.remove();
            }
        }
        
        animate();
    }
    
    /**
     * Add confetti effect
     * @param {HTMLElement} element - Target element
     */
    function addConfettiEffect(element) {
        const confetti = document.createElement('div');
        confetti.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            z-index: 999;
        `;
        
        document.body.appendChild(confetti);
        
        // Create confetti pieces
        for (let i = 0; i < 50; i++) {
            setTimeout(() => {
                createConfettiPiece(confetti);
            }, i * 20);
        }
        
        // Remove confetti after animation
        setTimeout(() => {
            confetti.style.opacity = '0';
            confetti.style.transition = 'opacity 0.5s ease';
            setTimeout(() => confetti.remove(), 500);
        }, 2000);
    }
    
    /**
     * Create a confetti piece
     * @param {HTMLElement} container - Confetti container
     */
    function createConfettiPiece(container) {
        const piece = document.createElement('div');
        const colors = ['#dee777', '#b7bb7e', '#2e3105', '#fffcc0', '#5a5d3a'];
        const color = colors[Math.floor(Math.random() * colors.length)];
        
        piece.style.cssText = `
            position: absolute;
            width: ${Math.random() * 10 + 5}px;
            height: ${Math.random() * 10 + 5}px;
            background: ${color};
            top: -20px;
            left: ${Math.random() * 100}%;
            border-radius: ${Math.random() > 0.5 ? '50%' : '2px'};
            transform: rotate(${Math.random() * 360}deg);
        `;
        
        container.appendChild(piece);
        
        // Animate confetti
        const animation = piece.animate([
            { 
                transform: `translateY(0) rotate(0deg)`,
                opacity: 1 
            },
            { 
                transform: `translateY(${window.innerHeight}px) rotate(${Math.random() * 720}deg)`,
                opacity: 0 
            }
        ], {
            duration: Math.random() * 2000 + 1000,
            easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
        });
        
        animation.onfinish = () => piece.remove();
    }
    
    /**
     * Update quiz progress indicator
     */
    function updateQuizProgress() {
        const quizContainer = document.querySelector('.quiz-widget');
        if (!quizContainer) return;
        
        let progressIndicator = quizContainer.querySelector('.quiz-progress');
        if (!progressIndicator) {
            progressIndicator = document.createElement('div');
            progressIndicator.className = 'quiz-progress';
            progressIndicator.style.cssText = `
                margin-top: 1rem;
                text-align: center;
                font-size: 0.9rem;
                color: var(--color-academic-text-light);
            `;
            quizContainer.appendChild(progressIndicator);
        }
        
        const selectedOptions = quizContainer.querySelectorAll('.quiz-option.selected');
        const totalOptions = quizContainer.querySelectorAll('.quiz-option').length;
        
        progressIndicator.textContent = `Progress: ${selectedOptions.length}/${totalOptions}`;
        
        // Check for quiz completion
        if (selectedOptions.length === totalOptions) {
            showQuizCompletion();
        }
    }
    
    /**
     * Show quiz completion message
     */
    function showQuizCompletion() {
        const quizContainer = document.querySelector('.quiz-widget');
        if (!quizContainer) return;
        
        let completionMessage = quizContainer.querySelector('.quiz-completion');
        if (!completionMessage) {
            completionMessage = document.createElement('div');
            completionMessage.className = 'quiz-completion';
            completionMessage.style.cssText = `
                margin-top: 1.5rem;
                padding: 1.5rem;
                background: linear-gradient(135deg, var(--color-academic-primary), var(--color-academic-light));
                color: var(--color-academic-secondary);
                border-radius: 12px;
                text-align: center;
                font-weight: bold;
                animation: fadeIn 0.6s ease;
            `;
            
            const correctAnswers = quizContainer.querySelectorAll('.quiz-option.selected[data-correct="true"]').length;
            const totalQuestions = quizContainer.querySelectorAll('.quiz-option').length / 4; // Assuming 4 options per question
            
            completionMessage.innerHTML = `
                <div style="font-size: 2rem; margin-bottom: 1rem;">🎉</div>
                <div style="font-size: 1.2rem; margin-bottom: 0.5rem;">Quiz Completed!</div>
                <div>Score: ${correctAnswers}/${totalQuestions}</div>
                <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.8;">
                    ${getPerformanceMessage(correctAnswers / totalQuestions)}
                </div>
            `;
            
            quizContainer.appendChild(completionMessage);
            
            // Add retry button
            const retryButton = document.createElement('button');
            retryButton.className = 'academic-button academic-button-primary';
            retryButton.style.marginTop = '1rem';
            retryButton.innerHTML = '<i class="fas fa-redo"></i> Try Again';
            retryButton.addEventListener('click', resetQuiz);
            
            completionMessage.appendChild(retryButton);
        }
    }
    
    /**
     * Get performance message based on score
     * @param {number} scoreRatio - Score ratio (0-1)
     * @returns {string} - Performance message
     */
    function getPerformanceMessage(scoreRatio) {
        if (scoreRatio >= 0.9) return 'Outstanding performance! Master level achieved.';
        if (scoreRatio >= 0.7) return 'Excellent work! Strong understanding demonstrated.';
        if (scoreRatio >= 0.5) return 'Good job! Solid grasp of concepts.';
        return 'Keep practicing! Review the concepts and try again.';
    }
    
    /**
     * Reset quiz to initial state
     */
    function resetQuiz() {
        const quizContainer = document.querySelector('.quiz-widget');
        if (!quizContainer) return;
        
        // Clear selections
        quizContainer.querySelectorAll('.quiz-option').forEach(option => {
            option.classList.remove('selected');
            option.style.transform = '';
        });
        
        // Hide feedback
        const feedback = quizContainer.querySelector('.quiz-feedback');
        if (feedback) {
            feedback.style.display = 'none';
        }
        
        // Remove progress indicator
        const progress = quizContainer.querySelector('.quiz-progress');
        if (progress) progress.remove();
        
        // Remove completion message
        const completion = quizContainer.querySelector('.quiz-completion');
        if (completion) completion.remove();
        
        // Reset timer
        const timer = quizContainer.querySelector('.quiz-timer');
        if (timer) {
            timer.textContent = 'Time: 5:00';
            timer.style.background = '';
            timer.style.color = '';
            timer.style.animation = '';
        }
    }
    
    /**
     * Add quiz timer
     */
    function addQuizTimer() {
        const quizContainer = document.querySelector('.quiz-widget');
        if (!quizContainer) return;
        
        const timer = document.createElement('div');
        timer.className = 'quiz-timer';
        timer.style.cssText = `
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--color-academic-primary);
            color: var(--color-academic-secondary);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9rem;
        `;
        
        let timeLeft = 300; // 5 minutes in seconds
        updateTimerDisplay(timer, timeLeft);
        
        const timerInterval = setInterval(() => {
            timeLeft--;
            updateTimerDisplay(timer, timeLeft);
            
            if (timeLeft <= 60) {
                timer.style.background = '#ff6b6b';
                timer.style.color = 'white';
                timer.style.animation = 'pulse 1s infinite';
            }
            
            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                timer.textContent = 'Time Expired!';
                autoSubmitQuiz();
            }
        }, 1000);
        
        quizContainer.style.position = 'relative';
        quizContainer.appendChild(timer);
    }
    
    /**
     * Update timer display
     * @param {HTMLElement} timer - Timer element
     * @param {number} seconds - Seconds remaining
     */
    function updateTimerDisplay(timer, seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        timer.textContent = `Time: ${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    }
    
    /**
     * Auto-submit quiz when time expires
     */
    function autoSubmitQuiz() {
        const quizContainer = document.querySelector('.quiz-widget');
        if (!quizContainer) return;
        
        // Select all correct answers (simulated)
        const correctOptions = quizContainer.querySelectorAll('.quiz-option[data-correct="true"]');
        correctOptions.forEach(option => {
            option.classList.add('selected');
        });
        
        // Show feedback
        const feedback = quizContainer.querySelector('.quiz-feedback');
        if (feedback) {
            feedback.className = 'quiz-feedback incorrect';
            feedback.innerHTML = `
                <div style="display: flex; align-items: center; gap: 10px;">
                    <i class="fas fa-clock" style="font-size: 1.2rem; color: #ff6b6b"></i>
                    <span>Time expired! Let's review the correct answers.</span>
                </div>
            `;
            feedback.style.display = 'block';
        }
        
        // Show completion
        setTimeout(() => {
            showQuizCompletion();
        }, 1000);
    }
    
    /**
     * Academic Navigation System
     * Enhanced navigation with smooth scrolling and active state management
     */
    function initAcademicNavigation() {
        const navLinks = document.querySelectorAll('.academic-nav-link');
        const sections = document.querySelectorAll('section[id]');
        
        // Smooth scrolling
        navLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId.startsWith('#')) {
                    e.preventDefault();
                    const targetSection = document.querySelector(targetId);
                    if (targetSection) {
                        smoothScrollTo(targetSection);
                        navLinks.forEach(l => l.classList.remove('active'));
                        this.classList.add('active');
                        history.pushState(null, null, targetId);
                    }
                }
            });
        });
        
        // Update active state on scroll
        window.addEventListener('scroll', throttle(() => {
            updateActiveNavLink(sections, navLinks);
        }, 100));
        
        // Mobile navigation toggle
        const mobileToggle = document.querySelector('.mobile-nav-toggle');
        const navMenu = document.querySelector('.academic-nav-menu');
        
        if (mobileToggle && navMenu) {
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
                this.setAttribute('aria-expanded', navMenu.classList.contains('active'));
                
                // Update icon
                const icon = this.querySelector('i');
                if (icon) {
                    icon.className = navMenu.classList.contains('active') ? 
                        'fas fa-times' : 'fas fa-bars';
                }
            });
        }
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (navMenu && navMenu.classList.contains('active') && 
                !e.target.closest('.academic-nav-menu') && 
                !e.target.closest('.mobile-nav-toggle')) {
                navMenu.classList.remove('active');
                if (mobileToggle) {
                    mobileToggle.setAttribute('aria-expanded', 'false');
                    const icon = mobileToggle.querySelector('i');
                    if (icon) icon.className = 'fas fa-bars';
                }
            }
        });
    }
    
    /**
     * Smooth scroll to element
     * @param {HTMLElement} element - Target element
     */
    function smoothScrollTo(element) {
        const headerHeight = document.querySelector('.academic-nav-widget')?.offsetHeight || 80;
        const targetPosition = element.offsetTop - headerHeight;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        const duration = 800;
        let start = null;
        
        function animation(currentTime) {
            if (start === null) start = currentTime;
            const timeElapsed = currentTime - start;
            const progress = Math.min(timeElapsed / duration, 1);
            
            // Easing function
            const ease = progress < 0.5 ? 
                2 * progress * progress : 
                -1 + (4 - 2 * progress) * progress;
            
            window.scrollTo(0, startPosition + distance * ease);
            
            if (timeElapsed < duration) {
                requestAnimationFrame(animation);
            }
        }
        
        requestAnimationFrame(animation);
    }
    
    /**
     * Update active navigation link based on scroll position
     * @param {NodeList} sections - Page sections
     * @param {NodeList} navLinks - Navigation links
     */
    function updateActiveNavLink(sections, navLinks) {
        let currentSection = '';
        const scrollPosition = window.pageYOffset + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSection = section.id;
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    }
    
    /**
     * Scroll-based Animations System
     * Animate elements when they come into view
     */
    function initScrollBasedAnimations() {
        const animatedElements = document.querySelectorAll(
            '.academic-fade-in-up, .theorem-widget, .example-widget, .equation-widget'
        );
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Add staggered animation delay
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        
                        // Add specific animations based on element type
                        if (entry.target.classList.contains('theorem-widget')) {
                            entry.target.style.animation = 'theoremReveal 0.8s ease';
                        } else if (entry.target.classList.contains('equation-widget')) {
                            entry.target.style.animation = 'equationGlow 2s ease';
                        }
                        
                        // Stop observing after animation
                        observer.unobserve(entry.target);
                    }, index * 100);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        });
        
        // Set initial state and start observing
        animatedElements.forEach((element, index) => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            observer.observe(element);
        });
    }
    
    /**
     * Throttle function for performance optimization
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
    
    // Add global CSS for animations
    const globalStyles = document.createElement('style');
    globalStyles.textContent = `
        /* Navigation active state */
        .academic-nav-link.active {
            color: var(--color-academic-secondary) !important;
            font-weight: 700 !important;
        }
        
        .academic-nav-link.active::after {
            width: 100% !important;
        }
        
        /* Mobile navigation */
        @media (max-width: 768px) {
        }
        
        /* Quiz feedback animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        
        .quiz-feedback {
            animation: fadeIn 0.3s ease;
        }
    `;
    document.head.appendChild(globalStyles);
    
    // Public API for external integration
    window.IntelligentAcademicWidgets = {
        // Theorem System
        showProof: function(theoremId) {
            const theorem = document.getElementById(theoremId);
            if (theorem) {
                const toggle = theorem.querySelector('.theorem-proof-toggle');
                if (toggle) toggle.click();
            }
        },
        
        hideAllProofs: function() {
            document.querySelectorAll('.proof-widget.active').forEach(proof => {
                proof.classList.remove('active');
            });
            document.querySelectorAll('.theorem-proof-toggle').forEach(toggle => {
                const icon = toggle.querySelector('i') || toggle.querySelector('span:last-child');
                if (icon) {
                    if (icon.tagName === 'I') {
                        icon.className = 'fas fa-chevron-right';
                    } else {
                        icon.textContent = '▶';
                    }
                }
                const text = toggle.querySelector('span:first-child');
                if (text) text.textContent = 'Show Proof';
            });
        },
        
        // Equation System
        solveEquation: function(equationId) {
            const equation = document.getElementById(equationId);
            if (equation) {
                const solution = equation.querySelector('.equation-solution');
                if (solution) {
                    solution.classList.add('active');
                    animateEquationSolution(solution);
                    return true;
                }
            }
            return false;
        },
        
        // Quiz System
        startQuiz: function() {
            resetQuiz();
            const timer = document.querySelector('.quiz-timer');
            if (timer) {
                timer.textContent = 'Time: 5:00';
                timer.style.background = 'var(--color-academic-primary)';
                timer.style.color = 'var(--color-academic-secondary)';
                timer.style.animation = '';
            }
            return 'Quiz started';
        },
        
        submitQuiz: function() {
            const correctOptions = document.querySelectorAll('.quiz-option[data-correct="true"]');
            correctOptions.forEach(option => {
                option.classList.add('selected');
            });
            showQuizCompletion();
            return 'Quiz submitted';
        },
        
        // Knowledge Graph
        highlightConcept: function(conceptId) {
            const node = document.getElementById(`node-${conceptId}`);
            if (node) {
                node.style.transform = 'translate(-50%, -50%) scale(1.3)';
                node.style.boxShadow = '0 0 30px rgba(222, 231, 119, 0.5)';
                highlightRelatedConnections(`node-${conceptId}`);
                
                setTimeout(() => {
                    node.style.transform = 'translate(-50%, -50%) scale(1)';
                    node.style.boxShadow = 'var(--academic-shadow-md)';
                    resetConnections();
                }, 2000);
            }
        },
        
        // Utility Functions
        scrollToSection: function(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) smoothScrollTo(section);
        },
        
        toggleMobileMenu: function() {
            const toggle = document.querySelector('.mobile-nav-toggle');
            if (toggle) toggle.click();
        }
    };
    
    // Initialize on window load
    window.addEventListener('load', function() {
        // Re-initialize MathJax if needed
        if (window.MathJax) {
            MathJax.typeset();
        }
        
        // Add loading animation removal
        document.body.classList.add('loaded');
        
        // Log initialization
        console.log('SkytrailGroup Mathematics Academy fully loaded');
    });
    
})();


// Fallback for slow/failed remote images (3s timeout)
(function () {
  const FALLBACKS = [
    'https://i.postimg.cc/VNXg2MBn/image-search-w1728-h1080-shu-xue-ke-shi-hua-ji-he-tu-xing-dai-shu-gong-shi.jpg',
    'https://i.postimg.cc/k5WsL8Fb/image-search-w4330-h3464-shu-xue-jiao-xue-tu-biao-gong-shi-shi-jue-hua.jpg',
    'https://i.postimg.cc/Zq6HX3FP/image-search-w5000-h4160-shu-xue-ke-shi-hua-ji-he-tu-xing-dai-shu-gong-shi.jpg',
    'https://i.postimg.cc/KYtfCLrL/image-search-w5196-h2887-shu-xue-jiao-xue-tu-biao-gong-shi-shi-jue-hua.jpg',
  ];
  let idx = 0;
  function fallback(img) {
    img._fallback = true;
    img.src = FALLBACKS[idx++ % FALLBACKS.length];
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('img[src*="picsum.photos"]').forEach(function (img) {
      const t = setTimeout(function () {
        if (!img.complete || img.naturalWidth === 0) fallback(img);
      }, 3000);
      img.addEventListener('load', function () { clearTimeout(t); });
      img.addEventListener('error', function () { clearTimeout(t); if (!img._fallback) fallback(img); });
    });
  });
})();
