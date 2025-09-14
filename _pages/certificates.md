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
    display: block;
    max-height: 220px;         /* 控制高度，避免过大 */
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,.25);
    background: rgba(255,255,255,.04);
  }

  /* Fallback：如果 tiny-slider 未加载成功，则静态三列栅格展示所有图片 */
  #certs .my-slider:not(.tns-slider){
    display: grid;
    grid-template-columns: repeat(3, minmax(0,1fr));
    gap: 10px;
  }

  /* tiny-slider 控制按钮 */
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
    <div class="slide"><img src="{{ '/assets/img/certificates/1.jpg'  | relative_url }}" alt="Certificate 1"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/2.jpg'  | relative_url }}" alt="Certificate 2"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/3.jpg'  | relative_url }}" alt="Certificate 3"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/4.jpg'  | relative_url }}" alt="Certificate 4"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/5.jpg'  | relative_url }}" alt="Certificate 5"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/6.jpg'  | relative_url }}" alt="Certificate 6"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/7.jpg'  | relative_url }}" alt="Certificate 7"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/8.jpg'  | relative_url }}" alt="Certificate 8"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/9.jpg'  | relative_url }}" alt="Certificate 9"  loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/10.jpg' | relative_url }}" alt="Certificate 10" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/11.jpg' | relative_url }}" alt="Certificate 11" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/12.jpg' | relative_url }}" alt="Certificate 12" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/13.jpg' | relative_url }}" alt="Certificate 13" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/14.jpg' | relative_url }}" alt="Certificate 14" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/15.jpg' | relative_url }}" alt="Certificate 15" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/16.jpg' | relative_url }}" alt="Certificate 16" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/17.jpg' | relative_url }}" alt="Certificate 17" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/18.jpg' | relative_url }}" alt="Certificate 18" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/19.jpg' | relative_url }}" alt="Certificate 19" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/20.jpg' | relative_url }}" alt="Certificate 20" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/21.jpg' | relative_url }}" alt="Certificate 21" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/22.jpg' | relative_url }}" alt="Certificate 22" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/23.jpg' | relative_url }}" alt="Certificate 23" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/24.jpg' | relative_url }}" alt="Certificate 24" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/25.jpg' | relative_url }}" alt="Certificate 25" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/26.jpg' | relative_url }}" alt="Certificate 26" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/27.jpg' | relative_url }}" alt="Certificate 27" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/28.jpg' | relative_url }}" alt="Certificate 28" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/29.jpg' | relative_url }}" alt="Certificate 29" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/30.jpg' | relative_url }}" alt="Certificate 30" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/31.jpg' | relative_url }}" alt="Certificate 31" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/32.jpg' | relative_url }}" alt="Certificate 32" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/33.jpg' | relative_url }}" alt="Certificate 33" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/34.jpg' | relative_url }}" alt="Certificate 34" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/35.jpg' | relative_url }}" alt="Certificate 35" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/36.jpg' | relative_url }}" alt="Certificate 36" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/37.jpg' | relative_url }}" alt="Certificate 37" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/38.jpg' | relative_url }}" alt="Certificate 38" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/39.jpg' | relative_url }}" alt="Certificate 39" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/40.jpg' | relative_url }}" alt="Certificate 40" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/41.jpg' | relative_url }}" alt="Certificate 41" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/42.jpg' | relative_url }}" alt="Certificate 42" loading="lazy"></div>
    <div class="slide"><img src="{{ '/assets/img/certificates/43.jpg' | relative_url }}" alt="Certificate 43" loading="lazy"></div>
  </div>

  <div class="d-flex justify-content-center align-items-center gap-2 mt-2">
    <div class="counter" id="cert-count">1 / 43</div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.4/min/tiny-slider.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
(function () {
  if (window.tns) {
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
      nav: false,              // 关闭小圆点
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
  } else {
    // tiny-slider 未加载时，给出总数
    document.getElementById('cert-count').textContent = '43 / 43';
  }
})();
</script>

<hr>

### Selected Honors and Awards

This section highlights some of the key honors received for academic excellence and innovation. For a complete list, please see the **Awards** section on my [CV page](/cv/).

* **Chongqing Advanced Individual for Innovation Ability Enhancement (Top 0.09%)**
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
