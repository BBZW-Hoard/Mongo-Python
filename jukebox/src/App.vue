<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue';
import { getLocalStorageItems } from './service/LocalStorage.ts';
import { onMounted } from 'vue';

// SHOULD BE DIFFERENT FILE
import { provide, ref } from 'vue'
import { config } from "./service/api.ts"
import axios from 'axios';
const songs = ref();
const playlists = ref("");

provide(/* key */ 'songs', /* value */ { songs, getSongs })
provide('playlists', { playlists, getPlaylists })

/**
 * get all songs from backend
 */
async function getSongs() {
  let request;

  await axios.get("http://localhost:5000/songs/", config.headers).then(res => {
    const parsed = res.data; // Assuming the res data is an object or JSON
    if (parsed) {
      // Access the expected properties or perform the desired actions
      request = res.data;
    } else {
      throw new Error('Response data is undefined or null.');
    }
  }).catch(e => {
    console.error("Throw error:", e);
    // Handle the error appropriately
  });

  console.log("request", request);
  console.log("datenyp", typeof (request));
  songs.value = request;
}

/**
 * get request to load all playlists and put them in playlists 
 */
async function getPlaylists() {
  let request;

  await axios.get("http://localhost:5000/playlists/", config.headers).then(res => {
    const parsed = res.data; // Assuming the res data is an object or JSON
    if (parsed) {
      // Access the expected properties or perform the desired actions
      request = res.data;
    } else {
      throw new Error('Response data is undefined or null.');
    }
  }).catch(e => {
    console.error("Throw error:", e);
  });

  console.log("request", request);
  console.log("datenyp", typeof (request));
  playlists.value = request;
}
// END OF SHOULD BE DIFFERENT FILE

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