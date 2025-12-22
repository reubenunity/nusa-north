# Floating 3D Phones Hero Animation - Implementation Guide

## Overview
Add a floating 3D phone mockups animation to the Performance Creative service page hero section. Phones should float around the edges of the hero with perspective transforms, surrounding the centered text content.

---

## Visual Reference
- Phones arranged around hero perimeter (2 on left, 2 on right, 1 at bottom center)
- Each phone tilted with 3D perspective (rotateX, rotateY, rotateZ)
- Subtle floating animation (up/down movement, 5-7 second cycles)
- Radial gradient overlay to darken edges and make center text pop
- Phone screens display ad creative examples

---

## CSS to Add

### 1. Phones Container (add to existing styles)
```css
/* Floating Phones Container */
.phones-container {
    position: absolute;
    inset: 0;
    pointer-events: none;
    perspective: 1200px;
    transform-style: preserve-3d;
}

/* Individual Phone */
.phone {
    position: absolute;
    width: 180px;
    height: 380px;
    border-radius: 36px;
    background: #1a1a1a;
    padding: 8px;
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.5),
        0 0 0 1px rgba(255, 255, 255, 0.1);
    transform-style: preserve-3d;
}

.phone-screen {
    width: 100%;
    height: 100%;
    border-radius: 28px;
    overflow: hidden;
    background: #000;
    position: relative;
}

.phone-screen img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Phone Notch */
.phone::before {
    content: '';
    position: absolute;
    top: 12px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 24px;
    background: #000;
    border-radius: 20px;
    z-index: 10;
}
```

### 2. Phone Positions (5 phones)
```css
.phone-1 {
    left: 5%;
    top: 15%;
    transform: rotateY(25deg) rotateX(5deg) rotateZ(-8deg);
    animation: float1 6s ease-in-out infinite;
    z-index: 2;
}

.phone-2 {
    left: 12%;
    bottom: 10%;
    transform: rotateY(20deg) rotateX(-5deg) rotateZ(5deg);
    animation: float2 7s ease-in-out infinite;
    z-index: 3;
}

.phone-3 {
    right: 5%;
    top: 20%;
    transform: rotateY(-25deg) rotateX(5deg) rotateZ(8deg);
    animation: float3 5.5s ease-in-out infinite;
    z-index: 2;
}

.phone-4 {
    right: 12%;
    bottom: 8%;
    transform: rotateY(-20deg) rotateX(-5deg) rotateZ(-5deg);
    animation: float4 6.5s ease-in-out infinite;
    z-index: 4;
}

.phone-5 {
    left: 50%;
    bottom: -5%;
    transform: translateX(-50%) rotateX(-15deg);
    animation: float5 7s ease-in-out infinite;
    z-index: 1;
    opacity: 0.6;
}
```

### 3. Float Animations
```css
@keyframes float1 {
    0%, 100% { transform: rotateY(25deg) rotateX(5deg) rotateZ(-8deg) translateY(0); }
    50% { transform: rotateY(28deg) rotateX(8deg) rotateZ(-10deg) translateY(-20px); }
}

@keyframes float2 {
    0%, 100% { transform: rotateY(20deg) rotateX(-5deg) rotateZ(5deg) translateY(0); }
    50% { transform: rotateY(18deg) rotateX(-8deg) rotateZ(3deg) translateY(-15px); }
}

@keyframes float3 {
    0%, 100% { transform: rotateY(-25deg) rotateX(5deg) rotateZ(8deg) translateY(0); }
    50% { transform: rotateY(-28deg) rotateX(8deg) rotateZ(10deg) translateY(-25px); }
}

@keyframes float4 {
    0%, 100% { transform: rotateY(-20deg) rotateX(-5deg) rotateZ(-5deg) translateY(0); }
    50% { transform: rotateY(-18deg) rotateX(-8deg) rotateZ(-3deg) translateY(-18px); }
}

@keyframes float5 {
    0%, 100% { transform: translateX(-50%) rotateX(-15deg) translateY(0); }
    50% { transform: translateX(-50%) rotateX(-18deg) translateY(-10px); }
}
```

### 4. Hero Gradient Overlay (for depth)
```css
.hero::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, transparent 0%, rgba(0,0,0,0.7) 70%);
    z-index: 5;
    pointer-events: none;
}
```

### 5. Responsive Adjustments
```css
@media (max-width: 1024px) {
    .phone {
        width: 140px;
        height: 300px;
        border-radius: 28px;
    }
    .phone-screen { border-radius: 22px; }
    .phone-1 { left: 2%; }
    .phone-3 { right: 2%; }
}

@media (max-width: 768px) {
    .phone {
        width: 100px;
        height: 210px;
        border-radius: 20px;
        padding: 5px;
    }
    .phone-screen { border-radius: 16px; }
    .phone::before {
        width: 50px;
        height: 16px;
        top: 8px;
    }
    .phone-5 { display: none; }
}
```

---

## HTML Structure

Add this inside the `.hero` section, BEFORE the `.hero-content` div:

```html
<!-- Floating Phones -->
<div class="phones-container">
    <div class="phone phone-1">
        <div class="phone-screen">
            <img src="assets/images/phone-screens/ad-1.jpg" alt="Ad creative">
        </div>
    </div>

    <div class="phone phone-2">
        <div class="phone-screen">
            <img src="assets/images/phone-screens/ad-2.jpg" alt="Ad creative">
        </div>
    </div>

    <div class="phone phone-3">
        <div class="phone-screen">
            <img src="assets/images/phone-screens/ad-3.jpg" alt="Ad creative">
        </div>
    </div>

    <div class="phone phone-4">
        <div class="phone-screen">
            <img src="assets/images/phone-screens/ad-4.jpg" alt="Ad creative">
        </div>
    </div>

    <div class="phone phone-5">
        <div class="phone-screen">
            <img src="assets/images/phone-screens/ad-5.jpg" alt="Ad creative">
        </div>
    </div>
</div>
```

---

## Required Images

Create 5 phone screen images at 9:16 aspect ratio (e.g., 450x800px):
- `ad-1.jpg` - Orange/red promotional ad (e.g., "SAVE ON YOUR FAVS")
- `ad-2.jpg` - Product launch ad (dark green/luxury feel)
- `ad-3.jpg` - Purple/lifestyle ad
- `ad-4.jpg` - Brand awareness ad
- `ad-5.jpg` - Gold/luxury hospitality ad

Place in: `assets/images/phone-screens/`

---

## Important Notes

1. **Hero must have**: `position: relative; overflow: hidden;`
2. **Hero content must have**: `position: relative; z-index: 10;` (to sit above phones and gradient)
3. **Phones container is `pointer-events: none`** so users can still click CTAs
4. **The radial gradient overlay** (z-index: 5) sits between phones and content
5. **Different animation durations** (5.5s, 6s, 6.5s, 7s) prevent synchronized movement

---

## Color Scheme Reference
- Background: #000000
- Accent: #d4af37 (gold)
- Text primary: #ffffff
- Text secondary: #b8c5c1 or #999999
- Card backgrounds: #0a0a0a, #1a1a1a
