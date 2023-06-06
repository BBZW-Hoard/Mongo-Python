<template>
    <div class="container mx-auto p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4">
            <div v-for="song in songs" :key="song.id" class="bg-white rounded-md shadow p-4">
                <div class="flex justify-between mb-2">
                    <div class="font-semibold">{{ song.name }}</div>
                    <div class="space-x-2">
                        <button class="text-green-600" @click="addToPlaylist(song)">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 5v14m-7-7h14"></path>
                            </svg>
                        </button>
                        <button class="text-blue-600" @click="editSong(song)">Bearbeiten</button>
                        <button class="text-red-600" @click="deleteSong(song)">Löschen</button>
                    </div>
                </div>
                <div class="text-gray-600 mb-2">
                    <span v-for="attribute in song.attributes" :key="attribute">
                        {{ attribute }} |
                        <!-- last objects in line is duration -->
                        <span v-if="isLastAttribute(attribute, song.attributes)">{{ durationValue(song.duartion) }}</span>
                    </span>
                </div>
                <div class="text-gray-500" :class="song.rating >= 4 ? 'text-green-600' : ''">{{ song.rating }} Rating</div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

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

/* functions */

// return the duration in h or m format
function durationValue(duration) {
  if (duration >= 60) {
    let hours = Math.floor(duration / 60);
    let minutes = duration % 60;
    return hours + " h " + minutes + " min";
  } else return duration + " min";
}

function addToPlaylist(song) {
    // Add logic for adding song to playlist
    console.log('Add to playlist:', song);
}
function editSong(song) {
    // Add logic for editing the song
    console.log('Edit song:', song);
}
function deleteSong(song) {
    // Add logic for deleting the song
    console.log('Delete song:', song);
}
function isLastAttribute(attribute, attributes) {
    // Check if the attribute is the last one in the list
    return attribute === attributes[attributes.length - 1];
}
</script>

<style scoped></style>