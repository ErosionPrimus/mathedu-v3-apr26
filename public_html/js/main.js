/**
 * Math Encyclopedia - Main JavaScript
 * Category filtering, search, and mobile navigation
 */

(function() {
  'use strict';

  // DOM Elements
  const categoryTags = document.querySelectorAll('.category-tag');
  const topicCards = document.querySelectorAll('.topic-card');
  const searchInput = document.getElementById('search-input');
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const currentCategoryDisplay = document.getElementById('current-category');

  // State
  let currentFilter = 'all';

  /**
   * Initialize the application
   */
  function init() {
    bindEvents();
    updateActiveCategory('all');
  }

  /**
   * Bind all event listeners
   */
  function bindEvents() {
    // Category filter tags
    categoryTags.forEach(tag => {
      tag.addEventListener('click', handleCategoryClick);
    });

    // Search input
    if (searchInput) {
      searchInput.addEventListener('input', debounce(handleSearch, 300));
    }

    // Mobile menu toggle
    if (mobileMenuToggle && navLinks) {
      mobileMenuToggle.addEventListener('click', toggleMobileMenu);
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (navLinks && navLinks.classList.contains('active') && 
          !navLinks.contains(e.target) && 
          !mobileMenuToggle.contains(e.target)) {
        closeMobileMenu();
      }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', handleAnchorClick);
    });
  }

  /**
   * Handle category tag click
   */
  function handleCategoryClick(e) {
    e.preventDefault();
    const category = this.dataset.category;
    
    if (category) {
      filterByCategory(category);
      updateActiveCategory(category);
    }
  }

  /**
   * Filter topics by category
   */
  function filterByCategory(category) {
    currentFilter = category;
    
    topicCards.forEach(card => {
      const cardCategory = card.dataset.category;
      
      if (category === 'all' || cardCategory === category) {
        showCard(card);
      } else {
        hideCard(card);
      }
    });

    updateCategoryDisplay(category);
    animateCards();
  }

  /**
   * Show a topic card with animation
   */
  function showCard(card) {
    card.style.display = '';
    card.classList.remove('hidden');
    
    // Small delay for stagger effect
    requestAnimationFrame(() => {
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    });
  }

  /**
   * Hide a topic card
   */
  function hideCard(card) {
    card.style.opacity = '0';
    card.style.transform = 'translateY(10px)';
    
    setTimeout(() => {
      card.classList.add('hidden');
      card.style.display = 'none';
    }, 200);
  }

  /**
   * Update active state of category tags
   */
  function updateActiveCategory(category) {
    categoryTags.forEach(tag => {
      const tagCategory = tag.dataset.category;
      
      if (tagCategory === category) {
        tag.classList.add('active');
        tag.setAttribute('aria-current', 'true');
      } else {
        tag.classList.remove('active');
        tag.removeAttribute('aria-current');
      }
    });
  }

  /**
   * Update category display text
   */
  function updateCategoryDisplay(category) {
    if (currentCategoryDisplay) {
      const categoryName = category === 'all' 
        ? 'All Topics' 
        : category.charAt(0).toUpperCase() + category.slice(1).replace(/-/g, ' ');
      
      currentCategoryDisplay.textContent = categoryName;
    }
  }

  /**
   * Handle search input
   */
  function handleSearch(e) {
    const query = e.target.value.toLowerCase().trim();
    
    if (!query) {
      // Reset to category filter
      filterByCategory(currentFilter);
      return;
    }

    topicCards.forEach(card => {
      const title = card.querySelector('.topic-title')?.textContent.toLowerCase() || '';
      const description = card.querySelector('.topic-description')?.textContent.toLowerCase() || '';
      const category = card.dataset.category?.toLowerCase() || '';
      
      const matches = title.includes(query) || 
                      description.includes(query) || 
                      category.includes(query);
      
      if (matches) {
        showCard(card);
      } else {
        hideCard(card);
      }
    });

    updateCategoryDisplay(`Search: "${query}"`);
  }

  /**
   * Toggle mobile menu
   */
  function toggleMobileMenu() {
    const isActive = navLinks.classList.contains('active');
    
    if (isActive) {
      closeMobileMenu();
    } else {
      openMobileMenu();
    }
  }

  /**
   * Open mobile menu
   */
  function openMobileMenu() {
    navLinks.classList.add('active');
    mobileMenuToggle.setAttribute('aria-expanded', 'true');
    mobileMenuToggle.innerHTML = '<span class="icon">✕</span>';
    document.body.style.overflow = 'hidden';
  }

  /**
   * Close mobile menu
   */
  function closeMobileMenu() {
    navLinks.classList.remove('active');
    mobileMenuToggle.setAttribute('aria-expanded', 'false');
    mobileMenuToggle.innerHTML = '<span class="icon">☰</span>';
    document.body.style.overflow = '';
  }

  /**
   * Handle anchor link clicks
   */
  function handleAnchorClick(e) {
    const targetId = this.getAttribute('href');
    
    if (targetId.startsWith('#')) {
      e.preventDefault();
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
        
        // Update URL without jumping
        history.pushState(null, '', targetId);
      }
    }
  }

  /**
   * Animate cards on page load
   */
  function animateCards() {
    const visibleCards = Array.from(topicCards).filter(card => 
      !card.classList.contains('hidden')
    );
    
    visibleCards.forEach((card, index) => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      
      setTimeout(() => {
        card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      }, index * 50);
    });
  }

  /**
   * Debounce function for performance
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
   * Lazy load images
   */
  function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
      const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            imageObserver.unobserve(img);
          }
        });
      }, {
        rootMargin: '50px'
      });
      
      images.forEach(img => imageObserver.observe(img));
    } else {
      // Fallback for browsers without IntersectionObserver
      images.forEach(img => {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
      });
    }
  }

  /**
   * Copy code to clipboard
   */
  function initCodeCopy() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(block => {
      const button = document.createElement('button');
      button.className = 'copy-button';
      button.textContent = 'Copy';
      button.setAttribute('aria-label', 'Copy code to clipboard');
      
      button.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(block.textContent);
          button.textContent = 'Copied!';
          button.classList.add('copied');
          
          setTimeout(() => {
            button.textContent = 'Copy';
            button.classList.remove('copied');
          }, 2000);
        } catch (err) {
          console.error('Failed to copy:', err);
          button.textContent = 'Failed';
        }
      });
      
      block.parentElement.style.position = 'relative';
      block.parentElement.appendChild(button);
    });
  }

  /**
   * Initialize reading progress indicator
   */
  function initReadingProgress() {
    const progressBar = document.getElementById('reading-progress');
    
    if (progressBar) {
      window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        
        progressBar.style.width = scrollPercent + '%';
      });
    }
  }

  /**
   * Table of contents highlighting
   */
  function initTOC() {
    const tocLinks = document.querySelectorAll('.toc a');
    const sections = document.querySelectorAll('section[id]');
    
    if (tocLinks.length && sections.length) {
      const observerOptions = {
        rootMargin: '-20% 0px -80% 0px'
      };
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.getAttribute('id');
            
            tocLinks.forEach(link => {
              link.classList.remove('active');
              if (link.getAttribute('href') === '#' + id) {
                link.classList.add('active');
              }
            });
          }
        });
      }, observerOptions);
      
      sections.forEach(section => observer.observe(section));
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      init();
      initLazyLoading();
      initCodeCopy();
      initReadingProgress();
      initTOC();
    });
  } else {
    init();
    initLazyLoading();
    initCodeCopy();
    initReadingProgress();
    initTOC();
  }

})();

