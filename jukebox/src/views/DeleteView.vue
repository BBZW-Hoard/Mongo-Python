<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../router/index.js';
import axios from 'axios';


const route = useRoute();
const id = route.params.id;

const song = ref({
    name: "",
    attributes: {
        composer: "",
        genre: "",
        interpret: "",
        year: 0,
        album: ""
    },
    duration: 0,
    rating: 0,
    url: ""
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
        let request = await axios.get(("http://localhost:5000/songs/" + id));
        song.value = request.data;
    } catch (e) {
        console.error("error in request:", e);
        // weiterleiten zu 404
    }
})


async function submit() {
    axios({
        url: 'http://localhost:5000/songs/' + song.value._id,
        method: "delete",
        headers: config.headers
    })

    try {
        await axios.delete();
    } catch (e) {
        console.error(e); // Handle the error
    }

    router.push({ path: '/', replace: true });
}
</script>

<template>
    <div class="container mx-auto p-4">
        <h1 class="text-2xl font-semibold mb-2">Soll dieser Song gelöscht werden?</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="name" class="text-gray-600">Name
                    <b>*</b></label>
                <input id="name" v-model="song.name" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label for="composer" class="text-gray-600">Komponist</label>
                <input v-model="song.attributes.composer" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label class="text-gray-600">Genre</label>
                <input v-model="song.attributes.genre" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label class="text-gray-600">Interpret</label>
                <input v-model="song.attributes.interpret" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label class="text-gray-600">Veröffentlichungsjahr</label>
                <input v-model="song.attributes.year" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label class="text-gray-600">Album</label>
                <input v-model="song.attributes.album" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div class="md:col-span-2">
                <hr class="my-4 border-gray-200" />
            </div>
            <div>
                <label class="text-gray-600">Dauer in Minuten <b>*</b></label>
                <input v-model="song.duration" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div>
                <label class="text-gray-600">Rating
                    <b>*</b></label>
                <input v-model="song.rating" class="input-field bg-gray-300 text-gray-700" readonly />
            </div>
            <div class="md:col-span-2">
                <button class="btn-delete" @click="submit()">Bestätigen</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>