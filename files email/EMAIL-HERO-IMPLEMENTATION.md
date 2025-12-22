# Email Marketing Hero Animation - Implementation Guide

## Overview
Add floating email cards, metric cards, notification toast, and flow bar to the Email Marketing service page hero. Creates a dynamic "email marketing command center" feel.

---

## Visual Layout
```
┌─────────────────────────────────────────────────────────┐
│                           [Notification Toast]          │
│  [Email Card 1]                         [Email Card 3]  │
│                                                         │
│      [Metric 1]      HERO CONTENT       [Metric 2]      │
│                                                         │
│  [Email Card 2]                         [Email Card 4]  │
│                                                         │
│            [──── Flow Bar at Bottom ────]               │
└─────────────────────────────────────────────────────────┘
```

---

## CSS to Add

### 1. Floating Email Cards
```css
/* Email Cards Container */
.email-cards-container {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
}

.email-card {
    position: absolute;
    width: 200px;
    background: rgba(20, 20, 20, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 14px;
    padding: 14px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.08);
}

.email-card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.email-avatar {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: linear-gradient(135deg, #d4af37, #aa8a2a);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
}

.email-meta {
    flex: 1;
}

.email-sender {
    font-size: 0.75rem;
    font-weight: 600;
    color: #fff;
}

.email-time {
    font-size: 0.6rem;
    color: #666;
}

.email-subject {
    font-size: 0.75rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 4px;
    line-height: 1.3;
}

.email-preview {
    font-size: 0.65rem;
    color: #666;
    line-height: 1.4;
}

.email-metric {
    position: absolute;
    top: -10px;
    right: -10px;
    background: #22c55e;
    color: #000;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 4px 8px;
    border-radius: 20px;
    box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
}
```

### 2. Email Card Positions & Animations
```css
.card-left-1 {
    left: 5%;
    top: 20%;
    transform: rotateY(20deg) rotateX(5deg) rotateZ(-5deg);
    animation: floatLeft1 6s ease-in-out infinite;
}

.card-left-2 {
    left: 8%;
    bottom: 22%;
    transform: rotateY(15deg) rotateX(-3deg) rotateZ(3deg);
    animation: floatLeft2 7s ease-in-out infinite;
}

.card-right-1 {
    right: 5%;
    top: 18%;
    transform: rotateY(-20deg) rotateX(5deg) rotateZ(5deg);
    animation: floatRight1 5.5s ease-in-out infinite;
}

.card-right-2 {
    right: 8%;
    bottom: 25%;
    transform: rotateY(-15deg) rotateX(-3deg) rotateZ(-3deg);
    animation: floatRight2 6.5s ease-in-out infinite;
}

@keyframes floatLeft1 {
    0%, 100% { transform: rotateY(20deg) rotateX(5deg) rotateZ(-5deg) translateY(0); }
    50% { transform: rotateY(22deg) rotateX(7deg) rotateZ(-6deg) translateY(-15px); }
}

@keyframes floatLeft2 {
    0%, 100% { transform: rotateY(15deg) rotateX(-3deg) rotateZ(3deg) translateY(0); }
    50% { transform: rotateY(13deg) rotateX(-5deg) rotateZ(4deg) translateY(-12px); }
}

@keyframes floatRight1 {
    0%, 100% { transform: rotateY(-20deg) rotateX(5deg) rotateZ(5deg) translateY(0); }
    50% { transform: rotateY(-22deg) rotateX(7deg) rotateZ(6deg) translateY(-18px); }
}

@keyframes floatRight2 {
    0%, 100% { transform: rotateY(-15deg) rotateX(-3deg) rotateZ(-3deg) translateY(0); }
    50% { transform: rotateY(-13deg) rotateX(-5deg) rotateZ(-4deg) translateY(-10px); }
}
```

### 3. Floating Metric Cards
```css
.metric-card {
    position: absolute;
    background: rgba(15, 15, 15, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 14px 18px;
    text-align: center;
    z-index: 3;
}

.metric-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #d4af37;
    line-height: 1;
}

.metric-label {
    font-size: 0.6rem;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 4px;
}

.metric-1 {
    left: 12%;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0;
    animation: fadeIn 1s ease 0.8s forwards, floatMetric1 8s ease-in-out 1s infinite;
}

.metric-2 {
    right: 12%;
    top: 48%;
    transform: translateY(-50%);
    opacity: 0;
    animation: fadeIn 1s ease 1s forwards, floatMetric2 7s ease-in-out 1.2s infinite;
}

@keyframes floatMetric1 {
    0%, 100% { transform: translateY(-50%); }
    50% { transform: translateY(calc(-50% - 8px)); }
}

@keyframes floatMetric2 {
    0%, 100% { transform: translateY(-50%); }
    50% { transform: translateY(calc(-50% - 10px)); }
}
```

