<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['enter-site']);

// The word for the slot machine
const targetWord = "WELCOME";

// Holds the "strips" of random characters for each slot
const strips = ref([]);

// Controls the growing animation state
const isGrowing = ref(false);

onMounted(() => {
  const randomChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
  const tempStrips = [];
  
  for (let i = 0; i < targetWord.length; i++) {
    let strip = [];
    for (let j = 0; j < 25; j++) {
      strip.push(randomChars[Math.floor(Math.random() * randomChars.length)]);
    }
    strip.push(targetWord[i]);
    tempStrips.push(strip);
  }
  
  strips.value = tempStrips;
});

// Triggers the nature growth BEFORE entering the site
const triggerGrowth = () => {
  isGrowing.value = true;
  
  // Wait 3 seconds for the forest to grow and text to be seen before entering
  setTimeout(() => {
    emit('enter-site');
  }, 3200);
};
</script>

<template>
  <div class="loader-overlay">
    
    <div class="loader-content" :class="{ 'fade-out-content': isGrowing }">
      
      <div class="slot-container">
        <div class="slot-window" v-for="(strip, index) in strips" :key="index">
          <div class="slot-strip" :style="{ animationDelay: `${index * 0.15}s` }">
            <span v-for="(char, charIdx) in strip" :key="charIdx" class="slot-char">
              {{ char }}
            </span>
          </div>
        </div>
      </div>

      <h2 class="system-text">System Initialized</h2>
      
      <button class="oval-btn sfx-trigger" @click="triggerGrowth">
        ENTER PROFILE
      </button>
    </div>

    <div v-if="isGrowing" class="nature-growth-layer">
      
      <div class="welcome-human-text">
        WELCOME HUMAN!
      </div>

      <div class="tree tree-1">🌳</div>
      <div class="tree tree-2">🌲</div>
      <div class="tree tree-3">🌳</div>
      <div class="tree tree-4">🌲</div>
      
      <div class="flower flower-1">🌸</div>
      <div class="flower flower-2">🌻</div>
      <div class="flower flower-3">🌷</div>
      <div class="flower flower-4">🌼</div>
      <div class="flower flower-5">🌸</div>
      <div class="flower flower-6">🌹</div>
      <div class="flower flower-7">🌻</div>
      <div class="flower flower-8">🌷</div>
      <div class="flower flower-9">🌼</div>
    </div>

  </div>
</template>

