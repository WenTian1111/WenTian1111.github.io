---
layout: han-page
permalink: /cv/
title: CV
heading: Curriculum vitae
eyebrow: Academic background
nav: true
nav_order: 4
page_class: hy-cv-page
description: Han YANG · Animal Science, Applied Mathematics, and an emerging research interest in Chinese philosophy.
---

{% assign cv = site.data.cv.cv %}

<div class="hy-cv-top">
  <div>
    <h2>{{ cv.name }}</h2>
    <p>{{ cv.location }} · <a href="mailto:{{ cv.email }}">{{ cv.email }}</a> · <a href="https://github.com/WenTian1111">GitHub</a></p>
    <p>{{ cv.summary }}</p>
  </div>
  <button type="button" class="hy-button hy-button-secondary hy-print-button" onclick="window.print()">Print / save PDF</button>
</div>

<section class="hy-cv-downloads" aria-label="Download academic CV">
  <button type="button" class="hy-cv-download" id="hy-cv-unlock-btn" aria-haspopup="dialog" aria-controls="hy-cv-modal" style="width: 100%; text-align: left; background: var(--hy-surface); border: 1px solid var(--hy-line); font: inherit; cursor: pointer;">
    <span class="hy-label">Academic profile · Encrypted</span>
    <span class="hy-cv-download-title">Academic CV <span style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 1.1rem; color: var(--hy-teal);"><i class="fa-solid fa-lock" style="font-size: 0.9em;"></i> ↗</span></span>
    <span class="hy-cv-download-detail">Research, education & selected achievements (Protected by password)</span>
    <span class="hy-cv-file">Encrypted PDF · Click to unlock</span>
  </button>
</section>

<!-- Password Verification Modal -->
<div id="hy-cv-modal" class="hy-cv-modal-backdrop" style="display: none;" role="dialog" aria-modal="true" aria-labelledby="hy-cv-modal-title">
  <div class="hy-cv-modal-box">
    <div class="hy-cv-modal-header">
      <div style="display: flex; align-items: center; gap: 0.65rem;">
        <span style="display: inline-flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: var(--hy-teal-soft); color: var(--hy-teal); font-size: 1.1rem; flex-shrink: 0;">
          <i class="fa-solid fa-lock"></i>
        </span>
        <div>
          <h3 id="hy-cv-modal-title" style="margin: 0; font-size: 1.25rem; font-family: var(--hy-serif); color: var(--hy-ink);">Access Verification</h3>
          <p style="margin: 0.2rem 0 0; font-size: 0.85rem; color: var(--hy-muted);">Enter password to decrypt and view the full CV.</p>
        </div>
      </div>
      <button type="button" id="hy-cv-modal-close" style="background: none; border: none; font-size: 1.25rem; color: var(--hy-muted); cursor: pointer; padding: 0.25rem; line-height: 1;" aria-label="Close">
        <i class="fa-solid fa-xmark"></i>
      </button>
    </div>

    <form id="hy-cv-form" style="margin-top: 1.25rem;">
      <div style="position: relative; margin-bottom: 0.75rem;">
        <input type="password" id="hy-cv-pwd-input" placeholder="Enter password / 请输入访问口令" required autocomplete="current-password"
          style="width: 100%; box-sizing: border-box; padding: 0.75rem 2.6rem 0.75rem 0.9rem; border-radius: 8px; border: 1px solid var(--hy-line); background: var(--hy-surface); color: var(--hy-ink); font-size: 0.95rem; outline: none; transition: border-color 0.2s;" />
        <button type="button" id="hy-cv-pwd-toggle" style="position: absolute; right: 0.75rem; top: 50%; transform: translateY(-50%); background: none; border: none; color: var(--hy-muted); cursor: pointer; padding: 0.25rem; font-size: 1rem;" aria-label="Toggle password visibility">
          <i class="fa-regular fa-eye" id="hy-cv-pwd-icon"></i>
        </button>
      </div>

      <div id="hy-cv-status-msg" style="display: none; font-size: 0.85rem; margin-bottom: 0.75rem; border-radius: 6px; padding: 0.6rem 0.85rem; line-height: 1.45;"></div>

      <div style="display: flex; gap: 0.75rem; justify-content: flex-end; margin-top: 1.25rem;">
        <button type="button" id="hy-cv-cancel-btn" class="hy-button hy-button-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Cancel</button>
        <button type="submit" id="hy-cv-submit-btn" class="hy-button" style="padding: 0.5rem 1.25rem; font-size: 0.9rem; background: var(--hy-teal); color: #fff; border: none; border-radius: 6px; cursor: pointer; font-weight: 500;">
          Unlock &amp; View
        </button>
      </div>
    </form>
  </div>
