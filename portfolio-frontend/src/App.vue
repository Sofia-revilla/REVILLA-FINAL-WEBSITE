<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { RouterView } from 'vue-router';
// RESTORED THE LOADING SCREEN IMPORT:
import WelcomeLoader from './components/WelcomeLoader.vue';

// Global State
const isLoaded = ref(false); // Changed back to false to show loader
const isDarkMode = ref(false);

// Cursor & Interaction State
const mouseX = ref(0);
const mouseY = ref(0);
const isHovering = ref(false);
let clickParticles = [];
let clickCtx = null;
let clickCanvas = null;

// Modal & UI State
const showSideNav = ref(false);
const showContactModal = ref(false);
const showRefModal = ref(false);

// Audio Player State
const isPlaying = ref(false);
const audioRef = ref(null);

// Leaf Animation Array
const leaves = Array.from({ length: 20 }, (_, i) => ({
  id: i,
  left: Math.random() * 100,
  duration: 8 + Math.random() * 7,
  delay: Math.random() * 5,
  size: 1 + Math.random() * 1.5
}));

// Cursor Logic
const updateCursor = (e) => {
  mouseX.value = e.clientX;
  mouseY.value = e.clientY;
  isHovering.value = e.target.closest('a, button, .sfx-trigger, .polaroid, .project-card, .info-card') !== null;
};

// Paw Print Click Effect (Replaced Fireworks)
const createFirework = (e) => {
  for (let i = 0; i < 6; i++) { // 6 paws per click
    clickParticles.push({
      x: e.clientX, y: e.clientY,
      vx: (Math.random() - 0.5) * 6,
      vy: (Math.random() - 0.5) * 6 - 2, // Slight upward burst
      life: 1,
      size: Math.random() * 15 + 15 // Random size between 15px and 30px
    });
  }
};

const animateFireworks = () => {
  if (clickCtx && clickCanvas) {
    clickCtx.clearRect(0, 0, clickCanvas.width, clickCanvas.height);
    clickParticles.forEach((p, i) => {
      p.x += p.vx; 
      p.y += p.vy; 
      p.life -= 0.03; // Fade out speed
      
      clickCtx.globalAlpha = Math.max(0, p.life);
      clickCtx.font = `${p.size}px sans-serif`;
      clickCtx.textAlign = 'center';
      clickCtx.textBaseline = 'middle';
      // Drawing paw prints!
      clickCtx.fillText('🐾', p.x, p.y); 
      
      if(p.life <= 0) clickParticles.splice(i, 1);
    });
  }
  requestAnimationFrame(animateFireworks);
};

const resizeCanvas = () => {
  if (clickCanvas) {
    clickCanvas.width = window.innerWidth;
    clickCanvas.height = window.innerHeight;
  }
};

// Audio Logic
const toggleAudio = () => {
  if (audioRef.value) {
    if (isPlaying.value) {
      audioRef.value.pause();
    } else {
      audioRef.value.play();
    }
    isPlaying.value = !isPlaying.value;
  }
};

onMounted(() => {
  clickCanvas = document.getElementById('click-canvas');
  if (clickCanvas) {
    clickCtx = clickCanvas.getContext('2d');
    resizeCanvas();
    animateFireworks();
  }
  
  window.addEventListener('mousemove', updateCursor);
  window.addEventListener('mousedown', createFirework);
  window.addEventListener('resize', resizeCanvas);
});

onUnmounted(() => {
  window.removeEventListener('mousemove', updateCursor);
  window.removeEventListener('mousedown', createFirework);
  window.removeEventListener('resize', resizeCanvas);
});

const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value;
  document.body.classList.toggle('dark-mode', isDarkMode.value);
};
</script>