<style scoped>
.loader-overlay {
  position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
  background-color: #0f172a; 
  background-image: radial-gradient(circle at center, #1a2235 0%, #0f172a 100%);
  display: flex; justify-content: center; align-items: center;
  z-index: 99999999; 
  overflow: hidden;
}

.loader-content {
  display: flex; flex-direction: column; align-items: center; gap: 40px;
  z-index: 20;
}

.fade-out-content {
  animation: hideContent 0.8s forwards;
}
@keyframes hideContent {
  to { opacity: 0; transform: translateY(-50px) scale(0.9); pointer-events: none; }
}

/* --- SLOT MACHINE --- */
.slot-container {
  display: flex; gap: 5px; font-size: 4rem; font-weight: 900;
  font-family: 'Courier New', Courier, monospace; color: #fff;
  text-shadow: 0 0 20px rgba(108, 138, 241, 0.8);
}
.slot-window {
  height: 1.1em; width: 1em; overflow: hidden; display: inline-flex;
  justify-content: center; align-items: flex-start; background: rgba(0, 0, 0, 0.4);
  border-radius: 8px; border: 1px solid rgba(108, 138, 241, 0.3);
  box-shadow: inset 0 5px 10px rgba(0,0,0,0.5);
}
.slot-strip {
  display: flex; flex-direction: column;
  animation: spinSlot 2s cubic-bezier(0.15, 0.85, 0.2, 1) forwards;
}
.slot-char { height: 1.1em; display: flex; justify-content: center; align-items: center; }

@keyframes spinSlot {
  0% { transform: translateY(0); opacity: 0.5; filter: blur(2px); }
  100% { transform: translateY(calc(-100% + 1.1em)); opacity: 1; filter: blur(0px); }
}

/* --- BUTTON & SUBTEXT --- */
.system-text {
  color: #6c8af1; font-family: 'Courier New', Courier, monospace;
  font-size: 1.2rem; letter-spacing: 5px; text-transform: uppercase;
  animation: pulse 2s infinite ease-in-out; margin: 0;
}
.oval-btn {
  background: linear-gradient(135deg, #6c8af1, #3b4d80); color: white;
  font-family: 'Poppins', sans-serif; font-size: 1.3rem; font-weight: 800;
  letter-spacing: 2px; border: none; padding: 20px 80px; border-radius: 50px; 
  cursor: pointer; box-shadow: 0 10px 30px rgba(108, 138, 241, 0.3);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.oval-btn:hover {
  transform: scale(1.08); box-shadow: 0 15px 40px rgba(108, 138, 241, 0.6);
  background: linear-gradient(135deg, #7b98f2, #475a96);
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; filter: drop-shadow(0 0 5px rgba(108,138,241,0.2)); }
  50% { opacity: 1; filter: drop-shadow(0 0 15px rgba(108,138,241,0.8)); }
}

/* --- 🌟 WELCOME HUMAN TEXT STYLES 🌟 --- */
.welcome-human-text {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Courier New', Courier, monospace;
  font-size: 3.5rem;
  font-weight: 900;
  color: #22c55e;
  text-shadow: 0 0 20px rgba(34, 197, 94, 0.8), 0 0 40px rgba(34, 197, 94, 0.4);
  z-index: 100;
  text-align: center;
  width: 100%;
  white-space: nowrap;
  animation: textFloat 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  opacity: 0;
}

@keyframes textFloat {
  0% { transform: translate(-50%, 0%) scale(0.5); opacity: 0; }
  100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
}

/* --- NATURE GROWTH --- */
.nature-growth-layer {
  position: absolute; bottom: -20px; left: 0; width: 100vw; height: 100vh;
  pointer-events: none; z-index: 10;
}

.tree, .flower {
  position: absolute; bottom: 0; transform-origin: bottom center;
  transform: scale(0); opacity: 0;
  animation: popUp 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  filter: drop-shadow(0 10px 20px rgba(34, 197, 94, 0.4));
}

.tree { font-size: 16rem; z-index: 12; }
.tree-1 { left: -5%; animation-delay: 0.2s; font-size: 20rem; bottom: -30px; }
.tree-2 { left: 25%; animation-delay: 0.6s; font-size: 14rem; }
.tree-3 { right: 20%; animation-delay: 0.4s; font-size: 18rem; bottom: -10px; }
.tree-4 { right: -5%; animation-delay: 0.1s; font-size: 22rem; bottom: -40px; }

.flower { font-size: 4.5rem; z-index: 15; bottom: 10px; }
.flower-1 { left: 10%; animation-delay: 0.8s; }
.flower-2 { left: 18%; animation-delay: 1.1s; font-size: 3rem; }
.flower-3 { left: 35%; animation-delay: 0.9s; font-size: 5rem; }
.flower-4 { left: 45%; animation-delay: 1.2s; font-size: 3.5rem; bottom: 20px; }
.flower-5 { left: 55%; animation-delay: 0.7s; }
.flower-6 { left: 65%; animation-delay: 1.0s; font-size: 4rem; }
.flower-7 { left: 78%; animation-delay: 1.3s; font-size: 3rem; bottom: 15px;}
.flower-8 { right: 15%; animation-delay: 0.9s; font-size: 4.5rem; }
.flower-9 { right: 5%; animation-delay: 1.1s; font-size: 3.5rem; }

@keyframes popUp {
  0% { transform: scale(0) translateY(50px); opacity: 0; }
  100% { transform: scale(1) translateY(0); opacity: 1; }
}

/* --- MOBILE RESPONSIVENESS --- */
@media (max-width: 768px) {
  .slot-container { font-size: 2.5rem; }
  .welcome-human-text { font-size: 2.2rem; }
  .oval-btn { padding: 18px 50px; font-size: 1.1rem; }
  .tree { font-size: 12rem; }
}

@media (max-width: 480px) {
  .slot-container { font-size: 1.8rem; }
  .welcome-human-text { font-size: 1.8rem; }
  .system-text { font-size: 0.9rem; }
  .tree-1 { font-size: 14rem; }
  .tree-4 { display: none; }
}
</style>