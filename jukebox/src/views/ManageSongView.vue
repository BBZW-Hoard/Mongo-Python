<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { isValidated } from "../service/ValidationSong.ts";
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

const file = ref();
function handleFileUpload(event) {
    file.value = event.target.files[0];
}

async function getFile(songId) {
    let response = await axios.get("http://localhost:5000/files/" + songId);
    return response.data
}
async function submitFile(songId) {
    const configFile = {
        headers: {
            'content-type': 'multipart/form-data',
            'Accept': 'application/json'
        }
    };
    let formData = new FormData();
    formData.append('songId', songId);
    formData.append('file', file.value);
    let response = await axios.post("http://localhost:5000/files", formData, configFile.headers);
    console.log(response.data)
}

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
            debugger;
            router.push({ name: "Error404", params: { pathMatch: "/E404" }, replace: true })
        }
    }

})

async function submit() {
    let validated = true;
    let el = document.getElementById("loadingBar");
    el.classList.toggle("hidden")

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
                let response = await axios.post("http://localhost:5000/songs/", song.value, config.headers);
                await submitFile(response.data._id)
            } catch (e) {
                console.error("error:", e);  // Handle the error
            }
        } else if (requestType.value === "PUT") {
            try {
                let response = await axios.put(('http://localhost:5000/songs/' + song.value._id), song.value, config.headers);
                await submitFile(response.data._id)
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
            <label> Song
                <input type="file" @change="handleFileUpload($event)" />
            </label>
            <p><b>Mit einem * versehene Felder, sind Pflichtfelder.</b></p>
            <div class="md:col-span-2">
                <button class="btn" @click="submit()">Speichern</button>
            </div>
            <div id="loadingBar" role="status"
                class="hidden absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                    viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="currentColor" />
                    <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentFill" />
                </svg>
                <span class="sr-only">Loading...</span>
            </div>
        </div>
    </div>
</template>

<style scoped></style>