### 4. Notification Toast
```css
.notification-toast {
    position: absolute;
    top: 12%;
    right: 18%;
    background: rgba(20, 20, 20, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    z-index: 4;
    opacity: 0;
    transform: translateX(30px);
    animation: slideInNotif 0.6s ease 1.5s forwards;
}

@keyframes slideInNotif {
    to { opacity: 1; transform: translateX(0); }
}

.notif-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, #22c55e, #15803d);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}

.notif-content {
    flex: 1;
}

.notif-title {
    font-size: 0.75rem;
    font-weight: 600;
    color: #fff;
}

.notif-desc {
    font-size: 0.65rem;
    color: #666;
}

.notif-badge {
    background: #d4af37;
    color: #000;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
}

/* Pulsing indicator dot */
.notification-toast::before {
    content: '';
    position: absolute;
    top: -4px;
    right: -4px;
    width: 10px;
    height: 10px;
    background: #22c55e;
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.3); opacity: 0.7; }
}
```

### 5. Bottom Flow Bar
```css
.flow-bar {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 0;
    z-index: 10;
    opacity: 0;
    animation: fadeIn 1s ease 1s forwards;
}

.flow-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 1.5rem;
}

.flow-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #333;
    margin-bottom: 8px;
}

.flow-dot.active {
    background: #d4af37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
}

.flow-dot.success {
    background: #22c55e;
    box-shadow: 0 0 15px rgba(34, 197, 94, 0.4);
}

.flow-label {
    font-size: 0.65rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.flow-node.active .flow-label {
    color: #d4af37;
}

.flow-node.success .flow-label {
    color: #22c55e;
}

.flow-line {
    width: 50px;
    height: 2px;
    background: #222;
    margin-bottom: 20px;
}

.flow-line.animated {
    background: linear-gradient(90deg, #d4af37, #333);
    background-size: 200% 100%;
    animation: flowPulse 2s ease-in-out infinite;
}

@keyframes flowPulse {
    0%, 100% { background-position: 100% 0; }
    50% { background-position: 0% 0; }
}
```

### 6. Responsive Styles
```css
@media (max-width: 1200px) {
    .email-card { width: 170px; padding: 12px; }
    .card-left-1 { left: 2%; }
    .card-left-2 { left: 4%; }
    .card-right-1 { right: 2%; }
    .card-right-2 { right: 4%; }
    .metric-1 { left: 3%; }
    .metric-2 { right: 3%; }
    .notification-toast { right: 10%; top: 10%; }
}

@media (max-width: 1000px) {
    .metric-card { display: none; }
    .notification-toast { display: none; }
}

@media (max-width: 900px) {
    .email-card { width: 150px; padding: 10px; }
    .email-avatar { width: 26px; height: 26px; }
    .email-subject { font-size: 0.7rem; }
    .email-preview { display: none; }
    .card-left-2, .card-right-2 { display: none; }
}

@media (max-width: 768px) {
    .email-cards-container { display: none; }
    .flow-bar { display: none; }
}
```

### 7. Required Base Animation
```css
@keyframes fadeIn {
    to { opacity: 1; }
}
```

---

## HTML Structure

Add this inside the `.hero` section, BEFORE the `.hero-content` div:

