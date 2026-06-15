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

  var allowMotion = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Scroll progress bar */
  var bar = document.getElementById('progress');
  if (bar) {
    var setProgress = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    window.addEventListener('scroll', setProgress, { passive: true });
    window.addEventListener('resize', setProgress, { passive: true });
    setProgress();
  }

  /* Animated count-up for stats */
  var counts = document.querySelectorAll('[data-count]');
  var runCount = function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var decimals = (el.getAttribute('data-count').split('.')[1] || '').length;
    if (!allowMotion) { el.textContent = target.toFixed(decimals) + suffix; return; }
    var start = null, dur = 1400;
    var tick = function (ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counts.forEach(function (el) { co.observe(el); });
  } else {
    counts.forEach(runCount);
  }

  /* Form (front-end only for now) */
  var form = document.getElementById('joinForm');
  var note = document.getElementById('formNote');
  if (form) {
    var setError = function (field, on) {
      field.classList.toggle('is-error', on);
      field.setAttribute('aria-invalid', on ? 'true' : 'false');
    };
    /* clear a field's error the moment the user corrects it */
    form.querySelectorAll('input').forEach(function (input) {
      input.addEventListener('input', function () {
        if (input.classList.contains('is-error')) setError(input, false);
      });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('#email');
      var name = form.querySelector('#name');
      var nameBad = !name.value.trim();
      var emailBad = !email.checkValidity();
      setError(name, nameBad);
      setError(email, emailBad);
      if (nameBad || emailBad) {
        note.textContent = nameBad
          ? 'Please add your name so we know who to welcome.'
          : 'That email doesn’t look right — mind checking it?';
        note.classList.remove('is-success');
        (nameBad ? name : email).focus();
        return;
      }
      note.textContent = 'Thank you — your place is reserved. We’ll be in touch.';
      note.classList.add('is-success');
      form.querySelector('button[type="submit"]').textContent = 'Request Sent ✓';
      form.querySelectorAll('input').forEach(function (i) { i.disabled = true; });
    });
  }

  /* Footer year */
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();
})();