<template>
  <canvas id="click-canvas" style="position: fixed; top: 0; left: 0; pointer-events: none; z-index: 9999999;"></canvas>

  <div class="leaf-container" aria-hidden="true">
    <div 
      v-for="leaf in leaves" 
      :key="leaf.id" 
      class="falling-leaf"
      :style="{ 
        left: leaf.left + '%', 
        animationDuration: leaf.duration + 's', 
        animationDelay: '-' + leaf.delay + 's',
        fontSize: leaf.size + 'rem'
      }"
    >
      🍃
    </div>
  </div>

  <div class="paw-cursor" :style="{ left: mouseX + 'px', top: mouseY + 'px' }">🐕</div>
  <div class="cursor-outline" :class="{ 'hovering': isHovering }" :style="{ left: mouseX + 'px', top: mouseY + 'px' }"></div>
  
  <Transition name="fade">
    <WelcomeLoader v-if="!isLoaded" @enter-site="isLoaded = true" />
  </Transition>

  <div v-if="isLoaded" :class="['app-master', { 'dark-mode': isDarkMode }]">
    
    <nav class="nav-bar">
      <div class="nav-left-icons">
        <a href="https://www.linkedin.com/in/ma-sofia-anne-revilla-" target="_blank" class="icon-box sfx-trigger"><i class="bi bi-linkedin"></i></a>
        <div class="icon-box sfx-trigger" @click="toggleTheme"><i class="bi" :class="isDarkMode ? 'bi-sun' : 'bi-moon'"></i></div>
      </div>
      <div class="nav-menu">
        <RouterLink to="/" class="active" style="text-decoration: none;">BSCS-SF Student Profile</RouterLink>
      </div>
      <div class="nav-auth-buttons">
        <button class="btn-pill btn-outline sfx-trigger" @click="showContactModal = true">Contact Me</button>
        <a href="https://github.com/Sofia-revilla" target="_blank" class="btn-pill btn-fill sfx-trigger" style="text-decoration: none;">GitHub</a>
      </div>
    </nav>

    <RouterView />

    <div class="bottom-guestbook-section">
      <p class="guestbook-note">Got a moment? Leave a trace in the digital forest... ✨</p>
      <RouterLink to="/guestbook" class="leaf-button sfx-trigger">
        🍃 Sign Guestbook
      </RouterLink>
    </div>

    <div class="heart-fab sfx-trigger" @click="showSideNav = true">
      <img src="https://i.pinimg.com/originals/6a/71/c8/6a71c8522afd22f20c4e78f96cf0b150.gif" alt="Heart Nav" />
    </div>

    <div class="side-nav" :class="{ 'active': showSideNav }">
      <span class="close-nav sfx-trigger" @click="showSideNav = false">&times;</span>
      <h3>Menu</h3>
      <RouterLink to="/" @click="showSideNav = false">Home</RouterLink>
      <RouterLink to="/guestbook" @click="showSideNav = false">Guestbook</RouterLink>
      <a href="/#projects" @click="showSideNav = false">Projects</a>
      <a href="/#gallery-section" @click="showSideNav = false">Life Gallery</a>
      <div class="nav-contact-bonus mt-5">
        <p style="font-size: 0.85rem; color: var(--text-light);"><i class="bi bi-envelope"></i> sofia.revilla@example.com</p>
      </div>
    </div>

    <div class="music-player-wrapper">
      <div class="music-player">
        <div class="player-thumb"><img src="/image/draww.png" alt="Music Thumbnail" /></div>
        <div class="player-info">
          <h5>Portfolio Vibes</h5>
          <p>Relaxing Lofi</p>
          <div class="progress-bar"><div class="progress-fill" :class="{ 'animating': isPlaying }"></div></div>
        </div>
        <div class="player-controls">
          <i class="bi bi-skip-backward-fill sfx-trigger"></i>
          <i class="bi sfx-trigger" :class="isPlaying ? 'bi-pause-circle-fill' : 'bi-play-circle-fill'" @click="toggleAudio"></i>
          <i class="bi bi-skip-forward-fill sfx-trigger"></i>
        </div>
        <audio ref="audioRef" src="/audio/down.mp3" loop></audio>
      </div>
    </div>

    <div v-if="showContactModal" class="modal-overlay" @click="showContactModal = false">
      <div class="modal-content contact-style" @click.stop>
        <span class="close-modal sfx-trigger" @click="showContactModal = false">&times;</span>
        <h2 style="margin-bottom: 20px;"><i class="bi bi-envelope"></i> Get in Touch</h2>
        <div class="modal-body-text" style="text-align: left;">
          <p><strong>Email:</strong> sofia.revilla@example.com</p>
          <p><strong>LinkedIn:</strong> linkedin.com/in/ma-sofia-anne-revilla-</p>
          <p><strong>Location:</strong> 5828 Foxhound Street, Clark Air Base, Mabalacat, Pampanga</p>
        </div>
      </div>
    </div>

    <div class="site-footer">
      WEBPROG SF241 | © 2025 Ma. Sofia Anne Revilla
    </div>

  </div>
