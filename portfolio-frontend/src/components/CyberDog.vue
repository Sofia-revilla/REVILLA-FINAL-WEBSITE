<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const dogX = ref(window.innerWidth / 2);
const dogY = ref(window.innerHeight / 2);
const isFacingLeft = ref(false);

let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let animationFrameId;

// Update target coordinates when mouse moves
const updateMouse = (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
};

// Physics loop to make the dog chase the mouse smoothly
const chaseCursor = () => {
  // Calculate distance
  const dx = mouseX - dogX.value;
  const dy = mouseY - dogY.value;
  
  // Flip the dog depending on direction
  if (dx < -10) isFacingLeft.value = true;
  if (dx > 10) isFacingLeft.value = false;

  // Ease towards the target (0.04 controls the speed/delay)
  dogX.value += dx * 0.04;
  dogY.value += dy * 0.04;

  animationFrameId = requestAnimationFrame(chaseCursor);
};

onMounted(() => {
  window.addEventListener('mousemove', updateMouse);
  chaseCursor();
});

onUnmounted(() => {
  window.removeEventListener('mousemove', updateMouse);
  cancelAnimationFrame(animationFrameId);
});
</script>

<template>
  <div 
    class="cyber-dog"
    :class="{ 'flip': isFacingLeft }"
    :style="{ left: dogX + 'px', top: dogY + 'px' }"
  >
    🐕
    <div class="glow"></div>
  </div>
</template>

<style scoped>
.cyber-dog {
  position: fixed;
  font-size: 30px;
  pointer-events: none; /* Let clicks pass through to the buttons */
  z-index: 99998; /* Just under the paw cursor */
  transform: translate(-50%, -50%);
  transition: transform 0.2s; /* Smooth flipping */
}

/* Flip the emoji when moving left */
.cyber-dog.flip {
  transform: translate(-50%, -50%) scaleX(-1);
}

/* Add a digital neon shadow under the dog */
.glow {
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 5px;
  background: rgba(74, 222, 128, 0.6);
  border-radius: 50%;
  filter: blur(4px);
  z-index: -1;
}
</style>