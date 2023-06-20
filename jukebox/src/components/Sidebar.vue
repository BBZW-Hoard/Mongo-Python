<script setup>
import { onMounted, ref } from 'vue';
import jsonPlaylists from '../assets/json/playlists.json'

const sidebarOpen = ref(true);
const isPlaylistOpen = ref(new Array(jsonPlaylists.length));
const playlists = ref(jsonPlaylists);
const currentlyPlayedSongUrl = ref("public/songs/a-call-to-the-soul.mp3");
const showPlaylistContainer = ref(false);
const selectedPlaylistId = ref("")

onMounted(() => {
    closeAllPlaylists();
    selectedPlaylistId.value = localStorage.getItem("selectedPlaylist");  // must not be converted
    isPlaylistOpen.value[selectedPlaylistId.value] = !isPlaylistOpen.value[selectedPlaylistId.value];
})

/**
 * closes all Playlists
 */
function closeAllPlaylists() {
    isPlaylistOpen.value.fill(false);
}

function togglePlaylist(id) {
    id--;
    // skip if user wants to close active playlist
    if (isPlaylistOpen.value[id] != true) closeAllPlaylists();

    isPlaylistOpen.value[id] = !isPlaylistOpen.value[id];

    // LS: Update LocalStorage entry
    if (localStorage.getItem("selectedPlaylist") == id) localStorage.setItem("selectedPlaylist", "null");
    else localStorage.setItem("selectedPlaylist", id);

    selectedPlaylistId.value = localStorage.getItem("selectedPlaylist");
}

/**
 * Updates the currtlyPlayedSong and stats it automaticly 
 * @param {string} url url to song mp3 file; if empty -> close player
 */
async function playSong(url) {
    showPlaylistContainer.value = false;    // for reload -> disable object and switch song

    // no song, just close Playlist Container
    if (url.trim().length === 0) return;

    setTimeout(() => {
        showPlaylistContainer.value = true; // enable object
    }, await changeUrl(url));
}

/**
 * changes the url link from the song
 * @param {string} url url to song mp3 file 
 */
async function changeUrl(url) {
    currentlyPlayedSongUrl.value = url;
    return true;
}

/**
 * cuts string if its longer that 30 digits.
 * @param {string} str song.name / long string
 */
function getSongLength(str) {
    if (str.length <= 30) return str;

    return str.slice(0, 30) + '...';
}
</script>

<template>
    <div class="flex min-h-screen">
        <!-- no v-if because songs will -->
        <div class="relative w-screen sm:w-80 bg-gray-800 text-white p-4" :class="{ 'hidden': !sidebarOpen }">
            <div class="flex items-center mb-4">
                <button class="mr-2 text-white hover:text-gray-300" title="Seitenleiste schliessen"
                    @click="sidebarOpen = false">
                    <img src="../assets/arrowRight.svg" alt=">" />
                </button>
                <span class="font-semibold text-2xl">Playlists</span>
                <span class="mx-2 mt-2">
                    <img src="../assets/playlist.svg" alt="" />
                </span>
            </div>
            <div v-for="playlist in playlists" :key="playlist.id">
                <button class="flex items-center justify-between w-full mb-2 focus:outline-none"
                    @click="togglePlaylist(playlist.id)">
                    <span class="truncate text-md font-bold">
                        {{ playlist.name }} <i>{{ isPlaylistOpen[playlist.id - 1] ? '(ausgewählt)' : '' }}</i>
                    </span>
                    <img :class="{ 'rotate-180': isPlaylistOpen[playlist.id - 1] }" src="../assets/arrowDown.svg" alt=""
                        :title="!isPlaylistOpen[playlist.id - 1] ? 'Playlist öffnen' : 'Playlist schliessen'" />
                </button>
                <div v-show="isPlaylistOpen[playlist.id - 1]">
                    <div v-for="song in playlist.songs" class="flex items-center mb-2">
                        <span class="truncate flex-grow">> {{ getSongLength(song.name) }}</span>
                        <div class="ml-auto flex">
                            <button class="p-1 hover:bg-gray-500 rounded-full" title="Download">
                                <a :href="song.url" download target="_blank" class="w-full h-full">
                                    <img src="../assets/download.svg" alt="download" />
                                </a>
                            </button>
                            <button @click="playSong(song.url)" class="p-1 hover:bg-green-500 rounded-full ml-1"
                                title="Play">
                                <img src="../assets/play.svg" alt="play" />
                            </button>
                            <button class="p-1 hover:bg-red-500 rounded-full ml-1" title="Delete">
                                <img src="../assets/trash.svg" alt="trash" />
                            </button>
                        </div>
                    </div>
                    <!-- Add more items here -->
                </div>
            </div>
            <!-- Add more playlists here -->

            <!-- Fixed container for currently played songs -->
            <div v-if="showPlaylistContainer" class="fixed bottom-0 left-0 w-80 bg-gray-800 p-4">
                <div class="text-white">
                    <div class="flex justify-between">
                        <span class="font-semibold">Laufendes Lied:</span>
                        <button @click="showPlaylistContainer = false" class="p-2 hover:bg-red-500 rounded-full"
                            title="Song stoppen">
                            <img src="../assets/trash.svg" alt="trash" />
                        </button>
                    </div>
                    <ul class="mt-2">
                        <!-- <li v-for="song in currentlyPlayedSongs" :key="song.id">{{ song.name }}</li> -->
                        <audio controls autoplay="true">
                            <source :src="currentlyPlayedSongUrl" type="audio/mpeg" />
                            Your browser does not support the audio player.
                        </audio>
                    </ul>
                </div>
            </div>
        </div>
        <div v-if="!sidebarOpen" class="flex-grow bg-gray-800">
            <button class="mr-2 text-white hover:text-gray-300 p-2" title="Seitenleiste öffnen" @click="sidebarOpen = true">
                <img src="../assets/arrowRight.svg" alt=">" class="w-8 p-1 rotate-180 hover:bg-gray-500 rounded-full" />
            </button>
        </div>
    </div>
</template>

<style scoped></style>