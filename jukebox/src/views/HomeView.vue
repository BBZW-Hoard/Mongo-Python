<script setup>
import { ref, onMounted, computed } from 'vue'
import Song from '../components/Song.vue';
import axios from 'axios';
import LoadingGrid from '../components/LoadingGridSong.vue';

const inputSearch = ref('');
const songs = ref("");
const filteredSongs = ref("");
const isLoading = ref(true);

// axios headers config
const config = {
    headers: {
        // 'content-type': 'application/x-www-form-urlencoded',
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
};

/**
 * loads song, if loading is fin, disable loading grid
 */
onMounted(async () => {
    await getSongs().then(() => {
        isLoading.value = false;
        filteredSongs.value = songs.value;
    });
})

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

function search() {
    let results = [];

    // Convert the input search string to lowercase for case-insensitive search
    let searchQuery = inputSearch.value.toLowerCase();

    if(searchQuery == "") {
        filteredSongs.value = songs.value;
        return;
    }

    for (let i = 0; i < songs.value.length; i++) {
        let song = songs.value[i];

        // Check if the search query matches the song's title or artist
        if (song.name.toLowerCase().includes(searchQuery)) results.push(song);
    }

    console.log(results);
    filteredSongs.value = results;
}
</script>

<template>
    <div v-if="!isLoading" class="mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <router-link :to="'/manage-song/' + 0">
                <button class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                    Song hinzufügen
                </button>
            </router-link>
            <input v-model="inputSearch" @keyup="search()" type="text" class="search w-full sm:w-auto sm:mx-4 text-gray-700" />
        </div>
        <!--  -->
        <div :class="{ 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4': songs.length != 0 }">
            <div v-if="songs.length != 0" v-for="song in filteredSongs" :key="song._id" class="bg-white rounded-md shadow p-4">
                <Song :song="song" />
            </div>
            <div v-else class="w-full border-2 border-black p-4 rounded-xl">
                <h1 class="text-2xl font-semibold text-center"><i>Keine Songs vorhaden</i></h1>
            </div>
        </div>
    </div>
    <div v-else>
        <LoadingGrid />
    </div>
</template>

<style scoped></style>