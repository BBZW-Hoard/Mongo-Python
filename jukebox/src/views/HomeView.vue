<script setup>
import { ref, computed, onMounted } from 'vue'
import Song from '../components/Song.vue';
import axios from 'axios';

const inputSearch = ref('');
const songs = ref("");

/* const filteredSongs = computed(() => {
    return songs.value.filter(x => x.name.toLowerCase().includes(inputSearch.value.toLowerCase()))
}) */

// axios headers config
const config = {
    headers: {
        // 'content-type': 'application/x-www-form-urlencoded',
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
};

onMounted(async () => {
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
})

</script>

<template>
    <div class="mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <router-link :to="'/manage-song/' + 0">
                <button class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                    Song hinzufügen
                </button>
            </router-link>
            <input v-model="inputSearch" type="text" class="search w-full sm:w-auto sm:mx-4" placeholder="Song suchen...">
        </div>
        <!--  -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            <div v-for="song in songs" :key="song._id" class="bg-white rounded-md shadow p-4">
                <Song :song="song" />
            </div>
        </div>
    </div>
</template>

<style scoped></style>