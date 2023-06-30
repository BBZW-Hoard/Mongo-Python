<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { isValidated } from "../service/ValidationPlaylist.ts";
import router from '../router/index.js';
import axios from 'axios';
import { prepareForEdit, config } from "../service/api.ts"


const route = useRoute();
const id = route.params.id;

const requestType = ref("");
const playlist = ref({
    name: "",
    songs: []
})

const errorMessages = ref({
    name: null
})

onMounted(async () => {
    prepareForEdit(id, playlist, requestType, route, "playlists")
})

async function submit() {
    let validated = true;

    /* set all key-values from errorMessages to null */
    try {
        Object.assign(errorMessages.value, Object.fromEntries(Object.keys(errorMessages.value).map(key => [key, null])));
    } catch (e) {
        console.error("Could not clear values from errorMessages object", e);
    }

    let result = isValidated(playlist.value);
    validated = result[0];
    errorMessages.value = result[1];

    if (validated) {
        // validated
        alert("validated");

        if (requestType.value === "POST") {
            try {
                await axios.post("http://localhost:5000/playlists/", playlist.value, config.headers);
            } catch (e) {
                console.error("error:", e);  // Handle the error
            }
        } else if (requestType.value === "PUT") {
            try {
                await axios.put(('http://localhost:5000/playlists/' + playlist.value._id), playlist.value, config.headers);
            } catch (e) {
                console.error("error:", e); // Handle the error
            }
        } else {
            console.error("Can't make request; Unknown requestType:", requestType.value);
        }

        window.location.href = "/";
    }
}
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="grid grid-cols-1 gap-4">
            <div>
                <label for="name" class="text-gray-600" :class="{ 'text-red-500': errorMessages.name != null }">Name
                    <b>*</b></label>
                <input id="name" type="text" v-model="playlist.name" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.name != null, 'border-red-500': errorMessages.name != null }"
                    placeholder="Name..." required />
                <label for="name" class="text-red-500 px-1">{{ errorMessages.name }}</label>
            </div>
            <div class="md:col-span-2">
                <hr class="my-4 border-gray-200" />
            </div>
            <p><b>Mit einem * versehene Felder, sind Pflichtfelder.</b></p>
            <div class="md:col-span-2">
                <button class="btn" @click="submit()">Speichern</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>