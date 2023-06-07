<template>
    <div class="container mx-auto p-4">
        <div class="sm:flex justify-start mb-4">
            <button class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                Playlist erstellen
            </button>
            <button class="btn w-full my-4 sm:w-auto sm:my-0 sm:mx-4">
                Song hinzufügen
            </button>
            <input type="text" class="search w-full sm:w-auto sm:mx-4" placeholder="Song suchen...">
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
</script>

<style scoped></style>