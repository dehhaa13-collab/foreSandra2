/* ============================================================
   SCRIPT — Комплексная упаковка активов
   IntersectionObserver, Scroll Progress, Split-Text, Dot Nav
   ============================================================ */

(function () {
    'use strict';

    // ---- Check for reduced motion preference ----
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ============================================================
    // 1. SPLIT-TEXT REVEAL — Разделяем заголовки на слова
    // ============================================================
    function initSplitText() {
        const elements = document.querySelectorAll('.split-text');

        elements.forEach(el => {
            const text = el.textContent;
            el.textContent = '';
            el.setAttribute('aria-label', text);

            const words = text.split(/\s+/);
            words.forEach((word, i) => {
                const wordSpan = document.createElement('span');
                wordSpan.classList.add('word');

                const innerSpan = document.createElement('span');
                innerSpan.classList.add('word-inner');
                innerSpan.textContent = word;
                innerSpan.style.transitionDelay = prefersReducedMotion ? '0ms' : `${i * 0.04}s`;

                wordSpan.appendChild(innerSpan);
                el.appendChild(wordSpan);

                // Add a space after each word (except last)
                if (i < words.length - 1) {
                    el.appendChild(document.createTextNode('\u00A0'));
                }
            });
        });
    }

    // ============================================================
    // 2. INTERSECTION OBSERVER — Reveal on scroll
    // ============================================================
    function initScrollReveal() {
        const revealElements = document.querySelectorAll('.reveal-up, .split-text');
        const staggerElements = document.querySelectorAll('.stagger');

        const isMobile = window.matchMedia('(max-width: 768px)').matches;
        
        const observerOptions = {
            root: null,
            threshold: isMobile ? 0.05 : 0.15,
            rootMargin: isMobile ? '0px 0px 0px 0px' : '0px 0px -50px 0px'
        };

        // Observer for simple reveal-up elements and split-text
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        revealElements.forEach(el => revealObserver.observe(el));

        // Observer for stagger elements (cascading delay)
        const staggerObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Find index among siblings with .stagger class
                    const parent = entry.target.closest('ul, .metric-category, .detail-block, .results-block');
                    if (parent) {
                        const siblings = parent.querySelectorAll('.stagger');
                        const index = Array.from(siblings).indexOf(entry.target);
                        if (!prefersReducedMotion) {
                            entry.target.style.transitionDelay = `${index * 0.06}s`;
                        }
                    }
                    entry.target.classList.add('is-visible');
                    staggerObserver.unobserve(entry.target);
                }
            });
        }, { ...observerOptions, threshold: 0.05 });

        staggerElements.forEach(el => staggerObserver.observe(el));
    }


    // ============================================================
    // 4. DOT NAVIGATION
    // ============================================================
    function initDotNav() {
        const dots = document.querySelectorAll('.dot-nav__dot');
        const slides = document.querySelectorAll('.slide');

        if (!dots.length || !slides.length) return;

        // Click handler — smooth scroll to slide
        dots.forEach(dot => {
            dot.addEventListener('click', () => {
                const slideIndex = parseInt(dot.dataset.slide, 10);
                const target = slides[slideIndex];
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Active dot tracking via IntersectionObserver
        const slideObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const index = Array.from(slides).indexOf(entry.target);
                    dots.forEach((d, i) => {
                        d.classList.toggle('is-active', i === index);
                    });
                }
            });
        }, {
            root: null,
            threshold: 0.4
        });

        slides.forEach(slide => slideObserver.observe(slide));
    }




    // ============================================================
    // 5. SCROLL ORB (Светящийся золотой кружок)
    // ============================================================
    function initScrollOrb() {
        const orb = document.getElementById('scroll-orb');
        if (!orb) return;
        
        // Находим все акцентные места (главный заголовок и заголовки секций)
        const headings = document.querySelectorAll('.hero__title, .section-title');
        if (headings.length === 0) return;

        let activeHeading = null;
        let moveTimeout = null;

        function updateOrbPosition() {
            // Находим заголовок, который ближе всего к центру экрана
            const viewportCenter = window.innerHeight / 2;
            let closestHeading = null;
            let minDistance = Infinity;

            headings.forEach(heading => {
                const rect = heading.getBoundingClientRect();
                const headingCenter = rect.top + rect.height / 2;
                
                // Проверяем, виден ли вообще элемент (с запасом)
                if (rect.top < window.innerHeight + 200 && rect.bottom > -200) {
                    const distance = Math.abs(viewportCenter - headingCenter);
                    if (distance < minDistance) {
                        minDistance = distance;
                        closestHeading = heading;
                    }
                }
            });

            // Если не нашли ничего в центре, берем первый заголовок
            if (!closestHeading) {
                closestHeading = headings[0];
            }

            // Вычисляем абсолютную позицию (с учетом скролла)
            const rect = closestHeading.getBoundingClientRect();
            const absoluteY = window.scrollY + rect.top;
            const absoluteX = window.scrollX + rect.left;
            
            // Шарик прячется прямо внутри текста
            let orbX = absoluteX + 20;
            // Центрируем шарик по вертикали (размер 80px => вычитаем 40)
            let orbY = absoluteY + rect.height / 2 - 40;
            
            orb.style.setProperty('--orb-x', `${orbX}px`);
            orb.style.setProperty('--orb-y', `${orbY}px`);

            if (activeHeading !== closestHeading) {
                if (activeHeading) {
                    activeHeading.classList.remove('title-glow-active');
                }
                activeHeading = closestHeading;
                activeHeading.classList.add('title-glow-active');
                
                // Показываем шарик во время перелета
                orb.classList.add('is-moving');
                clearTimeout(moveTimeout);
                
                // Прячем шарик, когда он долетел (через время транзиции)
                moveTimeout = setTimeout(() => {
                    orb.classList.remove('is-moving');
                }, 1200);
            }
        }

        // Обновляем при скролле и ресайзе
        window.addEventListener('scroll', () => {
            requestAnimationFrame(updateOrbPosition);
        }, { passive: true });
        
        window.addEventListener('resize', () => {
            requestAnimationFrame(updateOrbPosition);
        }, { passive: true });

        // Инициализация первой позиции с небольшой задержкой (чтобы шрифты успели загрузиться)
        setTimeout(() => {
            requestAnimationFrame(updateOrbPosition);
        }, 500);
    }

    // ============================================================
    // INIT — Run everything on DOM ready
    // ============================================================
    function init() {
        initSplitText();

        // If IntersectionObserver is not supported, show everything
        if (!('IntersectionObserver' in window)) {
            document.querySelectorAll('.reveal-up, .stagger').forEach(el => {
                el.classList.add('is-visible');
            });
            document.querySelectorAll('.split-text').forEach(el => {
                el.classList.add('is-visible');
            });
            return;
        }

        initScrollReveal();
        initScrollOrb();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