</template>

<style>
/* --- GLOBAL CSS VARIABLES --- */
:root {
  --bg-color: #f0f2f5;
  --card-white: #ffffff;
  --primary-blue: #6c8af1;
  --primary-dark: #3b4d80;
  --text-main: #0f172a;
  --text-light: #8fa1b3;
  --body-bg-image: url('https://png.pngtree.com/background/20210715/original/pngtree-white-simple-texture-background-picture-image_1323742.jpg');
  --hero-bg: url('https://i.pinimg.com/originals/c4/15/be/c415be334309ccf0b19a2c0a44c73331.gif');
}

/* EXACT MATCH TO YOUR DARK MODE IMAGE */
body.dark-mode {
  --bg-color: #121212; 
  --card-white: #242424; 
  --primary-blue: #6c8af1; 
  --primary-dark: #242424; 
  --text-main: #e4e6eb; 
  --text-light: #a0a0a0;
  --body-bg-image: none; 
  --hero-bg: url('https://i.pinimg.com/originals/e5/40/08/e54008fec896ec085da559cf537d6f32.gif');
}

* { box-sizing: border-box; margin: 0; padding: 0; cursor: none !important; }

/* FIX FOR DARK MODE BACKGROUND CUT OFF */
html, body { 
  min-height: 100vh;
  height: 100%;
}

html {
  background-color: var(--bg-color); /* Fallback */
  transition: background-color 0.3s;
}

body { 
  background-image: var(--body-bg-image); 
  background-color: var(--bg-color); 
  color: var(--text-main); 
  font-family: 'Poppins', sans-serif; 
  transition: background-color 0.3s, color 0.3s; 
  overflow-x: hidden; 
  background-attachment: fixed; 
  background-size: cover;
  background-position: center;
}

.app-master { max-width: 1400px; margin: 0 auto; padding: 20px; position: relative; z-index: 2;}

/* --- FALLING LEAVES GLOBALS --- */
.leaf-container {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  pointer-events: none;
  z-index: 1; 
  overflow: hidden;
}
.falling-leaf {
  position: absolute;
  top: -10%;
  animation: fallDown linear infinite;
  opacity: 0.6;
}
@keyframes fallDown {
  0% { transform: translate(0, 0) rotate(0deg); opacity: 0; }
  10% { opacity: 0.6; }
  90% { opacity: 0.6; }
  100% { transform: translate(100px, 110vh) rotate(360deg); opacity: 0; }
}

/* Custom Cursor Fixes - Z-Index set to MAX so it never disappears! */
.paw-cursor { 
  position: fixed; 
  font-size: 28px; 
  z-index: 2147483647 !important; /* Maximum possible z-index */
  transform: translate(-50%, -50%); 
  pointer-events: none; 
  text-shadow: 0 0 10px var(--primary-blue); 
}
.cursor-outline { 
  position: fixed; 
  width: 40px; 
  height: 40px; 
  border: 2px solid var(--primary-blue); 
  border-radius: 50%; 
  transform: translate(-50%, -50%); 
  pointer-events: none; 
  transition: width 0.2s, height 0.2s, background-color 0.2s; 
  z-index: 2147483646 !important; 
}
.cursor-outline.hovering { width: 60px; height: 60px; background-color: rgba(108, 138, 241, 0.2); }

