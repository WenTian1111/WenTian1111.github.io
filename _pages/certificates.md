---
layout: page
title: Certificates & Honors
permalink: /certificates/
nav: true
nav_order: 5
---

<!-- tiny-slider（无依赖，支持自动播放/拖拽/循环） -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.4/tiny-slider.css" crossorigin="anonymous" referrerpolicy="no-referrer"/>

<style>
  /* 轮播容器与图片样式 */
  #certs .slide {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 6px;
  }
  #certs .slide img{
    max-height: 220px;         /* 控制高度，避免过大 */
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,.25);
    background: rgba(255,255,255,.04);
  }

  /* tiny-slider 默认按钮微调 */
  #certs .tns-controls{
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 6px;
  }
  #certs .tns-controls button{
    background: transparent;
    border: 0;
    font-size: 26px;
    line-height: 1;
    padding: .25rem .5rem;
    color: var(--bs-body-color, #e5e5e5);
    opacity: .85;
    cursor: pointer;
  }
  #certs .tns-controls button:hover{ opacity: 1; }

  /* 计数器 */
  #certs .counter{
    font-size: .9rem;
    color: #9aa0a6;
  }
</style>

<p class="text-center">A rotating display of my 43 professional certificates and selected honors.</p>

<div id="certs" class="container my-3">
  <div class="my-slider">
    {% for i in (1..43) %}
      <div class="slide">
        <img
          src="{{ '/assets/img/certificates' | relative_url }}/{{ i }}.jpg"
          alt="Certificate {{ i }}"
          loading="lazy">
      </div>
    {% endfor %}
  </div>

  <div class="d-flex justify-content-center align-items-center gap-2 mt-2">
    <div class="counter" id="cert-count">1 / 43</div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.4/min/tiny-slider.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
(function () {
  var slider = tns({
    container: '#certs .my-slider',
    items: 3,                // 一次显示3张
    gutter: 10,              // 图片间距
    slideBy: 1,              // 每次滑动1张
    mouseDrag: true,         // 支持拖拽/触摸
    swipeAngle: 15,
    autoplay: true,          // 自动播放
    autoplayTimeout: 2500,   // 自动播放间隔(ms)
    autoplayHoverPause: true,
    autoplayButtonOutput: false,
    speed: 400,
    loop: true,              // 无限循环
    controls: true,          // 左右按钮
    controlsText: ['‹','›'],
    nav: false,              // 关闭小圆点（如需可改为 true）
    responsive: {
      0:   { items: 1 },     // 手机
      576: { items: 2 },     // 平板
      992: { items: 3 }      // 桌面
    }
  });

  // 计数器（当前/总数）
  var total = slider.getInfo().slideCount;
  var counter = document.getElementById('cert-count');
  function updateCounter(){
    var i = slider.getInfo().displayIndex; // 1-based
    counter.textContent = i + ' / ' + total;
  }
  slider.events.on('indexChanged', updateCounter);
  updateCounter();
})();
</script>

<hr>

### Selected Honors and Awards

This section highlights some of the key honors received for academic excellence and innovation. For a complete list, please see the **Awards** section on my [CV page](/cv/).

* **Chongqing Advanced Individual for Innovation Ability Enhancement (Top 0.09%, One of the fastest students to be awarded the honor)**
  * *Awarded by: Chongqing Municipal Education Commission*
  * *Date: June 2024*

* **VTR Bio-Tech Scholarship (Top 0.08%, Only one undergraduate recipient)**
  * *Awarded by: Guangdong VTR Bio-Tech Co., Ltd.*
  * *Date: March 2025*

* **The Chinese Mathematics Competitions (CMC), National First Prize**
  * *Awarded by: Chinese Mathematical Society*
  * *Date: March 2023*

* **'Certification Cup' Mathematical China Modeling Network Challenge, National First Prize**
  * *Awarded by: Computational Systems Biology Society of Operations Research Society of China*
  * *Date: April 2024*
