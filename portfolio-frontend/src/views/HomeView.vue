<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// ⚠️ IF YOU DON'T HAVE THIS FILE CREATED YET, ADD // IN FRONT OF THIS LINE:
import LifeGallery from '../components/LifeGallery.vue'; 

const showResume = ref(false);
const scrollY = ref(0);
let scrollInterval = null;

// Project Modal Logic
const activeProject = ref(null);
const openProject = (title, desc) => {
  activeProject.value = { title, desc };
};

// Capabilities Data
const capabilities = [
  { title: 'Cyber Security', desc: 'Forensics, Linux', icon: '🔐' },
  { title: 'Database Mgmt', desc: 'MySQL, PHP', icon: '🗄️' },
  { title: 'Creative Arts', desc: 'Photoshop, Procreate', icon: '🎨' },
  { title: 'Web Development', desc: 'HTML, CSS, JS, Vue', icon: '💻' },
  { title: 'Video Editing', desc: 'Premiere, CapCut', icon: '🎬' },
  { title: 'Hardware', desc: 'Arduino, Networking', icon: '🔌' }
];

// Quick Snaps / Lightbox Data
const albums = {
  'pets': ['/image/kel.jpg', '/image/pet2.jpg', '/image/tal.jpg'],
  'art': ['/image/draww.png'],
  'family': ['/image/family.jpg'],
  'hobbies': ['/image/shs.jpg'],
  'memories': ['/image/me.png']
};
const isLightboxOpen = ref(false);
const currentAlbum = ref([]);
const currentImgIndex = ref(0);

const openLightbox = (albumName) => {
  if(albums[albumName]) {
    currentAlbum.value = albums[albumName];
    currentImgIndex.value = 0;
    isLightboxOpen.value = true;
  }
};

const nextImage = () => { currentImgIndex.value = (currentImgIndex.value + 1) % currentAlbum.value.length; };
const prevImage = () => { currentImgIndex.value = (currentImgIndex.value - 1 + currentAlbum.value.length) % currentAlbum.value.length; };

// Weakness Button
const weaknessState = ref(0);
const weaknessBtnText = ref("View Weakness ⚠️");

const handleWeaknessClick = () => {
  if(weaknessState.value === 0) { weaknessBtnText.value = "👉 YOU"; weaknessState.value = 1; }
  else if(weaknessState.value === 1) { weaknessBtnText.value = "✖️ MATH"; weaknessState.value = 2; }
  else { weaknessBtnText.value = "View Weakness ⚠️"; weaknessState.value = 0; }
};

onMounted(() => {
  scrollInterval = setInterval(() => {
    scrollY.value -= 0.8; 
    if (scrollY.value < -540) scrollY.value = 0;
  }, 16); 
});

onUnmounted(() => {
  clearInterval(scrollInterval);
});
</script>

