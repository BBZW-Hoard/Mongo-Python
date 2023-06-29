<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { isValidated } from "../service/Valitation.ts";
import router from '../router/index.js';
import axios from 'axios';


const route = useRoute();
const id = route.params.id;

const requestType = ref("");
const song = ref({
    name: "",
    attributes: {
        composer: "",
        genre: "",
        interpret: "",
        year: new Date().getFullYear(), // number
        album: ""
    },
    duration: 6,
    rating: 3.4,
    url: "public/songs/a-call-to-the-soul.mp3"
})

const errorMessages = ref({
    name: null,
    composer: null,
    genre: null,
    interpret: null,
    year: null,
    album: null,
    duration: null,
    rating: null
})

// axios headers config
const config = {
    headers: {
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
};


onMounted(async () => {
    if (id == 0) {   // create new entry
        requestType.value = "POST";
    } else {
        requestType.value = "PUT";

        try {
            // loading entry with id from database
            let request = await axios.get(("http://localhost:5000/songs/" + id));
            song.value = request.data;
        } catch (e) {
            console.error("error in request:", e);
            // weiterleiten zu 404
        }
    }

})

async function submit() {
    let validated = true;

    /* set all key-values from errorMessages to null */
    try {
        Object.assign(errorMessages.value, Object.fromEntries(Object.keys(errorMessages.value).map(key => [key, null])));
    } catch (e) {
        console.error("Could not clear values from errorMessages object", e);
    }

    let result = isValidated(song.value);
    validated = result[0];
    errorMessages.value = result[1];

    if (validated) {
        // validated
        alert("validated");

        if (requestType.value === "POST") {
            try {
                await axios.post("http://localhost:5000/songs/", song.value, config.headers);
            } catch (e) {
                console.error("error:", e);  // Handle the error
            }
        } else if (requestType.value === "PUT") {
            try {
                await axios.put(('http://localhost:5000/songs/' + song.value._id), song.value, config.headers);
            } catch (e) {
                console.error("error:", e); // Handle the error
            }
        } else {
            console.error("Can't make request; Unknown requestType:", requestType.value);
        }

        router.push({ path: '/', replace: true });
    }
}
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="name" class="text-gray-600" :class="{ 'text-red-500': errorMessages.name != null }">Name
                    <b>*</b></label>
                <input id="name" type="text" v-model="song.name" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.name != null, 'border-red-500': errorMessages.name != null }"
                    placeholder="Name..." required />
                <label for="name" class="text-red-500 px-1">{{ errorMessages.name }}</label>
            </div>
            <div>
                <label for="composer" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.composer != null }">Komponist</label>
                <input id="composer" type="text" v-model="song.attributes.composer" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.composer != null, 'border-red-500': errorMessages.composer != null }"
                    placeholder="Komponist..." />
                <label for="composer" class="text-red-500 px-1">{{ errorMessages.composer }}</label>
            </div>
            <div>
                <label for="genre" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.genre != null }">Genre</label>
                <input id="genre" type="text" v-model="song.attributes.genre" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.genre != null, 'border-red-500': errorMessages.genre != null }"
                    placeholder="Genre..." />
                <label for="genre" class="text-red-500 px-1">{{ errorMessages.genre }}</label>
            </div>
            <div>
                <label for="interpret" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.interpret != null }">Interpret</label>
                <input id="interpret" type="text" v-model="song.attributes.interpret" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.interpret != null, 'border-red-500': errorMessages.interpret != null }"
                    placeholder="Interpret..." />
                <label for="interpret" class="text-red-500 px-1">{{ errorMessages.interpret }}</label>
            </div>
            <div>
                <label for="year" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.year != null }">Veröffentlichungsjahr</label>
                <input id="year" type="number" min="1900" :max="new Date().getFullYear()" v-model="song.attributes.year"
                    class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.year != null, 'border-red-500': errorMessages.year != null }"
                    :placeholder="new Date().getFullYear()" />
                <label for="year" class="text-red-500 px-1">{{ errorMessages.year }}</label>
            </div>
            <div>
                <label for="album" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.album != null }">Album</label>
                <input id="album" type="text" v-model="song.attributes.album" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.album != null, 'border-red-500': errorMessages.album != null }"
                    placeholder="Album..." />
                <label for="album" class="text-red-500 px-1">{{ errorMessages.album }}</label>
            </div>
            <div class="md:col-span-2">
                <hr class="my-4 border-gray-200" />
            </div>
            <div>
                <label for="duration" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.duration != null }">Dauer in Minuten <b>*</b></label>
                <input id="duration" type="number" min="1" max="65536" v-model="song.duration" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.duration != null, 'border-red-500': errorMessages.duration != null }"
                    placeholder="6" required />
                <label for="duration" class="text-red-500 px-1">{{ errorMessages.duration }}</label>
            </div>
            <div>
                <label for="rating" class="text-gray-600" :class="{ 'text-red-500': errorMessages.rating != null }">Rating
                    <b>*</b></label>
                <input id="rating" type="number" min="1" max="5" v-model="song.rating" class="input-field" placeholder="3.4"
                    :class="{ 'focus:ring-opacity-0': errorMessages.rating != null, 'border-red-500': errorMessages.rating != null }"
                    required />
                <label for="rating" class="text-red-500 px-1">{{ errorMessages.rating }}</label>
            </div>
            <p><b>Mit einem * versehene Felder, sind Pflichtfelder.</b></p>
            <div class="md:col-span-2">
                <button class="btn" @click="submit()">Speichern</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>