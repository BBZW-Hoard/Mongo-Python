<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue';
import { getLocalStorageItems } from './service/LocalStorage.ts';
import { onMounted } from 'vue';

onMounted(async () => {
  await getLocalStorageItems("selectedPlaylist");
})
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