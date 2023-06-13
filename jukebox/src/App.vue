<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div>
    <MangeLS />
    <Header />
    <div class="flex">
      <Sidebar />
      <router-view />
    </div>
  </div>
</template>

<style></style>
