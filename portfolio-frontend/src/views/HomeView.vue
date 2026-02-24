<script setup>
import { onMounted } from 'vue';
import gsap from 'gsap';

onMounted(() => {
  // Add a futuristic staggered fade-in effect when the page loads
  gsap.from(".cyber-card", {
    y: 50,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: "power3.out",
    delay: 3.5 // Waits for the Sprout loader to finish
  });
});
</script>

<template>
  <div class="home-container">
    <div class="profile-header cyber-card">
      <h1 class="glitch" data-text="Ma. Sofia Anne">Ma. Sofia Anne</h1>
      <h3 class="subtitle">Military Cyber Operations & Veterinary Dreamer</h3>
      <p class="scholar-badge">🛡️ AFP-OLC Scholar | BSCS Cybersecurity & Forensics</p>
    </div>

    <div class="grid-layout">
      <div class="cyber-card bio-card">
        <h2><span class="icon">🌿</span> The Mission</h2>
        <p>
          I am driven by a unique duality: the precise, analytical world of military cyber defense, and the compassionate calling of animal rescue. My ultimate goal is to build a large-scale animal shelter while ensuring digital security on a national level.
        </p>
        <p class="quote">"Practicality over passion, but passion always finds a way."</p>
      </div>

      <div class="cyber-card tech-card">
        <h2><span class="icon">💻</span> Tech Stack</h2>
        <ul class="skills-list">
          <li>Python & OpenCV</li>
          <li>Vue.js & HTML/CSS</li>
          <li>Linux & Network Security</li>
          <li>MySQL & Supabase</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
}

.cyber-card {
  background: rgba(16, 25, 33, 0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(74, 222, 128, 0.2);
  border-left: 4px solid #4ade80;
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s ease;
}

.cyber-card:hover {
  transform: translateY(-5px);
  border-color: rgba(74, 222, 128, 0.6);
  box-shadow: 0 10px 40px rgba(74, 222, 128, 0.1);
}

.profile-header {
  text-align: center;
  border-left: none;
  border-top: 4px solid #4ade80;
}

.glitch {
  font-size: 3.5rem;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 4px;
  text-shadow: 0 0 10px rgba(74, 222, 128, 0.5);
  margin-bottom: 10px;
}

.subtitle {
  color: #4ade80;
  font-family: 'Courier New', Courier, monospace;
  font-weight: normal;
  letter-spacing: 2px;
}

.scholar-badge {
  display: inline-block;
  margin-top: 15px;
  padding: 8px 16px;
  background: rgba(74, 222, 128, 0.1);
  border: 1px solid #4ade80;
  border-radius: 20px;
  font-size: 0.9rem;
}

.grid-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
}

.icon {
  margin-right: 10px;
}

h2 {
  color: #fff;
  margin-bottom: 20px;
  font-family: 'Courier New', Courier, monospace;
}

p {
  line-height: 1.8;
  color: #b0c4de;
  margin-bottom: 15px;
}

.quote {
  font-style: italic;
  color: #4ade80;
  opacity: 0.8;
  border-left: 2px solid #4ade80;
  padding-left: 15px;
}

.skills-list {
  list-style: none;
  padding: 0;
}

.skills-list li {
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  color: #b0c4de;
}

.skills-list li::before {
  content: '>';
  color: #4ade80;
  margin-right: 10px;
  font-weight: bold;
}

@media (max-width: 768px) {
  .grid-layout {
    grid-template-columns: 1fr;
  }
}
</style>