</div>

<nav class="hy-section-nav" aria-label="CV sections">
  <a href="#education">Education</a><a href="#projects">Research</a><a href="#publications">Publications</a><a href="#experience">Experience</a><a href="#awards">Awards</a><a href="#skills">Skills</a>
</nav>

{% assign section_order = 'Education|Projects|Publications|Experience|Awards|Skills|Languages|Interests' | split: '|' %}
{% for section_name in section_order %}

  <section class="hy-cv-section" id="{{ section_name | downcase }}">
    <h2>{% case section_name %}{% when 'Projects' %}Research experience{% when 'Publications' %}Publications &amp; intellectual property{% when 'Experience' %}Professional experience{% when 'Awards' %}Selected honors{% when 'Skills' %}Methods &amp; tools{% when 'Interests' %}Research interests{% else %}{{ section_name }}{% endcase %}</h2>
    <div class="hy-cv-entries">
      {% assign entries = cv.sections[section_name] %}
      {% if section_name == 'Awards' %}{% assign entries = entries | sort: 'date' | reverse %}{% endif %}
      {% for entry in entries %}
        <article class="hy-cv-entry">
          <div class="hy-cv-entry-heading">
            <h3>{{ entry.title | default: entry.position | default: entry.institution | default: entry.name }}</h3>
            {% if entry.status %}
              <span class="hy-status">{{ entry.status }}</span>
            {% elsif entry.start_date %}
              <span>{% if section_name == 'Projects' %}{{ entry.start_date | date: '%b %Y' }} – {{ entry.end_date | date: '%b %Y' }}{% else %}{{ entry.start_date }} – {{ entry.end_date }}{% endif %}</span>
            {% elsif entry.date %}
              <span>{{ entry.date | date: '%Y' }}</span>
            {% elsif entry.releaseDate %}
              <span>{{ entry.releaseDate | slice: 0, 4 }}</span>
            {% endif %}
          </div>
          {% if entry.studyType %}<p class="hy-cv-subtitle">{{ entry.area }} · {{ entry.studyType }}</p>{% endif %}
          {% if entry.company %}<p class="hy-cv-subtitle">{{ entry.company }} · {{ entry.location }}</p>{% endif %}
          {% if entry.publisher %}<p class="hy-cv-subtitle">{{ entry.authors | join: ', ' }} · {{ entry.publisher }}</p>{% endif %}
          {% if entry.awarder %}<p class="hy-cv-subtitle">{{ entry.awarder }}</p>{% endif %}
          {% if entry.location and entry.company == nil %}<p>{{ entry.location }}{% if entry.score and entry.score != '' %} · {{ entry.score }}{% endif %}</p>{% elsif entry.score and entry.score != '' %}<p>{{ entry.score }}</p>{% endif %}
          {% if entry.summary and entry.summary != '' %}<p>{{ entry.summary }}</p>{% endif %}
          {% if entry.keywords %}<p>{{ entry.keywords }}</p>{% endif %}
          {% if entry.highlights.size > 0 %}<ul>{% for highlight in entry.highlights %}<li>{{ highlight }}</li>{% endfor %}</ul>{% endif %}
        </article>
      {% endfor %}
      {% if section_name == 'Projects' %}<a class="hy-all-work" href="{{ '/projects/' | relative_url }}">Read illustrated project accounts <span aria-hidden="true">→</span></a>{% endif %}
      {% if section_name == 'Awards' %}<a class="hy-all-work" href="{{ '/certificates/' | relative_url }}">Explore honors, awards & further learning <span aria-hidden="true">→</span></a>{% endif %}
    </div>
  </section>
{% endfor %}

<style>
.hy-cv-modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  animation: hyFadeIn 0.2s ease-out;
}
.hy-cv-modal-box {
  background: var(--hy-surface);
  border: 1px solid var(--hy-line);
  border-radius: 14px;
  width: 100%;
  max-width: 440px;
  padding: 1.5rem;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
  animation: hyScaleUp 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.hy-cv-modal-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}
@keyframes hyFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes hyScaleUp {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}
</style>

