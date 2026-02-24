<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { RouterView } from 'vue-router';
import SproutLoader from './components/SproutLoader.vue';
import CyberDog from './components/CyberDog.vue';

const isLoading = ref(true);
const mouseX = ref(0);
const mouseY = ref(0);

const updateCursor = (e) => {
  mouseX.value = e.clientX;
  mouseY.value = e.clientY;
};

onMounted(() => {
  window.addEventListener('mousemove', updateCursor);
  setTimeout(() => { isLoading.value = false; }, 3500); 
});

onUnmounted(() => {
  window.removeEventListener('mousemove', updateCursor);
});
</script>

<template>
  <div class="paw-cursor" :style="{ left: mouseX + 'px', top: mouseY + 'px' }">🐾</div>
  <CyberDog v-if="!isLoading" />

  <Transition name="fade">
    <SproutLoader v-if="isLoading" />
  </Transition>

  <div v-if="!isLoading" class="app-wrapper">
  <nav class="cyber-nav">
    <RouterLink to="/">[ PROFILE ]</RouterLink>
    <RouterLink to="/guestbook">[ GUESTBOOK ]</RouterLink>
  </nav>
    <RouterView />
  </div>
</template>

<style>
* {
  margin: 0; padding: 0; box-sizing: border-box; cursor: none !important;
}

body {
  background-color: #050a0e;
  /* Cyber grid background pattern */
  background-image: 
    linear-gradient(rgba(74, 222, 128, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(74, 222, 128, 0.03) 1px, transparent 1px);
  background-size: 30px 30px;
  color: #e0e0e0;
  font-family: 'Poppins', sans-serif;
  overflow-x: hidden;
  min-height: 100vh;
}

.paw-cursor {
  position: fixed; pointer-events: none; font-size: 24px; z-index: 99999;
  transform: translate(-50%, -50%); text-shadow: 0 0 12px #4ade80;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.8s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.cyber-nav {
  display: flex;
  justify-content: center;
  gap: 30px;
  padding: 20px 0;
  position: relative;
  z-index: 100;
  background: rgba(5, 10, 14, 0.8);
  border-bottom: 1px solid rgba(74, 222, 128, 0.2);
}

.cyber-nav a {
  color: #b0c4de;
  text-decoration: none;
  font-family: 'Courier New', monospace;
  font-weight: bold;
  letter-spacing: 2px;
  transition: color 0.3s, text-shadow 0.3s;
}

.cyber-nav a:hover,
.cyber-nav a.router-link-active {
  color: #4ade80;
  text-shadow: 0 0 10px rgba(74, 222, 128, 0.8);
}

.app-wrapper {
  padding-top: 20px;
}
</style>