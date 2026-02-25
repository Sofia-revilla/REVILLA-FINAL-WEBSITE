<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import * as THREE from 'three';
import gsap from 'gsap';

const containerRef = ref(null);
const currentTitle = ref('Loading...');
const currentArtist = ref('MEMORIES');

// Added the missing 'tal.jpg' image back to the array
const images = [
  { url: '/image/pet2.jpg', title: 'Happiness', artist: 'MY PETS' },
  { url: '/image/draww.png', title: 'Creativity', artist: 'ARTWORKS' },
  { url: '/image/family.jpg', title: 'Support', artist: 'FAMILY' },
  { url: '/image/kel.jpg', title: 'Twinkel', artist: 'FUR BABY' },
  { url: '/image/shs.jpg', title: 'Memories', artist: 'SCHOOL DAYS' },
  { url: '/image/tal.jpg', title: 'Talia', artist: 'COMPANION' }
];

let scene, camera, renderer, material;
let currentIdx = 0;
let isAnimating = false;
let intervalId = null;
let animationFrameId = null;

// Extracted nextSlide so it can be called by clicking the container
const nextSlide = () => {
  if (isAnimating) return;
  isAnimating = true;

  const nextIdx = (currentIdx + 1) % images.length;
  material.uniforms.texture2.value = textures[nextIdx];

  gsap.to(material.uniforms.dispFactor, {
    value: 1, duration: 1.5, ease: "expo.inOut",
    onComplete: () => {
      material.uniforms.texture1.value = textures[nextIdx];
      material.uniforms.dispFactor.value = 0;
      currentIdx = nextIdx;
      currentTitle.value = images[nextIdx].title;
      currentArtist.value = images[nextIdx].artist;
      isAnimating = false;
    }
  });
};

// We need to keep textures globally accessible in this scope for nextSlide
let textures = [];

onMounted(() => {
  if (!containerRef.value) return;

  scene = new THREE.Scene();
  camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  
  const width = containerRef.value.offsetWidth;
  const height = containerRef.value.offsetHeight;
  renderer.setSize(width, height);
  containerRef.value.appendChild(renderer.domElement);

  const loader = new THREE.TextureLoader();
  textures = images.map(img => loader.load(img.url));

  const vertexShader = `varying vec2 vUv; void main() { vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
  const fragmentShader = `
    varying vec2 vUv;
    uniform sampler2D texture1;
    uniform sampler2D texture2;
    uniform float dispFactor;
    void main() {
      vec2 uv = vUv;
      vec2 dist1 = vec2(uv.x + dispFactor * (sin(uv.y * 10.0 + dispFactor) * 0.1), uv.y);
      vec2 dist2 = vec2(uv.x - (1.0 - dispFactor) * (sin(uv.y * 10.0 + dispFactor) * 0.1), uv.y);
      gl_FragColor = mix(texture2D(texture1, dist1), texture2D(texture2, dist2), dispFactor);
    }
  `;

  material = new THREE.ShaderMaterial({
    uniforms: {
      dispFactor: { value: 0.0 },
      texture1: { value: textures[0] },
      texture2: { value: textures[1] }
    },
    vertexShader, fragmentShader, transparent: true
  });

  const mesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
  scene.add(mesh);

  currentTitle.value = images[0].title;
  currentArtist.value = images[0].artist;

  // Set the 5-second interval
  intervalId = setInterval(nextSlide, 5000);

  const animate = () => {
    animationFrameId = requestAnimationFrame(animate);
    renderer.render(scene, camera);
  };
  animate();

  window.addEventListener('resize', handleResize);
});

const handleResize = () => {
  if (containerRef.value && renderer) {
    renderer.setSize(containerRef.value.offsetWidth, containerRef.value.offsetHeight);
  }
};

onUnmounted(() => {
  clearInterval(intervalId);
  cancelAnimationFrame(animationFrameId);
  window.removeEventListener('resize', handleResize);
  if (renderer) renderer.dispose();
});
</script>

<template>
  <div class="col-gallery-wide centered-gallery">
    <div class="section-header">Life Gallery <small style="opacity: 0.6; font-weight: normal;">(Landscape Mode)</small></div>
    
    <div ref="containerRef" class="art-container sfx-trigger" @click="nextSlide" style="cursor: pointer;">
      <div class="art-ui">
        <h2>{{ currentTitle }}</h2>
        <p>{{ currentArtist }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.centered-gallery { width: 100%; display: flex; flex-direction: column; align-items: center; margin-top: 50px; margin-bottom: 50px; }
.section-header { font-size: 1.2rem; font-weight: bold; margin-bottom: 20px; color: var(--text-main); }

.art-container {
  position: relative; width: 100%; max-width: 800px; height: 450px;
  border-radius: 20px; overflow: hidden; background-color: #000;
  box-shadow: 0 15px 50px rgba(0,0,0,0.3);
  transition: transform 0.3s ease;
}

/* Optional: Slight hover effect to indicate it's clickable */
.art-container:hover {
  transform: scale(1.02);
}

.art-ui {
  position: absolute; bottom: 30px; left: 30px; color: white;
  z-index: 10; pointer-events: none; text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}
.art-ui h2 { font-size: 2rem; margin: 0; letter-spacing: 2px; text-transform: uppercase; }
.art-ui p { font-size: 0.8rem; font-weight: 600; letter-spacing: 4px; color: #4ade80; margin-top: 5px; }

@media (max-width: 768px) {
  .art-container { height: 300px; }
  .art-ui h2 { font-size: 1.5rem; }
}
</style>