<script>
(function() {
  const modal = document.getElementById('hy-cv-modal');
  const triggerBtn = document.getElementById('hy-cv-unlock-btn');
  const closeBtn = document.getElementById('hy-cv-modal-close');
  const cancelBtn = document.getElementById('hy-cv-cancel-btn');
  const form = document.getElementById('hy-cv-form');
  const pwdInput = document.getElementById('hy-cv-pwd-input');
  const toggleBtn = document.getElementById('hy-cv-pwd-toggle');
  const pwdIcon = document.getElementById('hy-cv-pwd-icon');
  const statusMsg = document.getElementById('hy-cv-status-msg');
  const submitBtn = document.getElementById('hy-cv-submit-btn');

  let decryptedBlobUrl = null;

  function showModal() {
    if (!modal) return;
    modal.style.display = 'flex';
    pwdInput.value = '';
    statusMsg.style.display = 'none';
    submitBtn.disabled = false;
    submitBtn.textContent = 'Unlock & View';
    setTimeout(() => pwdInput.focus(), 50);
  }

  function hideModal() {
    if (!modal) return;
    modal.style.display = 'none';
    statusMsg.style.display = 'none';
  }

  if (triggerBtn) triggerBtn.addEventListener('click', showModal);
  if (closeBtn) closeBtn.addEventListener('click', hideModal);
  if (cancelBtn) cancelBtn.addEventListener('click', hideModal);

  if (modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === modal) hideModal();
    });
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modal && modal.style.display === 'flex') {
      hideModal();
    }
  });

  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      if (pwdInput.type === 'password') {
        pwdInput.type = 'text';
        pwdIcon.classList.remove('fa-eye');
        pwdIcon.classList.add('fa-eye-slash');
      } else {
        pwdInput.type = 'password';
        pwdIcon.classList.remove('fa-eye-slash');
        pwdIcon.classList.add('fa-eye');
      }
    });
  }

  async function decryptAndOpen(password) {
    submitBtn.disabled = true;
    submitBtn.textContent = 'Decrypting...';
    statusMsg.style.display = 'block';
    statusMsg.style.background = 'var(--hy-teal-soft)';
    statusMsg.style.color = 'var(--hy-teal)';
    statusMsg.textContent = '⏳ Decrypting and verifying access...';

    let newTab = null;
    try {
      newTab = window.open('about:blank', '_blank');
      if (newTab) {
        newTab.document.write('<p style="font-family:sans-serif;padding:2rem;color:#333;">Decrypting CV document, please wait...</p>');
      }
    } catch (e) {
      // ignore popup blocker error
    }

    try {
      const encUrl = '{{ "/assets/pdf/han-yang-academic-cv.enc" | relative_url }}';
      const response = await fetch(encUrl);
      if (!response.ok) throw new Error('Could not load encrypted document.');
      const buffer = await response.arrayBuffer();

      const payload = new Uint8Array(buffer);
      const salt = payload.slice(0, 16);
      const iv = payload.slice(16, 28);
      const ciphertext = payload.slice(28);

      const enc = new TextEncoder();
      const keyMaterial = await crypto.subtle.importKey(
        'raw',
        enc.encode(password),
        { name: 'PBKDF2' },
        false,
        ['deriveKey']
      );

      const key = await crypto.subtle.deriveKey(
        {
          name: 'PBKDF2',
          salt: salt,
          iterations: 100000,
          hash: 'SHA-256'
        },
        keyMaterial,
        { name: 'AES-GCM', length: 256 },
        false,
        ['decrypt']
      );

      const decrypted = await crypto.subtle.decrypt(
        { name: 'AES-GCM', iv: iv },
        key,
        ciphertext
      );

      const blob = new Blob([decrypted], { type: 'application/pdf' });
      decryptedBlobUrl = URL.createObjectURL(blob);

      statusMsg.style.background = 'rgba(16, 185, 129, 0.15)';
      statusMsg.style.color = '#10b981';
      statusMsg.innerHTML = '✅ Decryption successful! <a href="' + decryptedBlobUrl + '" target="_blank" style="text-decoration:underline;font-weight:600;color:inherit;margin-left:0.3rem;">Open PDF ↗</a>';

      if (newTab && !newTab.closed) {
        newTab.location.href = decryptedBlobUrl;
        setTimeout(hideModal, 1000);
      } else {
        window.open(decryptedBlobUrl, '_blank');
        setTimeout(hideModal, 1000);
      }
    } catch (err) {
      if (newTab && !newTab.closed) {
        newTab.close();
      }
      submitBtn.disabled = false;
      submitBtn.textContent = 'Unlock & View';
      statusMsg.style.display = 'block';
      statusMsg.style.background = 'rgba(239, 68, 68, 0.15)';
      statusMsg.style.color = '#ef4444';
      statusMsg.textContent = '❌ Incorrect password. Please try again or contact the author.';
      pwdInput.focus();
      pwdInput.select();
    }
  }

  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const pwd = pwdInput.value;
      if (!pwd) return;
      decryptAndOpen(pwd);
    });
  }
})();
</script>