```html
<!-- Floating Email Cards -->
<div class="email-cards-container">
    <!-- Left Side -->
    <div class="email-card card-left-1">
        <div class="email-metric">42% open</div>
        <div class="email-card-header">
            <div class="email-avatar">👋</div>
            <div class="email-meta">
                <div class="email-sender">Welcome Series</div>
                <div class="email-time">Just now</div>
            </div>
        </div>
        <div class="email-subject">Welcome to the family!</div>
        <div class="email-preview">Here's your exclusive 15% discount code to get started...</div>
    </div>

    <div class="email-card card-left-2">
        <div class="email-metric">€8.4K rev</div>
        <div class="email-card-header">
            <div class="email-avatar" style="background: linear-gradient(135deg, #ef4444, #b91c1c);">🛒</div>
            <div class="email-meta">
                <div class="email-sender">Abandoned Cart</div>
                <div class="email-time">1h ago</div>
            </div>
        </div>
        <div class="email-subject">You left something behind</div>
        <div class="email-preview">Your items are waiting! Complete your order before they're gone...</div>
    </div>

    <!-- Right Side -->
    <div class="email-card card-right-1">
        <div class="email-card-header">
            <div class="email-avatar" style="background: linear-gradient(135deg, #8b5cf6, #6d28d9);">📰</div>
            <div class="email-meta">
                <div class="email-sender">Weekly Newsletter</div>
                <div class="email-time">Today</div>
            </div>
        </div>
        <div class="email-subject">This week's top picks</div>
        <div class="email-preview">Curated content just for you based on your preferences...</div>
    </div>

    <div class="email-card card-right-2">
        <div class="email-metric">12% CTR</div>
        <div class="email-card-header">
            <div class="email-avatar" style="background: linear-gradient(135deg, #22c55e, #15803d);">💚</div>
            <div class="email-meta">
                <div class="email-sender">Win-back Flow</div>
                <div class="email-time">3d ago</div>
            </div>
        </div>
        <div class="email-subject">We miss you! Here's 20% off</div>
        <div class="email-preview">It's been a while since your last visit. Come back and save...</div>
    </div>
</div>

<!-- Floating Metric Cards -->
<div class="metric-card metric-1">
    <div class="metric-value">47%</div>
    <div class="metric-label">Avg Open Rate</div>
</div>

<div class="metric-card metric-2">
    <div class="metric-value">€847K</div>
    <div class="metric-label">Revenue Generated</div>
</div>

<!-- Notification Toast -->
<div class="notification-toast">
    <div class="notif-icon">✓</div>
    <div class="notif-content">
        <div class="notif-title">Flow Triggered</div>
        <div class="notif-desc">Welcome series sent to 1,247 subscribers</div>
    </div>
    <div class="notif-badge">Live</div>
</div>
```

Add this AFTER the `.hero-content` div (at the bottom of hero):

```html
<!-- Bottom Flow Indicator -->
<div class="flow-bar">
    <div class="flow-node active">
        <div class="flow-dot active"></div>
        <div class="flow-label">Trigger</div>
    </div>
    <div class="flow-line animated"></div>
    <div class="flow-node">
        <div class="flow-dot"></div>
        <div class="flow-label">Email 1</div>
    </div>
    <div class="flow-line"></div>
    <div class="flow-node">
        <div class="flow-dot"></div>
        <div class="flow-label">Wait</div>
    </div>
    <div class="flow-line"></div>
    <div class="flow-node">
        <div class="flow-dot"></div>
        <div class="flow-label">Email 2</div>
    </div>
    <div class="flow-line"></div>
    <div class="flow-node success">
        <div class="flow-dot success"></div>
        <div class="flow-label">Convert</div>
    </div>
</div>
```

---

## Important Notes

1. **Hero must have**: `position: relative; overflow: hidden;`
2. **Hero content must have**: `position: relative; z-index: 10;` (to sit above all floating elements)
3. **Z-index layering**:
   - Email cards: z-index 2
   - Metric cards: z-index 3
   - Notification toast: z-index 4
   - Radial gradient overlay: z-index 5
   - Hero content: z-index 10
   - Flow bar: z-index 10
4. **All floating elements are `pointer-events: none`** so users can click CTAs
5. **Animation delays create staggered entrance**:
   - Metric cards: 0.8s, 1s
   - Notification toast: 1.5s
   - Flow bar: 1s

---

## Color Reference
- Background: #000000
- Accent (gold): #d4af37
- Success (green): #22c55e
- Card backgrounds: rgba(20, 20, 20, 0.9)
- Text primary: #ffffff
- Text secondary: #888888, #666666
- Borders: rgba(255,255,255,0.08)

---

## Avatar Gradients for Email Cards
- Welcome (gold): `linear-gradient(135deg, #d4af37, #aa8a2a)`
- Abandoned Cart (red): `linear-gradient(135deg, #ef4444, #b91c1c)`
- Newsletter (purple): `linear-gradient(135deg, #8b5cf6, #6d28d9)`
- Win-back (green): `linear-gradient(135deg, #22c55e, #15803d)`
