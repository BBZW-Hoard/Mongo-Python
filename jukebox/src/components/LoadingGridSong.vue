<script setup></script>

<template>
    <div class="grid grid-cols-3 gap-4">
        <div v-for="i in 8" class="bg-white p-4 rounded shadow">
            <!-- Display item content -->
            <div class="mb-2 h-6 bg-gray-300 animate-pulse"></div>
            <div class="h-4 bg-gray-300 animate-pulse"></div>
            <div class="h-4 bg-gray-300 animate-pulse"></div>
        </div>
    </div>
</template>