<template>
  <div class="home-view">
    
    <div v-if="isLightboxOpen" class="lightbox" @click="isLightboxOpen = false">
      <span class="close-btn sfx-trigger" @click="isLightboxOpen = false">&times;</span>
      <div class="lightbox-nav prev-btn sfx-trigger" @click.stop="prevImage"><i class="bi bi-chevron-left"></i></div>
      <img class="lightbox-content" :src="currentAlbum[currentImgIndex]" @click.stop />
      <div class="lightbox-nav next-btn sfx-trigger" @click.stop="nextImage"><i class="bi bi-chevron-right"></i></div>
      <div id="caption">Viewing Album</div>
      <div id="album-counter">{{ currentImgIndex + 1 }} / {{ currentAlbum.length }}</div>
    </div>

    <div v-if="activeProject" class="lightbox" @click="activeProject = null">
      <div class="modal-content" @click.stop>
        <span class="close-modal sfx-trigger" @click="activeProject = null">&times;</span>
        <h2>{{ activeProject.title }}</h2>
        <p class="mt-3">{{ activeProject.desc }}</p>
        <button class="btn-pill btn-fill mt-3 sfx-trigger" @click="activeProject = null">Close</button>
      </div>
    </div>

    <section class="hero-banner" id="hero">
      <div class="hero-text">
        <h1>Ma. Sofia Anne</h1>
        <p><strong>Future Military Cyber Specialist & Veterinarian</strong><br />"Practicality over passion, but passion always finds a way."</p>
        <button class="btn-pill btn-dark-fix sfx-trigger mt-3" @click="handleWeaknessClick">
          {{ weaknessBtnText }}
        </button>
      </div>
      
      <div class="hero-img-wrapper sfx-trigger">
        <img src="/image/me.png" alt="Active Character" class="char-light" />
        
        <img src="/img/mesleep.png" alt="Sleeping Character" class="char-dark" />
      </div>
    </section>

    <div class="resume-section" id="resume-section">
      <button class="resume-toggle-btn sfx-trigger" @click="showResume = !showResume">
        <i class="bi bi-file-earmark-person"></i> {{ showResume ? 'HIDE BIO' : 'VIEW FULL BIO & RESUME' }}
      </button>
      
      <transition name="expand">
        <div v-if="showResume" class="paper-sheet mt-3">
          <div class="paper-header">
            <h2>CURRICULUM VITAE</h2>
            <p>MA. SOFIA ANNE C. REVILLA</p>
          </div>
          <div class="paper-grid mt-3">
            <div class="resume-item">
              <span class="resume-label">Profile</span>
              <span class="resume-value">
                <strong>Age:</strong> 20 (April 26, 2005)<br />
                <strong>School:</strong> Asia Pacific College<br />
                <strong>Course:</strong> BSCS - Cybersecurity & Forensics
              </span>
            </div>
            <div class="resume-item">
              <span class="resume-label">Scholarship</span>
              <span class="resume-value">
                AFP-OLC Scholarship<br />
                (60% Armed Forces Scholarship)
              </span>
            </div>
            <div class="resume-item full-width">
              <span class="resume-label">Why This Course?</span>
              <div class="experience-box">
                "I chose practicality. Tech is in high demand, and I plan to join <strong>Military Cyber Operations</strong>. I originally wanted Veterinary Medicine, but found the ethical hacking specialization intriguing."
              </div>
            </div>
            <div class="resume-item full-width">
              <span class="resume-label">Experience</span>
              <div class="experience-box">
                <strong>Head of Arts Committee (2 Years)</strong><br />
                Clark Air Base Youth Club<br />
                <em>Led artistic initiatives, managed events, and coordinated youth activities.</em>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>

    <div class="dashboard-grid mt-5">
      <div class="about-card cyber-card" style="display: flex; flex-direction: column; justify-content: center;">
        <div class="section-header">About Me</div>
        <h3 class="title-blue" style="margin-bottom: 15px;">Aspiring Cyber Operations Specialist & Future Veterinarian</h3>
        <p style="line-height: 1.8; margin-bottom: 20px;">
          Driven 2nd-year Computer Science student specializing in Cybersecurity & Forensics at Asia Pacific College. My career path is defined by a unique duality: the precision of military cyber defense and the compassion of veterinary medicine.
        </p>
        <p style="line-height: 1.8; font-size: 0.9rem; color: var(--text-light);">
          I am dedicated to mastering Linux fundamentals, database management, and network security, with the ultimate goal of serving in military cyber operations.
        </p>
      </div>
      
      <div class="cap-card cyber-card" style="height: 350px; overflow: hidden; position: relative;">
        <h3 class="cap-title" style="margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 10px;">Capabilities</h3>
        <div class="scrolling-wrapper">
          <div class="scroll-content" :style="{ transform: 'translateY(' + scrollY + 'px)' }">
            <div v-for="(item, index) in capabilities" :key="index" class="cap-item sfx-trigger">
              <div class="cap-icon">{{ item.icon }}</div>
              <div><h4>{{ item.title }}</h4><small>{{ item.desc }}</small></div>
            </div>
            <div v-for="(item, index) in capabilities" :key="'dup'+index" class="cap-item sfx-trigger">
              <div class="cap-icon">{{ item.icon }}</div>
              <div><h4>{{ item.title }}</h4><small>{{ item.desc }}</small></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-header mt-5" id="projects">Projects</div>
    <div class="projects-grid">
      <div class="project-card sfx-trigger" @click="openProject('Face Track', 'Attendance face tracker for school used by LeanTech. Built with Python and OpenCV.')">
        <div class="p-icon"><i class="bi bi-person-bounding-box"></i></div>
        <h3>Face Track</h3><p>Attendance System</p>
      </div>
      <div class="project-card sfx-trigger" @click="openProject('TechZone DB', 'A complete Database Management System for inventory and sales. Built with MySQL and PHP.')">
        <div class="p-icon"><i class="bi bi-database"></i></div>
        <h3>TechZone DB</h3><p>Database Management</p>
      </div>
      <div class="project-card sfx-trigger" @click="openProject('Cyber Lab', 'Network Security Simulation and Packet Analysis project using Linux tools.')">
        <div class="p-icon"><i class="bi bi-shield-lock"></i></div>
        <h3>Cyber Lab</h3><p>Security Simulation</p>
      </div>
      <div class="project-card sfx-trigger" @click="openProject('Achievement Board', 'Coming Soon...')">
        <div class="p-icon"><i class="bi bi-trophy"></i></div>
        <h3>Achievement Board</h3><p>Future Module</p>
      </div>
    </div>

    <div class="dashboard-grid mt-5">
      <div class="polaroid-wrapper">
        <div class="section-header">Quick Snaps</div>
        <div class="polaroid-container">
          <div class="polaroid sfx-trigger" @click="openLightbox('pets')" style="--r:-3deg;"><img src="/image/kel.jpg" /><span>Fur Babies 🐾</span></div>
          <div class="polaroid sfx-trigger" @click="openLightbox('art')" style="--r:2deg;"><img src="/image/draww.png" /><span>Artworks 🎨</span></div>
          <div class="polaroid sfx-trigger" @click="openLightbox('family')" style="--r:-2deg;"><img src="/image/family.jpg" /><span>Family ❤️</span></div>
          <div class="polaroid sfx-trigger" @click="openLightbox('hobbies')" style="--r:4deg;"><img src="/image/shs.jpg" /><span>Hobbies 🔫</span></div>
          <div class="polaroid sfx-trigger" @click="openLightbox('memories')" style="--r:-4deg;"><img src="/image/me.png" /><span>Memories ✨</span></div>
        </div>
      </div>
      
      <div class="details-column">
        <div class="col-info">
          <div class="section-header">Goals</div>
          <div class="info-list">
            <div class="info-card sfx-trigger">
              <div class="info-img">🎯</div>
              <div class="info-content"><h4>Life Goal</h4><p>Financial stability for my family.</p></div>
            </div>
            <div class="info-card sfx-trigger">
              <div class="info-img">🐾</div>
              <div class="info-content"><h4>Dream</h4><p>Build a large animal rescue shelter.</p></div>
            </div>
            <div class="info-card sfx-trigger">
              <div class="info-img">🛡️</div>
              <div class="info-content"><h4>Career</h4><p>Military Cyber Operations.</p></div>
            </div>
          </div>
        </div>
        <div class="col-info mt-5">
          <div class="section-header">Hobbies</div>
          <div class="info-list">
            <div class="info-card sfx-trigger">
              <div class="info-img">☕</div>
              <div class="info-content"><h4>Exploration</h4><p>Cafe hopping & relaxing.</p></div>
            </div>
            <div class="info-card sfx-trigger">
              <div class="info-img">🔫</div>
              <div class="info-content"><h4>Shooting Range</h4><p>Target practice.</p></div>
            </div>
            <div class="info-card sfx-trigger">
              <div class="info-img">🎨</div>
              <div class="info-content"><h4>Arts</h4><p>Drawing, Painting & Design.</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="gallery-section" style="margin-top: 50px;">
      <LifeGallery />
    </div>

  </div>
