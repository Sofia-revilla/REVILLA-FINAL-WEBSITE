<script setup>
import { ref, onMounted } from 'vue';

// ==========================================
// 🌟 SUPABASE CONFIGURATION 🌟
// Paste your URL and ANON KEY below:
// ==========================================
const SUPABASE_URL = 'YOUR_SUPABASE_URL_HERE'; 
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY_HERE';

const messages = ref([]);
const newName = ref('');
const newMessage = ref('');
const isSubmitting = ref(false);
const plantedType = ref(null);

const headers = {
  'apikey': SUPABASE_ANON_KEY,
  'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
  'Content-Type': 'application/json',
  'Prefer': 'return=representation'
};

// GET: Fetch messages from Supabase
const fetchMessages = async () => {
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/guestbook?select=*&order=created_at.desc`, { headers });
    if (!res.ok) throw new Error("Failed to fetch");
    const data = await res.json();
    messages.value = data;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
};

// POST: Send new message & Instant Update with "Pop Under"
const plantMessage = async (type) => {
  if (!newMessage.value) {
    alert("Please write a message before planting!");
    return;
  }
  
  isSubmitting.value = true;
  
  // 1. INSTANT UI UPDATE
  const tempMsg = {
    id: Date.now(),
    name: newName.value || 'Anonymous Traveler',
    message: newMessage.value,
    sticker: type,
    created_at: new Date().toISOString()
  };
  
  // Instantly add to the top of the list so it "Pops Under" the input box
  messages.value.unshift(tempMsg); 
  plantedType.value = type;

  try {
    // 2. Sync to Supabase Database
    await fetch(`${SUPABASE_URL}/rest/v1/guestbook`, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify({ 
        name: tempMsg.name, 
        message: tempMsg.message, 
        sticker: tempMsg.sticker 
      })
    });

    // Clear inputs
    newName.value = '';
    newMessage.value = '';
    
    // Hide success overlay after 3 seconds
    setTimeout(() => { plantedType.value = null; }, 3000);
    
  } catch (e) {
    console.error("Planting failed:", e);
    // If it fails to save, remove it from the list
    messages.value.shift(); 
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(() => {
  fetchMessages();
});
</script>

<template>
  <div class="guestbook-view">
    
    <div class="nav-back">
      <RouterLink to="/" class="back-btn sfx-trigger">
        <i class="bi bi-arrow-left"></i> Back to Profile
      </RouterLink>
    </div>

    <div class="forest-header">
      <h1 class="glitch-green">Cyber Forest Logs</h1>
      <p class="subtitle">Your message helps this digital ecosystem grow.</p>
    </div>

    <div class="input-card shadow-forest cyber-card">
      <div class="input-group">
        <label>Identity</label>
        <input v-model="newName" placeholder="User-XXXX" class="forest-input sfx-trigger">
      </div>
      
      <div class="input-group">
        <label>Data String</label>
        <textarea v-model="newMessage" placeholder="Write your message here..." class="forest-input text-area sfx-trigger"></textarea>
      </div>

      <div class="sticker-tray">
        <p class="tray-label">Select a seed to plant your message:</p>
        <div class="sticker-options">
          <button class="sticker-btn sfx-trigger" :disabled="isSubmitting" @click="plantMessage('leaf')">
            <span class="emoji">🍃</span><span class="label">Leaf</span>
          </button>
          <button class="sticker-btn sfx-trigger" :disabled="isSubmitting" @click="plantMessage('paw')">
            <span class="emoji">🐾</span><span class="label">Paw</span>
          </button>
          <button class="sticker-btn sfx-trigger" :disabled="isSubmitting" @click="plantMessage('tree')">
            <span class="emoji">🌳</span><span class="label">Tree</span>
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

    <TransitionGroup name="pop-list" tag="div" class="logs-container">
      
      <div v-if="messages.length === 0" key="empty" class="empty-state">No traces found yet. Be the first.</div>
      
      <div v-for="msg in messages" :key="msg.id" class="leaf-comment cyber-card">
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

    </TransitionGroup>
  </div>
</template>

<style scoped>
.guestbook-view { max-width: 800px; margin: 0 auto; padding-top: 20px; padding-bottom: 100px; }

/* Back Button */
.nav-back { margin-bottom: 30px; }
.back-btn { 
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--card-white); color: var(--primary-blue); 
  padding: 10px 20px; border-radius: 30px; text-decoration: none; font-weight: bold;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: 0.3s; border: 1px solid transparent;
}
.back-btn:hover { background: var(--primary-blue); color: white; transform: translateX(-5px); }
:global(body.dark-mode) .back-btn { background: #242424; border-color: var(--primary-blue); color: var(--primary-blue); }
:global(body.dark-mode) .back-btn:hover { background: var(--primary-blue); color: white; box-shadow: 0 0 15px rgba(108, 138, 241, 0.5);}

/* Header */
.forest-header { text-align: center; margin-bottom: 40px; }
.glitch-green { font-family: 'Courier New', monospace; color: #22c55e; font-size: 2.8rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;}
:global(body.dark-mode) .glitch-green { text-shadow: 0 0 15px rgba(34, 197, 94, 0.6); } /* Extra glow in dark mode */
.subtitle { color: var(--text-light); }

/* Input Card */
.input-card { background: var(--card-white); border-radius: 28px; padding: 35px; position: relative; overflow: hidden; }
:global(body.dark-mode) .input-card { 
  background: #1e1e1e !important; 
  border: 1px solid #22c55e !important; 
  box-shadow: 0 0 30px rgba(34, 197, 94, 0.15) !important; 
}

.input-group label { display: block; font-size: 0.8rem; font-weight: 800; text-transform: uppercase; color: #16a34a; margin-bottom: 8px; }
:global(body.dark-mode) .input-group label { color: #4ade80; }

.forest-input { width: 100%; background: var(--bg-color); border: 2px solid transparent; padding: 15px; border-radius: 12px; margin-bottom: 20px; transition: 0.3s; color: var(--text-main); font-family: inherit;}
.forest-input:focus { border-color: #22c55e; outline: none; }
:global(body.dark-mode) .forest-input { background: #111; color: white; border: 1px solid #333; }
:global(body.dark-mode) .forest-input:focus { border-color: #4ade80; box-shadow: 0 0 15px rgba(34, 197, 94, 0.3); }
.text-area { min-height: 120px; resize: vertical; }

.sticker-tray { padding-top: 20px; border-top: 1px dashed var(--text-light); }
.tray-label { font-size: 0.9rem; color: var(--text-light); margin-bottom: 15px; }
.sticker-options { display: flex; gap: 15px; }
.sticker-btn { flex: 1; display: flex; flex-direction: column; align-items: center; padding: 15px; background: var(--bg-color); border: 2px solid transparent; border-radius: 16px; transition: 0.3s; cursor: pointer; }
.sticker-btn .emoji { font-size: 2rem; margin-bottom: 5px; }
.sticker-btn .label { font-size: 0.85rem; font-weight: bold; color: var(--text-main); }
.sticker-btn:hover { background: rgba(34, 197, 94, 0.1); border-color: #22c55e; transform: translateY(-5px); }

:global(body.dark-mode) .sticker-btn { background: #111; border: 1px solid #333; }
:global(body.dark-mode) .sticker-btn .label { color: #ccc; }
:global(body.dark-mode) .sticker-btn:hover { background: rgba(34, 197, 94, 0.15); border-color: #4ade80; box-shadow: 0 0 15px rgba(34, 197, 94, 0.4); }

.success-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(34, 197, 94, 0.95); display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; z-index: 10; backdrop-filter: blur(5px);}
.success-icon { font-size: 5rem; animation: growShrink 1s infinite; }

@keyframes growShrink { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.2); } }

/* 🍃 MESSAGES LIST & POP ANIMATION 🍃 */
.logs-container { margin-top: 40px; display: flex; flex-direction: column; gap: 25px;}
.empty-state { text-align: center; color: var(--text-light); font-style: italic; }

/* The Pop Under Animation */
.pop-list-enter-active,
.pop-list-leave-active {
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.pop-list-enter-from {
  opacity: 0;
  transform: translateY(-40px) scale(0.9);
}
.pop-list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.9);
}

.leaf-comment {
  background: var(--card-white);
  padding: 25px 30px;
  /* Looks like a leaf */
  border-radius: 0 40px 0 40px; 
  border-left: 6px solid #22c55e;
  position: relative;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
}
.leaf-comment:hover { transform: translateX(10px) scale(1.02); border-color: #4ade80;}

:global(body.dark-mode) .leaf-comment {
  background: #1e1e1e !important;
  border-left: 6px solid #4ade80 !important;
  border-top: 1px solid #333;
  border-right: 1px solid #333;
  border-bottom: 1px solid #333;
  box-shadow: 0 5px 20px rgba(0,0,0,0.3) !important;
}

.sticker-tag { position: absolute; top: -15px; right: 25px; background: white; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; border-radius: 50%; box-shadow: 0 5px 15px rgba(0,0,0,0.1); font-size: 1.5rem; border: 2px solid #22c55e;}
:global(body.dark-mode) .sticker-tag { background: #111; border-color: #4ade80; box-shadow: 0 0 15px rgba(74, 222, 128, 0.4);}

.user-name { color: var(--text-main); font-weight: 800; font-size: 1.1rem;}
.msg-body { color: var(--text-main); margin: 10px 0; line-height: 1.6; font-size: 0.95rem; opacity: 0.9;}
.timestamp { font-size: 0.8rem; color: var(--text-light); }
</style>