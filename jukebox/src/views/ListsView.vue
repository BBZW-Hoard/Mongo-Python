<template>
    <div class="container mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <button class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                Playlist erstellen
            </button>
            <button @click="addSong" class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                Song hinzufügen
            </button>
            <input v-model="inputSearch" type="text" class="search w-full sm:w-auto sm:mx-4" placeholder="Song suchen...">
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-h-[405px] overflow-y-auto border-2 border-gray-500 px-2"
            :class="filteredSongs == null ? 'py-1' : ''">
            <div v-for="song in songsListPlaylist" :key="song.id" class="bg-white rounded-md shadow p-4">
                <Song :song="song" :showCRUDButtons="false" />
            </div>
        </div>
        <div>
            <h1 class="flex justify-center text-5xl py-8 font-bold tracking-wider waving-text">
                <span>Playlists</span>
                <span class="mx-4 mt-4">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 15.944 15.266">
                        <g id="Komponente_1_1" data-name="Komponente 1 – 1" transform="translate(0.5 0.5)">
                            <line id="Linie_1" data-name="Linie 1" x2="11" fill="none" stroke="#000" stroke-linecap="round"
                                stroke-width="1" />
                            <line id="Linie_2" data-name="Linie 2" x2="11" transform="translate(0 4)" fill="none"
                                stroke="#000" stroke-linecap="round" stroke-width="1" />
                            <line id="Linie_3" data-name="Linie 3" x2="6" transform="translate(0 8)" fill="none"
                                stroke="#000" stroke-linecap="round" stroke-width="1" />
                            <line id="Linie_4" data-name="Linie 4" x2="6" transform="translate(0 12)" fill="none"
                                stroke="#000" stroke-linecap="round" stroke-width="1" />
                            <g id="Polygon_1" data-name="Polygon 1" transform="translate(13.5 7) rotate(90)" fill="#fff"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path
                                    d="M 6.883100032806396 5.5 L 6 5.5 L -4.440892098500626e-16 5.5 L -0.8830999732017517 5.5 L -0.4287500083446503 4.74275016784668 L 2.571249961853027 -0.2572500109672546 L 3 -0.9718300104141235 L 3.428750038146973 -0.2572500109672546 L 6.428750038146973 4.74275016784668 L 6.883100032806396 5.5 Z"
                                    stroke="none" />
                                <path
                                    d="M 3 0 L 0 5 L 6 5 L 3 0 M 3 -1 C 3.35125994682312 -1 3.676769971847534 -0.8157000541687012 3.857490062713623 -0.5145001411437988 L 6.857490062713623 4.485499858856201 C 7.042850017547607 4.794429779052734 7.047709941864014 5.179190158843994 6.870200157165527 5.492700099945068 C 6.692689895629883 5.806210041046143 6.360270023345947 6 6 6 L 0 6 C -0.3602700233459473 6 -0.6926898956298828 5.806210041046143 -0.8702001571655273 5.492700099945068 C -1.047709941864014 5.179190158843994 -1.042850017547607 4.794429779052734 -0.857490062713623 4.485499858856201 L 2.142509937286377 -0.5145001411437988 C 2.323230028152466 -0.8157000541687012 2.64874005317688 -1 3 -1 Z"
                                    stroke="none" fill="#000" />
                            </g>
                        </g>
                    </svg>
                </span>
            </h1>
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

const songsListPlaylist = computed(() => {
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