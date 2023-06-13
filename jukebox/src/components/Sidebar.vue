<script setup>
import { onMounted, ref } from 'vue';
import jsonPlaylists from '../assets/json/playlists.json'

const sidebarOpen = ref(true);
const isPlaylistOpen = ref(new Array(jsonPlaylists.length));
const playlists = ref(jsonPlaylists);

onMounted(() => {
    closeAllPlaylists();
    let selectedPlaylistId = localStorage.getItem("selectedPlaylist") == "0" ? null : parseInt(localStorage.getItem("selectedPlaylist")); 
    isPlaylistOpen.value[selectedPlaylistId] = !isPlaylistOpen.value[selectedPlaylistId];
})

function closeAllPlaylists() {
    isPlaylistOpen.value.fill(false);
}

function togglePlaylist(id) {
    // skip if user wants to close active playlist
    if(isPlaylistOpen.value[id - 1] != true) closeAllPlaylists();

    isPlaylistOpen.value[id - 1] = !isPlaylistOpen.value[id - 1];
    
    // LS: Update LocalStorage entry
    localStorage.setItem("selectedPlaylist", id);
}
</script>

<template>
    <div class="flex min-h-screen">
        <!-- no v-if because songs will -->
        <div class="w-72 bg-gray-800 text-white p-4" :class="{ 'hidden': !sidebarOpen }">
            <div class="flex items-center mb-4">
                <button class="mr-2 text-white hover:text-gray-300" @click="sidebarOpen = false">
                    <img src="../assets/arrowRight.svg" alt=">" />
                </button>
                <span class="font-semibold text-2xl">Playlists</span>
                <span class="mx-2 mt-2">
                    <img src="../assets/playlist.svg" alt="" />
                </span>
            </div>
            <div v-for="playlist in playlists" :key="playlist.id">
                <button class="flex items-center justify-between w-full mb-2 focus:outline-none" @click="togglePlaylist(playlist.id)">
                    <span class="truncate text-md font-bold">
                        {{ playlist.name }} <i>{{ isPlaylistOpen[playlist.id - 1] ? '(ausgewählt)' : ''  }}</i>
                    </span>
                    <img :class="{ 'rotate-180': isPlaylistOpen[playlist.id - 1] }" src="../assets/arrowDown.svg" alt="" />
                </button>
                <div v-show="isPlaylistOpen[playlist.id - 1]">
                    <div v-for="song in playlist.songs" class="flex items-center mb-2">
                        <span class="truncate">> {{ song.name }}</span>
                        <div class="ml-auto flex">
                            <button class="p-1 hover:bg-green-500 rounded-full" title="Play">
                                <img src="../assets/play.svg" alt="play" />
                            </button>
                            <button class="p-1 hover:bg-red-500 rounded-full ml-2" title="Delete">
                                <img src="../assets/trash.svg" alt="trash" />
                            </button>
                        </div>
                    </div>
                    <!-- Add more items here -->
                </div>
            </div>
            <!-- Add more playlists here -->
        </div>
        <div class="flex-grow bg-gray-100">
            <!-- Content of your website -->
        </div>
    </div>
</template>

<style scoped></style>