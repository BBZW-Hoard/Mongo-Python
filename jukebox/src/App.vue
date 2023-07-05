<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue';
import CreateLocalStorage from './components/CreateLocalStorage.vue';
</script>

<template>
  <div>
    <CreateLocalStorage />
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