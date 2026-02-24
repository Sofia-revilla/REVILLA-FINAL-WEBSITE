<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import gsap from 'gsap';

// State variables
const messages = ref([]);
const newName = ref('');
const newMessage = ref('');
const isSubmitting = ref(false);
const showBark = ref(false);

// Your Flask Backend URL
const API_URL = 'https://sofia-portfolio-backend.onrender.com/api/messages';

// GET Method: Fetch comments from the backend
const fetchMessages = async () => {
  try {
    const response = await axios.get(API_URL);
    messages.value = response.data;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
};

// POST Method: Send a new comment to the backend
const submitMessage = async () => {
  if (!newMessage.value) return;
  isSubmitting.value = true;
  
  try {
    await axios.post(API_URL, {
      name: newName.value || 'Anonymous',
      message: newMessage.value
    });
    
    // Trigger the interactive Dog Bark!
    showBark.value = true;
    setTimeout(() => showBark.value = false, 2000);

    // Clear the input fields
    newName.value = '';
    newMessage.value = '';

    // Refetch messages to get the new one
    await fetchMessages();

    // GSAP Animation: Make the newest comment drop in like a leaf
    setTimeout(() => {
      gsap.from(".leaf-comment:first-child", {
        y: -50,
        opacity: 0,
        rotation: 15,
        duration: 1,
        ease: "bounce.out"
      });
    }, 100);

  } catch (error) {
    console.error("Error submitting message:", error);
  } finally {
    isSubmitting.value = false;
  }
};

// Fetch messages immediately when the page loads
onMounted(() => {
  fetchMessages();
});
</script>

<template>
  <div class="guestbook-container">
    <div class="header">
      <h1 class="glitch" data-text="Terminal Log">Terminal Log</h1>
      <p class="subtitle">Leave a trace in the cyber-forest.</p>
    </div>
    
    <div class="input-section cyber-card">
      <input 
        v-model="newName" 
        type="text" 
        placeholder="Enter Designation (Name)" 
        class="cyber-input" 
      />
      <textarea 
        v-model="newMessage" 
        placeholder="Plant your message here..." 
        class="cyber-input textarea"
      ></textarea>
      
      <button @click="submitMessage" :disabled="isSubmitting" class="cyber-btn">
        {{ isSubmitting ? 'UPLOADING...' : 'DROP LEAF 🍃' }}
      </button>

      <transition name="bark-fade">
        <div v-if="showBark" class="bark-alert">
          🐕 WOOF! HI! Data planted successfully!
        </div>
      </transition>
    </div>

    <div class="comments-section">
      <div v-if="messages.length === 0" class="empty-state">No traces found yet. Be the first.</div>
      
      <transition-group name="list">
        <div v-for="msg in messages" :key="msg.id" class="leaf-comment cyber-card">
          <div class="leaf-deco"></div>
          <div class="comment-content">
            <h4 class="comment-name">{{ msg.name }}</h4>
            <p class="comment-text">{{ msg.message }}</p>
            <small class="comment-date">{{ new Date(msg.created_at).toLocaleString() }}</small>
          </div>
        </div>
      </transition-group>
    </div>
  </div>
</template>

<style scoped>
.guestbook-container {
  padding: 40px;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
}

.header { text-align: center; margin-bottom: 40px; }

.glitch {
  font-size: 2.5rem; color: #fff; text-transform: uppercase;
  letter-spacing: 4px; text-shadow: 0 0 10px rgba(74, 222, 128, 0.5);
}
.subtitle { color: #4ade80; font-family: 'Courier New', monospace; }

/* Reusing the cyber-card aesthetic */
.cyber-card {
  background: rgba(16, 25, 33, 0.6); backdrop-filter: blur(10px);
  border: 1px solid rgba(74, 222, 128, 0.2); border-left: 4px solid #4ade80;
  border-radius: 12px; padding: 25px; margin-bottom: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

/* Input Styling */
.cyber-input {
  width: 100%; background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(74, 222, 128, 0.3);
  color: #4ade80; padding: 15px; border-radius: 8px; margin-bottom: 15px;
  font-family: 'Courier New', monospace; font-size: 1rem; outline: none;
  transition: border 0.3s;
}
.cyber-input:focus { border: 1px solid #4ade80; box-shadow: 0 0 10px rgba(74, 222, 128, 0.2); }
.textarea { min-height: 100px; resize: vertical; }

.cyber-btn {
  background: rgba(74, 222, 128, 0.1); border: 1px solid #4ade80;
  color: #4ade80; padding: 12px 24px; border-radius: 8px; font-weight: bold;
  font-family: 'Courier New', monospace; width: 100%; transition: 0.3s;
}
.cyber-btn:hover:not(:disabled) {
  background: #4ade80; color: #050a0e; box-shadow: 0 0 15px #4ade80;
}
.cyber-btn:disabled { opacity: 0.5; border-color: gray; color: gray; }

/* The Bark Alert */
.bark-alert {
  margin-top: 15px; text-align: center; color: #fff;
  background: rgba(74, 222, 128, 0.2); padding: 10px; border-radius: 8px;
  font-weight: bold; border: 1px dashed #4ade80;
}

/* Leaf Comments */
.leaf-comment {
  position: relative; display: flex; gap: 15px;
  border-left: none; border-right: 4px solid #4ade80; border-radius: 0 20px 20px 20px;
}
.leaf-deco {
  width: 20px; height: 20px; background: #4ade80;
  border-radius: 0 15px 0 15px; /* Leaf shape */
  box-shadow: 0 0 10px #4ade80; flex-shrink: 0; margin-top: 5px;
}
.comment-name { color: #fff; margin-bottom: 5px; font-family: 'Courier New', monospace;}
.comment-text { color: #b0c4de; line-height: 1.6; margin-bottom: 10px; }
.comment-date { color: rgba(74, 222, 128, 0.6); font-size: 0.8rem; }

/* Vue Transitions */
.list-enter-active, .list-leave-active { transition: all 0.5s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateY(30px); }
.bark-fade-enter-active, .bark-fade-leave-active { transition: opacity 0.3s; }
.bark-fade-enter-from, .bark-fade-leave-to { opacity: 0; }
</style>