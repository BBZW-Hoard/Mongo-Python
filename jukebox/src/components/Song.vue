<script setup>
import { onMounted, ref } from 'vue';
import { config } from "../service/api.ts";
import axios from 'axios';

defineProps({
    song: {
        _id: String,
        name: String,
        attributes: {
            composer: String,
            genre: String,
            year: Number,
            album: String,
            required: false
        },
        duration: Number,
        rating: String,
        required: true,
    }
})

const playlists = ref("")
const isMobileView = ref(false);
const isDropdownOpen = ref(false);

onMounted(async () => {
    await handleScreenWidthChange();    // toggle mobile view

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
        // Handle the error appropriately
    });

    console.log("request", request);
    console.log("datenyp", typeof (request));
    playlists.value = request;
})

/* functions */
async function handleScreenWidthChange() {
    let screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

    if (screenWidth < 768) isMobileView.value = true;
    else isMobileView.value = false;
}

/**
 * return the duration in h or m format
 * */
function durationValue(duration) {
    if (duration >= 60) {
        let hours = Math.floor(duration / 60);
        let minutes = duration % 60;
        return hours + " h " + minutes + " min";
    } else return duration + " min";
}

async function addToPlaylist(song) {
    let selectedPlaylistId = localStorage.getItem("selectedPlaylist");
    const index = playlists.value.findIndex(x => x._id === selectedPlaylistId);
    let playlist = playlists.value[index];
    let res = playlist.songs.map(s => s._id);
    
    if (!Array.isArray(playlist.songs)) {
        console.log("No array: " + playlist.songs);
        playlist.songs = [song._id];
    } else {
        playlist.songs = res;
    }

    if (!res.includes(song._id)) {
        console.log("Pushed to array: " + playlist.songs);
        playlist.songs = res;
        playlist.songs.push(song._id);
    }

    console.log('Add to playlist:', song);
    await axios.put(('http://localhost:5000/playlists/' + playlist._id), playlist, config.headers);

    window.location.href = "/";
}

/* even listeners */
window.addEventListener('resize', handleScreenWidthChange);
</script>

<template>
    <div class="flex justify-between mb-2">
        <div class="font-semibold">{{ song.name }}</div>
        <div class="space-x-2 relative">
            <button title="Zur ausgewählten Playlist hinzufügen" class="text-green-600" @click="addToPlaylist(song)">
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 5v14m-7-7h14"></path>
                </svg>
            </button>
            <span v-if="!isMobileView">
                <button class="rounded-full p-1" @click="isDropdownOpen = !isDropdownOpen">
                    <img src="../assets/threeDots.svg" alt="" />
                </button>
                <div v-if="isDropdownOpen">
                    <router-link :to="'/manage-song/' + song._id">
                        <button class="dropdown rounded-t-sm mt-8">Bearbeiten</button>
                    </router-link>
                    <router-link :to="'delete-song/' + song._id">
                        <button class="dropdown rounded-b-sm mt-16">Löschen</button>
                    </router-link>
                </div>
            </span>
        </div>
    </div>
    <div class="text-gray-600 mb-2">
        <span>
            {{ song.attributes.composer != "" && song.attributes.composer != undefined ? 
                song.attributes.composer + " |" : '' }}
            {{ song.attributes.genre != "" && song.attributes.genre != undefined ?
                song.attributes.genre + " |" : '' }}
            {{ song.attributes.interpret != "" && song.attributes.interpret != undefined ?
                song.attributes.interpret + " |" : '' }}
            {{ song.attributes.year != "" && song.attributes.year != undefined ?
                song.attributes.year + " |" : '' }}
            {{ song.attributes.album != "" && song.attributes.album != undefined ?
            song.attributes.album : '' }}
            <!-- last objects in line is duration -->
            <span>{{ durationValue(song.duartion) }}</span>
        </span>
    </div>
    <div class="text-gray-500" :class="song.rating >= 4 ? 'text-green-600' : ''">{{ song.rating }} Rating</div>
    <div v-if="isMobileView">
        <router-link :to="'/manage-song/' + song._id">
            <button class="text-blue-900 mr-1">Bearbeiten</button>
        </router-link>
        <router-link :to="'delete-song/' + song._id">
            <button class="text-red-600 mx-1">Löschen</button>
        </router-link>
    </div>
</template>

<style scoped></style>