</template>


<style scoped>
/* --- HERO BANNER --- */
.hero-banner {
  position: relative; 
  background-image: var(--hero-bg); 
  background-size: cover; 
  background-position: center;
  border-radius: 20px; 
  padding: 60px; 
  height: 380px; 
  display: flex; 
  align-items: center; 
  color: white; 
  margin-bottom: 20px; 
  box-shadow: 0 10px 40px rgba(0,0,0,0.2); 
  transition: background-image 0.5s ease;
  overflow: visible !important; 
}

:global(body.dark-mode) .hero-banner {
  background-image: var(--hero-bg-dark);
}

.hero-text { position: relative; z-index: 2; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }
.hero-text h1 { font-size: 3.5rem; }

.btn-dark-fix { background: transparent; border: 1px solid white; color: white; padding: 10px 20px; border-radius: 30px;}
:global(body.dark-mode) .btn-dark-fix { background: #333; border: 1px solid #555; }

/* --- OVERLAP IMAGE LOGIC --- */
.hero-img-wrapper { 
  position: absolute; 
  right: 50px; 
  bottom: 0px; 
  height: 145%; 
  z-index: 10; 
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.4s; 
}

.hero-img-wrapper:hover {
  transform: scale(1.05) translateY(-10px);
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.7));
}