/* Navigation */
.nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 0 30px; }
.nav-left-icons { display: flex; gap: 15px; }
.icon-box { width: 45px; height: 45px; background: var(--card-white); border-radius: 12px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: 0.2s; }
.icon-box:hover { color: var(--primary-blue); transform: translateY(-2px); }
.btn-pill { padding: 10px 25px; border-radius: 30px; border: none; font-weight: 600; transition: 0.3s; }
.btn-pill:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
.btn-outline { background: var(--card-white); color: var(--text-main); border: 1px solid #e0e0e0; }
body.dark-mode .btn-outline { border: 1px solid #444; } 
.btn-fill { background: var(--primary-dark); color: white; }
body.dark-mode .btn-fill { background: #333; } 
.nav-menu a { text-decoration: none; color: var(--text-main); font-weight: bold; }

/* Floating Heart Nav */
.heart-fab { position: fixed; top: 20px; right: 20px; width: 60px; height: 60px; z-index: 10001; transition: 0.3s; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.2)); }
.heart-fab:hover { transform: scale(1.1) rotate(5deg); }
.heart-fab img { width: 100%; height: 100%; object-fit: contain; }

/* --- GUESTBOOK BOTTOM LEAF BUTTON --- */
.bottom-guestbook-section { text-align: center; margin-top: 80px; margin-bottom: 20px;}
.guestbook-note { font-family: 'Courier New', monospace; color: var(--text-light); margin-bottom: 15px; font-weight: bold;}
.leaf-button { 
  display: inline-block;
  background: linear-gradient(135deg, #4ade80, #166534); 
  color: white; 
  padding: 15px 30px; 
  border-radius: 0 25px 0 25px; /* Leaf shape! */
  text-decoration: none; 
  font-weight: bold; 
  font-size: 1.1rem;
  box-shadow: 0 10px 20px rgba(22, 101, 52, 0.3);
  transition: 0.3s;
}
.leaf-button:hover { transform: scale(1.05) rotate(-2deg); box-shadow: 0 15px 25px rgba(22, 101, 52, 0.5); }

/* Side Navigation */
.side-nav { position: fixed; top: 0; right: -300px; width: 300px; height: 100vh; background: var(--card-white); box-shadow: -5px 0 20px rgba(0,0,0,0.1); z-index: 10000; padding: 40px; display: flex; flex-direction: column; gap: 20px; transition: 0.4s ease-in-out; }
.side-nav.active { right: 0; }
.side-nav h3 { color: var(--primary-blue); margin-bottom: 20px; border-bottom: 2px solid var(--bg-color); padding-bottom: 10px; }
.side-nav a { text-decoration: none; color: var(--text-main); font-size: 1.1rem; font-weight: 600; transition: 0.2s; padding: 10px 0; }
.side-nav a:hover { color: var(--primary-blue); padding-left: 10px; }
.close-nav { position: absolute; top: 20px; right: 20px; font-size: 30px; color: var(--text-light); transition: 0.3s; }
.close-nav:hover { color: var(--text-main); transform: scale(1.1); }

/* Modals */
.modal-overlay { display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 100000; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-content { background: var(--card-white); padding: 40px; border-radius: 20px; max-width: 500px; width: 90%; text-align: center; color: var(--text-main); position: relative; box-shadow: 0 10px 40px rgba(0,0,0,0.2); animation: popIn 0.3s ease; }
body.dark-mode .modal-content { background: #242424; color: white;}
.close-modal { position: absolute; top: 15px; right: 25px; font-size: 30px; color: var(--text-light); transition: 0.3s; }
.close-modal:hover { color: var(--primary-blue); transform: scale(1.2); }
.modal-body-text p { margin-bottom: 15px; font-size: 0.95rem; }

/* Music Player */
.music-player-wrapper { position: fixed; bottom: 30px; left: 30px; z-index: 9000; }
.music-player { background: var(--card-white); padding: 15px; border-radius: 20px; display: flex; align-items: center; gap: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); border: 1px solid rgba(108, 138, 241, 0.2); }
.player-thumb img { width: 50px; height: 50px; border-radius: 12px; object-fit: cover; }
.player-info h5 { margin: 0; font-size: 0.9rem; color: var(--text-main); }
.player-info p { margin: 0; font-size: 0.75rem; color: var(--text-light); }
.progress-bar { width: 100%; height: 4px; background: var(--bg-color); border-radius: 2px; margin-top: 5px; overflow: hidden; }
.progress-fill { width: 0%; height: 100%; background: var(--primary-blue); }
.progress-fill.animating { animation: playProgress 30s linear infinite; }
.player-controls { display: flex; gap: 10px; color: var(--primary-blue); font-size: 1.2rem; align-items: center; }
.player-controls .bi-play-circle-fill, .player-controls .bi-pause-circle-fill { font-size: 1.8rem; }

/* Loader Transition */
.fade-enter-active, .fade-leave-active { transition: opacity 0.8s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* Footer */
.site-footer { text-align: center; margin-top: 10px; padding-bottom: 20px; color: var(--text-light); font-size: 0.85rem; font-family: 'Courier New', monospace; }

@keyframes popIn { from { transform: scale(0.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }
@keyframes playProgress { from { width: 0%; } to { width: 100%; } }
</style>