<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue'
</script>

<template>
    <header class="header bg-gray-800 text-white">
      <div class="header-content flex items-center justify-between px-4 py-2">
        <div class="logo-container flex items-center">
          <img src="../assets/logo.png" alt="Logo" class="logo h-16 w-16 m-2">
          <button class="header-button">Meine Liste</button>
          <button class="header-button">Song suchen</button>
        </div>
        <div class="search-container">
          <input
            type="text"
            placeholder="Song suchen..."
            class="search-bar"
          >
        </div>
      </div>
      <div class="shine-animation"></div>
    </header>
</template>

<style scoped>
.header {
  position: relative;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  transition: transform 0.5s;
}

.header-button {
  transition: transform 0.5s;
}

.search-container {
  position: relative;
}

.search-bar {
  padding: 0.5rem 1rem;
  background-color: #2d3748;
  color: #fff;
  border: none;
  border-radius: 0.25rem;
  width: 200px;
  transition: width 0.5s;
}

.shine-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(to right, rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0));
  background-size: 200% 100%;
  transition: background-position 0.5s;
  pointer-events: none;
}

.header:hover .logo {
  transform: scale(1.2);
}

.header-button:hover {
  transform: scale(1.2);
}

.header:hover .search-bar {
  width: 300px;
}

.header:hover .shine-animation {
  background-position: -100% 0;
}

@media (max-width: 640px) {
  .header-content {
    flex-direction: column;
    align-items: center;
  }

  .logo-container {
    margin-bottom: 1rem;
  }
}
</style>