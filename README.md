
# 🐾 Cyber-Forensics & Veterinary Portfolio

An immersive, full-stack personal webpage built with **Vue 3**, blending high-tech cybersecurity aesthetics with animal welfare themes. This project features advanced WebGL transitions, GPU-accelerated interactions, and a real-time digital "Cyber Forest" guestbook.

## 🚀 Key Features

### 🎰 Nature-Integrated Loading Sequence

A custom `WelcomeLoader` component that initializes the user experience with:

* **Slot Machine Reveal:** A staggered text animation that spins through random characters to reveal "WELCOME".
* **The Growth Sequence:** Upon clicking "Enter Profile," a middle-screen "WELCOME HUMAN!" prompt appears as a digital forest (Trees 🌳 and Flowers 🌸) grows dynamically from the bottom of the screen using CSS transform-origin logic.

### 🌓 Dual-State Interactive Hero

A responsive hero banner that adapts to the user's environment:

* **State Switching:** Swaps between an "Active" character (`me.png`) and a "Sleeping" character (`mesleep.png`) based on the theme.
* **Static Overlap:** The character image utilizes absolute positioning and overflow logic to "pop out" of the banner frame for a 3D effect.
* **Dynamic Backgrounds:** Hardcoded GIF transitions to ensure zero-lag background updates during theme switching.

### 🐕 Advanced Cursor & Particles

* **GPU Acceleration:** The custom Dog cursor (🐕) uses `translate3d` and direct DOM manipulation to bypass Vue's reactivity lag, ensuring 60FPS tracking.
* **Interaction SFX:** A custom canvas layer that generates "Paw Print" (🐾) particles at the exact mouse coordinates upon every click.

### 🖼️ WebGL Life Gallery

A high-performance image slider built with **Three.js** and **GSAP**:

* **Displacement Mapping:** Uses a custom fragment shader to warp images during transitions.
* **Interactive Navigation:** Supports both a 5-second auto-play timer and manual click-to-advance functionality.

### 🍃 Cyber Forest Guestbook (CRUD)

A full-stack integration with **Supabase**:

* **Real-time Sync:** Messages are fetched and posted via RESTful API headers.
* **Unfurling UI:** New entries use a "Pop-Under" animation where messages appear to unfurl like opening leaves using `<TransitionGroup>`.
* **Sticker System:** Allows users to "plant" messages with Leaf, Paw, or Tree metadata.

---

## 📂 Project Structure

```text
portfolio-frontend/
├── public/                 # Static assets (Directly served)
│   ├── img/                # Character state assets (mesleep.png)
│   ├── image/              # Gallery & Polaroid assets (kel.jpg, draww.png)
│   ├── audio/              # Background music (down.mp3)
│   └── favicon.ico         # Site icon
├── src/
│   ├── components/         # Reusable Global Components
│   │   ├── LifeGallery.vue     # WebGL/Three.js Gallery
│   │   └── WelcomeLoader.vue   # Loading sequence & nature growth
│   ├── views/              # Page Components
│   │   ├── HomeView.vue        # Main Landing (Hero, Resume, Projects)
│   │   └── GuestbookView.vue   # Supabase Message Board
│   ├── App.vue             # Master Layout (Navbar, Cursor, Global CSS)
│   ├── main.js             # Entry point
│   └── router.js           # Vue Router definitions
├── .env                    # Environment variables (Hidden)
├── index.html              # Template root
└── package.json            # Dependencies (Three.js, GSAP, Vue-Router)

```

---

## 📱 Responsiveness Details

The site utilizes a **Mobile-First** approach with specific logic for touch devices:

* **Grid Collapse:** 2-column dashboard grids transition to a single column at `1024px`.
* **Hero Stacking:** At `768px`, the Hero Banner character moves from an absolute right-side position to a centered bottom position to prevent text overlap.
* **Adaptive Cursor:** The custom cursor is automatically disabled on touch devices (`(pointer: coarse)`) to ensure standard mobile usability and prevent "stuck" cursor bugs.

---

## 🛠️ Installation & Setup

1. **Clone the Repo**
```bash
git clone https://github.com/Sofia-revilla/portfolio-frontend.git

```


2. **Dependencies**
```bash
npm install

```


3. **Environment Setup**
Create a `.env` file and provide your Supabase credentials:
```env
VITE_SUPABASE_URL=your_project_url
VITE_SUPABASE_ANON_KEY=your_anon_key

```


4. **Launch**
```bash
npm run dev

```



---

## 🔐 Technical Documentation

### GPU-Accelerated Cursor Logic

To prevent the cursor from disappearing behind complex components like the WebGL Gallery or Goal cards, the `paw-cursor` is set to `position: fixed` with a `z-index` of `2147483647`. It uses the `animate()` API for the trailing outline to reduce CPU overhead.

### Theme Persistence

Theme switching is handled by toggling the `.dark-mode` class on `document.documentElement`. This ensures that CSS variables for `--bg-color` and `--card-white` propagate through the entire DOM tree, including scroll-parent containers.

### Supabase Integration

The guestbook utilizes an **Optimistic UI** pattern. When a user clicks "Plant," the message is unshifted into the local Vue `ref` array instantly for a zero-lag feel, while the `fetch` POST request runs asynchronously in the background.

---

**Author:** Ma. Sofia Anne C. Revilla

**Specialization:** Cybersecurity & Forensics | Future Veterinarian

**Stack:** Vue.js, Three.js, GSAP, Supabase, Vite.
