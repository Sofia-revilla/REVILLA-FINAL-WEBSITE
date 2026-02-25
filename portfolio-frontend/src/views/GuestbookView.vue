<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import gsap from 'gsap';

const messages = ref([]);
const newName = ref('');
const newMessage = ref('');
const isSubmitting = ref(false);

// State for the "Planting" success
const plantedType = ref(null); 

const API_URL = 'YOUR_BACKEND_URL';

const fetchMessages = async () => {
  try {
    const response = await axios.get(API_URL);
    messages.value = response.data;
  } catch (e) { console.error(e); }
};

// Updated: Submit now accepts a "type" (leaf, paw, or tree)
const plantMessage = async (type) => {
  if (!newMessage.value) {
    alert("Please write a message before planting!");
    return;
  }
  
  isSubmitting.value = true;
  try {
    await axios.post(API_URL, { 
      name: newName.value || 'Anonymous Traveler', 
      message: newMessage.value,
      sticker: type // You can save the sticker type in your DB
    });

    plantedType.value = type;
    
    // Clear inputs
    newName.value = '';
    newMessage.value = '';
    
    // Refresh and Animate
    await fetchMessages();
    
    // GSAP: Make the new leaf fall from the top
    gsap.from(".leaf-comment:first-child", { 
      y: -100, 
      rotation: 25, 
      opacity: 0, 
      duration: 1.2, 
      ease: "bounce.out" 
    });

    // Reset the "Planted" state after 3 seconds
    setTimeout(() => { plantedType.value = null; }, 3000);
    
  } catch (e) {
    console.error("Planting failed:", e);
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(fetchMessages);
</script>

<template>
  <div class="guestbook-view">
    <div class="forest-header">
      <h1 class="glitch-green">Cyber Forest Logs</h1>
      <p class="subtitle">Your message helps this digital ecosystem grow.</p>
    </div>

    <div class="input-card shadow-forest">
      <div class="input-group">
        <label>Identity</label>
        <input v-model="newName" placeholder="User-XXXX" class="forest-input">
      </div>
      
      <div class="input-group">
        <label>Data String</label>
        <textarea v-model="newMessage" placeholder="Write your message here..." class="forest-input text-area"></textarea>
      </div>

      <div class="sticker-tray">
        <p class="tray-label">Select a seed to plant your message:</p>
        <div class="sticker-options">
          <button 
            class="sticker-btn sfx-trigger" 
            :disabled="isSubmitting"
            @click="plantMessage('leaf')"
            title="Plant a Leaf"
          >
            <span class="emoji">🍃</span>
            <span class="label">Leaf</span>
          </button>

          <button 
            class="sticker-btn sfx-trigger" 
            :disabled="isSubmitting"
            @click="plantMessage('paw')"
            title="Leave a Paw Print"
          >
            <span class="emoji">🐾</span>
            <span class="label">Paw</span>
          </button>

          <button 
            class="sticker-btn sfx-trigger" 
            :disabled="isSubmitting"
            @click="plantMessage('tree')"
            title="Grow a Tree"
          >
            <span class="emoji">🌳</span>
            <span class="label">Tree</span>
          </button>
        </div>
      </div>

      <transition name="grow">
        <div v-if="plantedType" class="success-overlay">
          <div class="success-icon">
            <span v-if="plantedType === 'leaf'">🍃</span>
            <span v-if="plantedType === 'paw'">🐾</span>
            <span v-if="plantedType === 'tree'">🌳</span>
          </div>
          <h3>Success! Message Planted.</h3>
        </div>
      </transition>
    </div>

    <div class="logs-container">
      <div v-for="msg in messages" :key="msg.id" class="leaf-comment">
        <div class="sticker-tag" v-if="msg.sticker">
          {{ msg.sticker === 'leaf' ? '🍃' : msg.sticker === 'paw' ? '🐾' : '🌳' }}
        </div>
        <div class="content">
          <h4 class="user-name">{{ msg.name }}</h4>
          <p class="msg-body">{{ msg.message }}</p>
          <div class="meta">
            <span class="timestamp">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Header Styling */
.glitch-green {
  font-family: 'Courier New', monospace;
  color: #22c55e;
  font-size: 2.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.shadow-forest {
  box-shadow: 0 20px 40px rgba(34, 197, 94, 0.1);
}

.input-card {
  background: white;
  border-radius: 28px;
  padding: 35px;
  border: 1px solid #e2e8f0;
  position: relative;
  overflow: hidden;
}

.input-group label {
  display: block;
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  color: #16a34a;
  margin-bottom: 8px;
  letter-spacing: 1px;
}

.forest-input {
  width: 100%;
  background: #f8fafc;
  border: 2px solid transparent;
  padding: 14px;
  border-radius: 12px;
  margin-bottom: 20px;
  transition: 0.3s;
}

.forest-input:focus {
  border-color: #22c55e;
  background: white;
  outline: none;
}

/* Sticker Tray UI */
.sticker-tray {
  margin-top: 10px;
  padding-top: 20px;
  border-top: 1px dashed #cbd5e1;
}

.tray-label {
  font-size: 0.9rem;
  color: #64748b;
  margin-bottom: 15px;
}

.sticker-options {
  display: flex;
  gap: 15px;
}

.sticker-btn {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px;
  background: #f1f5f9;
  border: 2px solid transparent;
  border-radius: 16px;
  transition: 0.3s;
  cursor: none; /* Uses your paw cursor */
}

.sticker-btn .emoji { font-size: 1.8rem; margin-bottom: 5px; }
.sticker-btn .label { font-size: 0.8rem; font-weight: 600; color: #475569; }

.sticker-btn:hover {
  background: #f0fdf4;
  border-color: #22c55e;
  transform: translateY(-5px);
}

.sticker-btn:active { transform: scale(0.95); }

/* Success Overlay */
.success-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(34, 197, 94, 0.95);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  z-index: 10;
}

.success-icon { font-size: 4rem; animation: growShrink 1s infinite; }

@keyframes growShrink {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

/* Comments */
.leaf-comment {
  background: white;
  margin-top: 25px;
  padding: 25px;
  border-radius: 20px;
  border-left: 6px solid #22c55e;
  position: relative;
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.sticker-tag {
  position: absolute;
  top: -12px;
  right: 20px;
  background: white;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  font-size: 1.2rem;
}

.user-name { color: #1e293b; font-weight: 700; }
.msg-body { color: #475569; margin: 10px 0; line-height: 1.6; }
.timestamp { font-size: 0.75rem; color: #94a3b8; }
</style>