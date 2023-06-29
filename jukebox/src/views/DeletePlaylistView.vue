<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../router/index.js';
import axios from 'axios';


const route = useRoute();
const id = route.params.id;

const playlist = ref({
    name: "",
    songs: []
})

// axios headers config
const config = {
    headers: {
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
};

onMounted(async () => {
    try {
        // loading entry with id from database
        let request = await axios.get(("http://localhost:5000/playlists/" + id));
        playlist.value = request.data;
    } catch (e) {
        console.error("error in request:", e);
        // weiterleiten zu 404
    }
})


async function submit() {
    try {
        await axios.delete(('http://localhost:5000/playlists/' + playlist.value._id), config.headers);
    } catch (e) {
        console.error(e); // Handle the error
    }

    window.location.href = "/";
}
</script>

<template>
    <div class="container mx-auto p-4">
        <h1 class="text-2xl font-semibold mb-2">Soll diese Playlist gelöscht werden?</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="name" class="text-gray-600">Name
                    <b>*</b></label>
                <input id="name" v-model="playlist.name" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
        </div>
        <h1 class="text-2xl font-bold">Enthaltene Songs:</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <ul v-for="song in playlist.songs" class="pb-4 border-black border-b-2">
                <li><b>Name:</b> {{ song.name }}</li>
                <ul>
                    {{ console.log("songAttribute", song.attributes) }}
                    <li class="list-none text-lg"><b>Attribute:</b></li>
                    <li class="ml-4"><b>Komponist:</b> {{ song.attributes.composer }}</li>
                    <li class="ml-4"><b>Genre:</b> {{ song.attributes.genre }}</li>
                    <li class="ml-4"><b>Interpret:</b> {{ song.attributes.interpret }}</li>
                    <li class="ml-4"><b>Veröffentlichungsjahr:</b> {{ song.attributes.year }}</li>
                    <li class="ml-4"><b>Album:</b> {{ song.attributes.album }}</li>
                </ul>
                <li><b>Dauer in Minuten:</b> {{ song.duration }}</li>
                <li><b>Rating:</b> {{ song.rating }}</li>
            </ul>
        </div>

        <div class="md:col-span-2">
            <hr class="my-4 border-gray-200" />
        </div>
        <div class="md:col-span-2">
            <button class="btn-delete" @click="submit()">Bestätigen</button>
        </div>

    </div>
</template>

<style scoped></style>