<script setup>
// The loader component logic
</script>

<template>
  <div class="loader-container">
    <div class="cyber-ground"></div>
    <div class="sprout">
      <div class="stem"></div>
      <div class="leaf left-leaf"></div>
      <div class="leaf right-leaf"></div>
    </div>
    <p class="loading-text">INITIALIZING SYSTEM_ <span class="blink">|</span></p>
  </div>
</template>

<style scoped>
.loader-container {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  background-color: #050a0e; /* Deep dark cyber blue/black */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 10000;
}

/* The glowing ground line */
.cyber-ground {
  width: 150px;
  height: 2px;
  background: #4ade80;
  box-shadow: 0 0 15px #4ade80;
  position: relative;
  top: 60px;
}

/* Sprout animations */
.sprout {
  position: relative;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.stem {
  width: 4px;
  height: 0px;
  background-color: #4ade80;
  box-shadow: 0 0 10px #4ade80;
  animation: growStem 2s ease-in-out forwards;
}

.leaf {
  position: absolute;
  width: 15px;
  height: 15px;
  background-color: #4ade80;
  border-radius: 0 15px 0 15px;
  box-shadow: 0 0 10px #4ade80;
  opacity: 0;
  bottom: 30px;
}

.left-leaf {
  right: 50%;
  transform-origin: bottom right;
  animation: growLeafLeft 1s ease-in-out 1.5s forwards;
}

.right-leaf {
  left: 50%;
  transform: scaleX(-1);
  transform-origin: bottom left;
  animation: growLeafRight 1s ease-in-out 1.8s forwards;
}

.loading-text {
  margin-top: 80px;
  color: #4ade80;
  font-family: 'Courier New', monospace;
  letter-spacing: 3px;
  text-shadow: 0 0 8px rgba(74, 222, 128, 0.5);
}

.blink { animation: flash 1s infinite; }

@keyframes growStem {
  0% { height: 0px; }
  100% { height: 50px; }
}
@keyframes growLeafLeft {
  0% { opacity: 0; transform: scale(0) rotate(-20deg); }
  100% { opacity: 1; transform: scale(1) rotate(-45deg); }
}
@keyframes growLeafRight {
  0% { opacity: 0; transform: scaleX(-1) scale(0) rotate(-20deg); }
  100% { opacity: 1; transform: scaleX(-1) scale(1) rotate(-45deg); }
}
@keyframes flash {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
</style>