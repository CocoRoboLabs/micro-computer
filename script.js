// Intersection Observer for reveal animations
(function () {
    var els = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {
        els.forEach(function (el) { el.classList.add('visible'); });
        return;
    }
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { observer.observe(el); });
})();

// Video play/pause on thumbnail click
document.querySelectorAll('.demo-media').forEach(function (media) {
    var video = media.querySelector('video');
    var thumb = media.querySelector('.demo-thumbnail');
    var btn = media.querySelector('.demo-play-btn');
    if (!video || !btn) return;

    function playVideo() {
        video.play();
        if (thumb) thumb.classList.add('hidden');
        btn.classList.add('hidden');
    }

    function pauseVideo() {
        video.pause();
        if (thumb) thumb.classList.remove('hidden');
        btn.classList.remove('hidden');
    }

    btn.addEventListener('click', playVideo);
    if (thumb) thumb.addEventListener('click', playVideo);

    video.addEventListener('click', function () {
        if (video.paused) {
            playVideo();
        } else {
            pauseVideo();
        }
    });
});

// Smooth nav background on scroll
var nav = document.querySelector('nav');
window.addEventListener('scroll', function () {
    if (window.scrollY > 60) {
        nav.style.background = 'oklch(94% 0.012 70 / 0.95)';
    } else {
        nav.style.background = 'oklch(94% 0.012 70 / 0.88)';
    }
}, { passive: true });

// Mobile hamburger menu
(function () {
    var burger = document.querySelector('.nav-burger');
    var overlay = document.querySelector('.nav-overlay');
    if (!burger || !overlay) return;

    function toggleMenu() {
        var isOpen = burger.classList.toggle('active');
        overlay.classList.toggle('open');
        burger.setAttribute('aria-expanded', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
    }

    function closeMenu() {
        burger.classList.remove('active');
        overlay.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    burger.addEventListener('click', toggleMenu);

    overlay.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && overlay.classList.contains('open')) {
            closeMenu();
        }
    });
})();
