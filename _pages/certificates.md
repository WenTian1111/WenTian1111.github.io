---
layout: page
title: Certificates & Honors
permalink: /certificates/
nav: true
nav_order: 5
---

<!-- 1. 加载 Tiny Slider 的 CSS 样式 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.4/tiny-slider.css">

<!-- 2. 自定义轮播图的样式 -->
<style>
  .certs-container {
    padding: 1rem 0;
  }
  .cert-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 250px; /* 给一个固定高度，防止图片加载时页面跳动 */
  }
  .cert-slide img {
    display: block;
    max-height: 100%;
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,.2);
  }
  .tns-nav { /* 小圆点导航 */
    text-align: center;
    margin-top: 10px;
  }
  .tns-nav button {
    width: 10px;
    height: 10px;
    padding: 0;
    margin: 0 5px;
    border-radius: 50%;
    background: #555;
    border: 0;
  }
  .tns-nav button.tns-nav-active {
    background: #ddd;
  }
</style>

<p class="text-center">A rotating display of my 43 professional certificates and selected honors.</p>

<!-- 3. 轮播图的 HTML 结构 -->
<div class="certs-container">
  <div class="certs-slider">
    <div><div class="cert-slide"><img src="/assets/img/certificates/1.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/2.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/3.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/4.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/5.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/6.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/7.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/8.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/9.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/10.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/11.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/12.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/13.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/14.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/15.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/16.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/17.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/18.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/19.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/20.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/21.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/22.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/23.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/24.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/25.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/26.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/27.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/28.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/29.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/30.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/31.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/32.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/33.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/34.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/35.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/36.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/37.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/38.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/39.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/40.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/41.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/42.jpg" loading="lazy"></div></div>
    <div><div class="cert-slide"><img src="/assets/img/certificates/43.jpg" loading="lazy"></div></div>
  </div>
</div>

<!-- 4. 加载 Tiny Slider 的 JS 脚本 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.2/min/tiny-slider.js"></script>

<!-- 5. 确保页面加载完成后再执行轮播图初始化 -->
<script>
  document.addEventListener('DOMContentLoaded', function () {
    var slider = tns({
      container: '.certs-slider',
      items: 1,
      slideBy: 'page',
      autoplay: true,
      autoplayButtonOutput: false,
      controls: false, // 隐藏左右箭头
      nav: true, // 显示小圆点导航
      mouseDrag: true,
      responsive: {
        768: { // 屏幕宽度大于 768px
          items: 3,
          gutter: 15
        },
        992: { // 屏幕宽度大于 992px
          items: 5,
          gutter: 20
        }
      }
    });
  });
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