// Topic-card image quality enhancer with semantic free-image queries and safe fallback
(function () {
  const FALLBACKS = [
    'https://i.postimg.cc/VNXg2MBn/image-search-w1728-h1080-shu-xue-ke-shi-hua-ji-he-tu-xing-dai-shu-gong-shi.jpg',
    'https://i.postimg.cc/k5WsL8Fb/image-search-w4330-h3464-shu-xue-jiao-xue-tu-biao-gong-shi-shi-jue-hua.jpg',
    'https://i.postimg.cc/Zq6HX3FP/image-search-w5000-h4160-shu-xue-ke-shi-hua-ji-he-tu-xing-dai-shu-gong-shi.jpg',
    'https://i.postimg.cc/KYtfCLrL/image-search-w5196-h2887-shu-xue-jiao-xue-tu-biao-gong-shi-shi-jue-hua.jpg'
  ];

  const SEMANTIC_QUERY_MAP = [
    { re: /matrix|determinant|linear algebra/i, query: 'linear-algebra,matrix,mathematics' },
    { re: /vector|space|basis|eigen/i, query: 'vector-space,geometry,mathematics' },
    { re: /polynomial|factor|algebraic/i, query: 'algebra,formula,blackboard' },
    { re: /calculus|derivative|integral|limit/i, query: 'calculus,graph,math' },
    { re: /geometry|triangle|circle|shape/i, query: 'geometry,diagram,mathematics' },
    { re: /probability|statistics|distribution/i, query: 'statistics,data,chart' },
    { re: /prime|number theory|modular/i, query: 'numbers,mathematics,abacus' }
  ];

  let fallbackIndex = 0;

  function hashText(text) {
    let hash = 0;
    for (let i = 0; i < text.length; i += 1) {
      hash = (hash << 5) - hash + text.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  function inferQuery(img) {
    const card = img.closest('.topic-card');
    const title = card?.querySelector('h3')?.textContent || '';
    const alt = img.alt || '';
    const seed = `${title} ${alt}`.trim();
    for (const rule of SEMANTIC_QUERY_MAP) {
      if (rule.re.test(seed)) return rule.query;
    }
    return 'mathematics,education,formula';
  }

  function setFallback(img) {
    if (img._fallback) return;
    img._fallback = true;
    img.src = FALLBACKS[fallbackIndex++ % FALLBACKS.length];
  }

  function maybeUpgradeImage(img) {
    const src = img.getAttribute('src') || '';
    if (!src.includes('picsum.photos')) return;

    const query = inferQuery(img);
    const sig = hashText((img.alt || '') + query) % 1000;
    img.src = `https://source.unsplash.com/640x360/?${encodeURIComponent(query)}&sig=${sig}`;
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.topic-image img, img[src*="picsum.photos"]').forEach(function (img) {
      img.loading = img.loading || 'lazy';
      img.decoding = img.decoding || 'async';
      maybeUpgradeImage(img);

      const timeoutId = setTimeout(function () {
        if (!img.complete || img.naturalWidth === 0) setFallback(img);
      }, 3500);

      img.addEventListener('load', function () {
        clearTimeout(timeoutId);
      });
      img.addEventListener('error', function () {
        clearTimeout(timeoutId);
        setFallback(img);
      });
    });
  });
})();
