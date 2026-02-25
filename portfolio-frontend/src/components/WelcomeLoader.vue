<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['enter-site']);
const stage = ref('slot'); 
const reels = ref(['?', '?', '?', '?', '?']);
const finalWord = ['H', 'E', 'L', 'L', 'O'];
const showEnterBtn = ref(false);

const spinReels = () => {
  reels.value.forEach((_, idx) => {
    let iteration = 0;
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const maxIterations = 20 + idx * 5;
    const interval = setInterval(() => {
      reels.value[idx] = characters.charAt(Math.floor(Math.random() * 26));
      if (++iteration > maxIterations) {
        clearInterval(interval);
        reels.value[idx] = finalWord[idx];
        if (idx === 4) setTimeout(() => { showEnterBtn.value = true; }, 500);
      }
    }, 50);
  });
};

const handleEnterClick = () => {
  stage.value = 'sprout';
  // Sprout growth duration before automatic entry
  setTimeout(() => emit('enter-site'), 3500);
};

onMounted(() => spinReels());
</script>

<template>
  <div class="loader-overlay">
    <div v-if="stage === 'slot'" class="slot-container">
      <div class="slot-window">
        <div v-for="(char, i) in reels" :key="i" class="slot-reel" :class="{ 'done': char === finalWord[i] }">
          {{ char }}
        </div>
      </div>
      <div class="slot-sub" :class="{ 'visible': showEnterBtn }">THERE</div>
      <button v-if="showEnterBtn" @click="handleEnterClick" class="enter-btn">ENTER PROFILE</button>
    </div>

    <div v-else class="sprout-stage">
      <div class="cyber-ground"></div>
      <div class="sprout">
        <div class="stem"></div>
        <div class="leaf left"></div>
        <div class="leaf right"></div>
      </div>
      <p class="loading-text">INITIALIZING NATURE.SYS_</p>
    </div>
  </div>
</template>

<style scoped>
.loader-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #0a0a0a; z-index: 10000; display: flex; justify-content: center; align-items: center; color: white; overflow: hidden; }
.slot-window { display: flex; gap: 15px; font-family: 'Courier New', monospace; font-size: 5rem; font-weight: bold; margin-bottom: 30px; }
.slot-reel { width: 80px; height: 120px; background: #222; border: 4px solid white; display: flex; align-items: center; justify-content: center; transition: 0.3s; }
.slot-reel.done { border-color: #6c8af1; color: #6c8af1; }
.slot-sub { letter-spacing: 5px; opacity: 0; transition: 1s; margin-bottom: 30px; font-size: 1.5rem; text-align: center; }
.slot-sub.visible { opacity: 1; }
.enter-btn { background: transparent; border: 3px solid white; color: white; padding: 20px 60px; font-size: 1.5rem; cursor: pointer; transition: 0.3s; font-family: 'Courier New'; }
.enter-btn:hover { background: white; color: black; box-shadow: 0 0 30px white; }

/* Sprout Animation */
.sprout-stage { display: flex; flex-direction: column; align-items: center; position: relative; }
.cyber-ground { width: 150px; height: 2px; background: #4ade80; box-shadow: 0 0 15px #4ade80; }
.sprout { position: relative; height: 60px; display: flex; justify-content: center; align-items: flex-end; }
.stem { width: 4px; height: 0; background: #4ade80; animation: growStem 2s forwards; }
.leaf { position: absolute; width: 15px; height: 15px; background: #4ade80; border-radius: 0 15px 0 15px; opacity: 0; bottom: 30px; }
.left { right: 50%; animation: growLeafLeft 1s 1.5s forwards; }
.right { left: 50%; transform: scaleX(-1); animation: growLeafRight 1s 1.8s forwards; }

@keyframes growStem { to { height: 60px; } }
@keyframes growLeafLeft { 0% { opacity: 0; transform: scale(0) rotate(-20deg); } 100% { opacity: 1; transform: scale(1) rotate(-45deg); } }
@keyframes growLeafRight { 0% { opacity: 0; transform: scaleX(-1) scale(0) rotate(-20deg); } 100% { opacity: 1; transform: scaleX(-1) scale(1) rotate(-45deg); } }
.loading-text { margin-top: 50px; color: #4ade80; font-family: 'Courier New'; letter-spacing: 3px; }
</style>