:global(body.dark-mode) .hero-img-wrapper:hover {
  filter: drop-shadow(0 0 20px rgba(108, 138, 241, 0.6)); 
}

.hero-img-wrapper img { 
  position: absolute; 
  bottom: 0; 
  right: 0; 
  height: 100%; 
  object-fit: contain; 
  transform-origin: bottom center; 
  transition: opacity 0.5s ease; 
}

/* Base states for images before Dark Mode overrides them */
.char-light { opacity: 1; pointer-events: auto; }
.char-dark { opacity: 0; pointer-events: none; }

/* --- RESUME & PAPER SHEET --- */
.resume-toggle-btn { width: 100%; background: transparent; color: var(--primary-blue); padding: 15px; border-radius: 20px; border: 2px dashed var(--primary-blue); font-weight: bold; transition: 0.3s; }
.resume-toggle-btn:hover { background: var(--primary-blue); color: white; border-style: solid; }
:global(body.dark-mode) .resume-toggle-btn { background: var(--card-white); border: 1px dashed var(--primary-blue); color: var(--primary-blue); box-shadow: none; }

.paper-sheet { background: #fdfbf7; color: #333; padding: 40px; border-left: 5px solid #d14444; font-family: 'Courier New', monospace; margin-top: 15px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
:global(body.dark-mode) .paper-sheet { background-color: #1e1e1e; color: #ccc; border-left: 5px solid #6c8af1; }

.paper-header h2 { margin-bottom: 5px; font-weight: bold; letter-spacing: 1px; }
.paper-header p { font-weight: bold; color: #555; }
:global(body.dark-mode) .paper-header p { color: #aaa; }

.paper-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.resume-item { display: flex; flex-direction: column; }
.full-width { grid-column: 1 / -1; }
.resume-label { font-weight: bold; color: #d14444; margin-bottom: 5px; text-transform: uppercase; font-size: 0.9rem; border-bottom: 1px solid #ddd; padding-bottom: 5px;}
:global(body.dark-mode) .resume-label { color: #6c8af1; border-bottom: 1px solid #333;}
.resume-value { font-size: 0.95rem; line-height: 1.6; }

.experience-box { background: rgba(0,0,0,0.03); padding: 15px; border-radius: 8px; font-size: 0.95rem; line-height: 1.6; }
:global(body.dark-mode) .experience-box { background: rgba(255,255,255,0.05); }

/* --- GLOBAL CARD STYLING FOR DARK MODE --- */
.cyber-card { background: var(--card-white); padding: 40px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }
:global(body.dark-mode) .cyber-card,
:global(body.dark-mode) .project-card,
:global(body.dark-mode) .info-card { background: var(--card-white); color: var(--text-main); border-radius: 15px; border: none; box-shadow: none; }

.title-blue { color: var(--primary-blue); }
:global(body.dark-mode) h3, :global(body.dark-mode) h4 { color: var(--text-main); }
:global(body.dark-mode) .title-blue { color: var(--primary-blue) !important; }

.dashboard-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 30px; }
.section-header { font-size: 1.2rem; font-weight: bold; margin-bottom: 20px; color: var(--text-main); }

/* --- CAPABILITIES SECTION --- */
.cap-card { background: var(--primary-dark); color: white; }
.cap-title { color: white; }
:global(body.dark-mode) .cap-title { color: var(--text-main); border-bottom: 1px solid #444 !important; }

.scrolling-wrapper { height: 100%; overflow: hidden; position: relative; }
.scroll-content { display: flex; flex-direction: column; gap: 15px; }
.cap-item { display: flex; gap: 15px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 12px; transition: 0.3s; align-items: center; }
.cap-icon { font-size: 1.8rem; background: rgba(255,255,255,0.2); width: 45px; height: 45px; border-radius: 10px; display: flex; align-items: center; justify-content: center; }
:global(body.dark-mode) .cap-item { background: #333333; border: 1px solid #3d3d3d; }
:global(body.dark-mode) .cap-icon { background: #444444; }

/* --- PROJECTS GRID --- */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
.project-card { background: white; padding: 25px; border-radius: 15px; text-align: center; transition: 0.3s; border: 1px solid transparent; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; }
.project-card:hover { transform: translateY(-5px); border-color: var(--primary-blue); }
.p-icon { font-size: 2rem; color: var(--primary-blue); margin-bottom: 10px; }
:global(body.dark-mode) .project-card p { color: var(--text-light); font-size: 0.85rem; }

/* --- POLAROIDS --- */
.polaroid-container { display: flex; flex-wrap: wrap; gap: 20px; }
.polaroid { background: white; padding: 10px 10px 40px; width: 140px; box-shadow: 5px 8px 15px rgba(0,0,0,0.2); transform: rotate(var(--r)); transition: 0.3s; position: relative; cursor: pointer; }
.polaroid:hover { transform: scale(1.1) rotate(0deg); z-index: 10;}
.polaroid img { width: 100%; height: 120px; object-fit: cover; }
.polaroid span { position: absolute; bottom: 10px; left: 0; width: 100%; text-align: center; color: black; font-family: 'Courier New'; font-weight: bold; font-size: 0.9rem;}
:global(body.dark-mode) .polaroid { background: var(--card-white); border: 1px solid #333; box-shadow: none; }
:global(body.dark-mode) .polaroid span { color: var(--text-main); }

/* --- INFO LIST (Goals & Hobbies) --- */
.info-list { display: flex; flex-direction: column; gap: 15px; }
.info-card { background: white; padding: 20px; border-radius: 15px; display: flex; gap: 15px; align-items: center; transition: 0.3s; border: 1px solid transparent; }
.info-card:hover { transform: translateX(5px); border-color: var(--primary-blue); }
.info-img { width: 50px; height: 50px; background: #eef2ff; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;}
.info-content h4 { margin: 0; font-size: 1rem; }
.info-content p { margin: 5px 0 0 0; font-size: 0.85rem; color: #555;}
:global(body.dark-mode) .info-img { background: #333333; }
:global(body.dark-mode) .info-content p { color: var(--text-light); }

/* --- LIGHTBOX & MODALS --- */
.lightbox { display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 100000; justify-content: center; align-items: center; flex-direction: column; backdrop-filter: blur(5px); }
.lightbox-content { max-width: 90%; max-height: 70vh; object-fit: contain; border-radius: 10px; box-shadow: 0 0 50px rgba(255,255,255,0.1); animation: zoom 0.3s; }
.close-btn, .close-modal { position: absolute; top: 20px; right: 30px; font-size: 40px; color: white; cursor: pointer; transition: 0.3s; }
.close-btn:hover, .close-modal:hover { color: var(--primary-blue); transform: scale(1.1); }
.lightbox-nav { position: absolute; top: 50%; color: white; font-size: 3rem; cursor: pointer; transition: 0.3s; padding: 20px; }
.lightbox-nav:hover { color: var(--primary-blue); transform: scale(1.2); }
.prev-btn { left: 20px; }
.next-btn { right: 20px; }
#caption, #album-counter { color: #ccc; margin-top: 15px; font-family: 'Courier New', monospace; font-size: 1.2rem; }

.modal-content { background: var(--card-white); padding: 40px; border-radius: 20px; max-width: 500px; width: 90%; text-align: center; color: var(--text-main); position: relative; box-shadow: 0 10px 40px rgba(0,0,0,0.2); animation: zoom 0.3s ease; }
:global(body.dark-mode) .modal-content { background: #242424; color: white;}
:global(body.dark-mode) .close-modal { color: white; }

.mt-3 { margin-top: 15px; }
.mt-5 { margin-top: 40px; }

@keyframes zoom { from {transform:scale(0.9); opacity:0;} to {transform:scale(1); opacity:1;} }
.expand-enter-active, .expand-leave-active { transition: all 0.5s ease; max-height: 800px; overflow: hidden; opacity: 1; }
.expand-enter-from, .expand-leave-to { max-height: 0; opacity: 0; margin-top: 0; padding-top: 0; padding-bottom: 0; border: none; }
</style>

<style>
body.dark-mode .char-light {
  opacity: 0 !important;
  pointer-events: none !important;
}

body.dark-mode .char-dark {
  opacity: 1 !important;
  pointer-events: auto !important;
  
  /* The breathing animation only applies to the Dark image now.
    It uses 'scale' instead of 'translateY' so it does NOT shift the whole page. 
  */
  animation: sleepingBreath 4s infinite ease-in-out !important; 
}

@keyframes sleepingBreath {
  0%, 100% { transform: scale(1); filter: brightness(0.9) drop-shadow(0 0 10px rgba(0,0,0,0.5)); }
  50% { transform: scale(0.98); filter: brightness(1) drop-shadow(0 0 15px rgba(108, 138, 241, 0.5)); }
}
</style>