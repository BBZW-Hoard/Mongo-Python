<script setup></script>

<template>
    <div class="flex items-center justify-center h-screen bg-gray-200">
        <div class="text-center">
            <h1 class="text-6xl font-bold text-red-500">404</h1>
            <h2 class="text-2xl mt-4">Seite nicht gefunden</h2>
            <p class="mt-2">Die gesuchte Seite existiert nicht (mehr) oder sie wurde verschoben.</p>
            <router-link to="/"
                class="mt-4 inline-block bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded">
                Zurück zur Homeseite
            </router-link>
        </div>
    </div>
</template>

<style scoped></style>