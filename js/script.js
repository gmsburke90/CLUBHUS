/* CLUBHUS — landing interactions */
(function () {
  'use strict';

  /* Sticky nav state */
  var nav = document.getElementById('nav');
  var onScroll = function () {
    if (window.scrollY > 24) nav.classList.add('is-stuck');
    else nav.classList.remove('is-stuck');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile menu */
  var burger = document.getElementById('burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('.nav__links a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* Scroll reveal */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* Subtle can parallax on pointer move (desktop, motion-allowed) */
  var can = document.getElementById('heroCan');
  var allowMotion = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (can && allowMotion && window.matchMedia('(pointer:fine)').matches) {
    window.addEventListener('mousemove', function (ev) {
      var x = (ev.clientX / window.innerWidth - 0.5) * 14;
      var y = (ev.clientY / window.innerHeight - 0.5) * 10;
      can.style.transform = 'translate(' + x + 'px,' + y + 'px) rotate(' + (x * 0.15) + 'deg)';
    }, { passive: true });
  }

  /* Form (front-end only for now) */
  var form = document.getElementById('joinForm');
  var note = document.getElementById('formNote');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('#email');
      var name = form.querySelector('#name');
      if (!name.value.trim() || !email.checkValidity()) {
        note.textContent = 'Please add your name and a valid email.';
        note.classList.remove('is-success');
        (name.value.trim() ? email : name).focus();
        return;
      }
      note.textContent = 'Thank you — your place is reserved. We’ll be in touch.';
      note.classList.add('is-success');
      form.querySelector('button[type="submit"]').textContent = 'Request Sent';
      form.querySelectorAll('input').forEach(function (i) { i.disabled = true; });
    });
  }

  /* Footer year */
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();
})();
