<script setup>
import { ref, computed } from 'vue'
import Song from '../components/Song.vue';
import jsonSongs from '../assets/json/songs.json';

const inputSearch = ref('');
const songs = ref(jsonSongs);

const filteredSongs = computed(() => {
    return songs.value.filter(x => x.name.toLowerCase().includes(inputSearch.value.toLowerCase()))
})

/* functions */

// adds a song to songs array (Hardcoded)
function addSong() {
    let song = {
        id: Math.floor(Math.random() * 4242),
        name: 'new Song',
        attributes: ['new Attribute'],
        duration: Math.floor(Math.random() * 424),
        rating: (Math.random() * 5).toFixed(1)
    };
    songs.value.push(song);
}
</script>

<template>
    <div class="mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <router-link :to="'/manage-song/' + 0">
                <button @click="addSong()" class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                    Song hinzufügen
                </button>
            </router-link>
            <input v-model="inputSearch" type="text" class="search w-full sm:w-auto sm:mx-4" placeholder="Song suchen...">
        </div>
        <!--  -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            <div v-for="song in filteredSongs" :key="song.id" class="bg-white rounded-md shadow p-4">
                <Song :song="song" :showCRUDButtons="true" />
            </div>
        </div>
    </div>
</template>

<style scoped></style>