<script setup>
import { ref, defineProps } from 'vue';

defineProps({
    isError: {
        type: Boolean,
        required: true,
    },
    errorMessage: {
        type: String,
        required: true,
    }
})
</script>

<template>
    <div :class="isError ? 'bg-red-500' : 'bg-green-500'"
        class="fixed bottom-4 right-4 text-white px-4 py-2 rounded flex items-center">
        <span class="mr-2">{{ errorMessage }}</span>
        <button class="text-white hover:text-gray-300">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd"
                    d="M13.414 10l4.293-4.293a1 1 0 10-1.414-1.414L12 8.586 7.707 4.293a1 1 0 10-1.414 1.414L10.586 10l-4.293 4.293a1 1 0 001.414 1.414L12 11.414l4.293 4.293a1 1 0 001.414-1.414L13.414 10z"
                    clip-rule="evenodd" />
            </svg>
        </button>
    </div>
</template>

<style scoped></style>