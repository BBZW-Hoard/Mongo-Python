<template>
    <div class="container mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <button @click="addSong()" class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                Song hinzufügen
            </button>
            <input v-model="inputSearch" type="text" class="search w-full sm:w-auto sm:mx-4" placeholder="Song suchen...">
        </div>
        <!--  -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div v-for="song in filteredSongs" :key="song.id" class="bg-white rounded-md shadow p-4">
                <Song :song="song" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Song from '../components/Song.vue';

const inputSearch = ref('');
const songs = ref([
    {
        id: 1,
        name: 'Forest of Jnana and Vidya',
        // Author, Interpret (publisher), Album
        attributes: ['Genshin Impact'],
        duartion: 65,
        rating: 4.5
    },
    {
        id: 2,
        name: 'We Named Her Ku',
        attributes: ['Ori and the Will of the Wisps'],
        duartion: 4,
        rating: 5
    },
    {
        id: 3,
        name: 'Dovahkiin',
        attributes: ['Jeremy Soule', 'London Music Works', 'The Song Of The Dragonborn'],
        duartion: 4,
        rating: 4.8
    },
])

const filteredSongs = computed(() => {
    return songs.value.filter(x => x.name.toLowerCase().includes(inputSearch.value.toLowerCase()))
})

/* functions */

// adds a song to songs array (HArdcoded)
function addSong() {
    let song = {
        id: Math.random() * 4249,
        name: 'new Song',
        attributes: ['new Attribute'],
        duration: 424,
        rating: 2.8
    }
    songs.value.push(song);
}
</script>

<style scoped></style>