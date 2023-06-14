<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div>
    <Header />
    <div class="flex">
      <Sidebar />
      <div class="flex-grow">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style></style>
