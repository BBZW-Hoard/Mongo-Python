<script setup>
import { onMounted, ref } from 'vue'

defineProps({
    song: {
        name: String,
        attributes: Array,
        duration: Number,
        rating: String,
        required: true,
    },
    showCRUDButtons: {
        type: Boolean,
        required: true
    },
})

const isMobileView = ref(false);
const isDropdownOpen = ref(false);

onMounted(() => {
    handleScreenWidthChange();
})

/* functions */
function handleScreenWidthChange() {
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


/* even listeners */
window.addEventListener('resize', handleScreenWidthChange);
</script>

<template>
    <div class="flex justify-between mb-2">
        <div class="font-semibold">{{ song.name }}</div>
        <div class="space-x-2 relative">
            <button class="text-green-600" @click="addToPlaylist(song)">
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 5v14m-7-7h14"></path>
                </svg>
            </button>
            <span v-if="!isMobileView">
                <button class="rounded-full p-1" @click="isDropdownOpen = !isDropdownOpen">
                    <img src="../assets/threeDots.svg" alt="" />
                </button>
                <div v-if="showCRUDButtons && isDropdownOpen">
                    <button class="dropdown rounded-t-sm mt-8" @click="editSong(song)">Bearbeiten</button>
                    <button class="dropdown rounded-b-sm mt-16" @click="deleteSong(song)">Löschen</button>
                </div>
            </span>
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
    <div v-if="isMobileView">
        <button class="text-blue-900 mx-1" @click="editSong(song)">Bearbeiten</button>
        <button class="text-red-600 mx-1" @click="deleteSong(song)">Löschen</button>
    </div>
</template>

<style scoped></style>