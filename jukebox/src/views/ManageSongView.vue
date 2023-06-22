<script setup>
import { ref, defineProps, onMounted, reactive } from 'vue';

const props = defineProps({
    id: {
        type: Number,
        required: true,
    }
})

let { id } = reactive(props);
const requestType = ref("");
const song = ref({
    id: 0,
    name: "",
    attributes: {
        composer: "",
        genre: "",
        interpret: "",
        year: new Date().getFullYear(), // number
        album: ""
    },
    duration: 6,
    rating: 3.4
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

onMounted(() => {
    if (id == 0) {
        console.log("new Song");
        requestType.value = "POST";
    } else {
        console.log("edit song with id:", id);
        requestType.value = "PUT";
    }
})

function submit() {
    let attributesLengthMsg = " muss weniger als 30 Zeichen haben!";
    let has2beString = " muss ein String sein!";
    let has2beNumber = " muss eine Zahl sein!";
    let requiredField = " ist ein Pflichtfeld!";

    /* set all key-values from errorMessages to null */
    try {
        Object.assign(errorMessages.value, Object.fromEntries(Object.keys(errorMessages.value).map(key => [key, null])));
    } catch (e) {
        console.error("Could not clear values from errorMessages object", e);
    }

    do {
        // name
        if (song.value.name.trim().length === 0) {
            errorMessages.value.name = "Name" + requiredField;
            continue;
        } else if (typeof (song.value.name) != "string") {
            errorMessages.value.name = "Name" + has2beString;
            continue;
        } else if (song.value.name.length < 3 || song.value.name.length > 25) {
            errorMessages.value.name = "Der Name muss mehr als 3 und weniger als 25 Zeichen haben!";
            continue;
        }

        // composer
        if (typeof (song.value.attributes.composer) != "string") {
            errorMessages.value.composer = "Komponist" + has2beString;
            continue;
        } else if (song.value.attributes.composer.length > 30) {
            errorMessages.value.composer = "Der Komponist" + attributesLengthMsg;
            continue;
        }

        // genre
        if (typeof (song.value.attributes.genre) != "string") {
            errorMessages.value.genre = "Genre" + has2beString;
            continue;
        } else if (song.value.attributes.genre.length > 30) {
            errorMessages.value.genre = "Das Genre" + attributesLengthMsg;
            continue;
        }

        // interpret
        if (typeof (song.value.attributes.interpret) != "string") {
            errorMessages.value.interpret = "Interpret" + has2beString;
            continue;
        } else if (song.value.attributes.interpret.length > 30) {
            errorMessages.value.interpret = "Der Interpret" + attributesLengthMsg;
            continue;
        }

        // year
        if (typeof (song.value.attributes.year) != "number") {
            errorMessages.value.year = "Jahr" + has2beNumber;
            continue;
        } else if (song.value.attributes.year > new Date().getFullYear()) {
            errorMessages.value.year = "Das aktuelle Jahr kann nicht überstiegen werden!";
            continue;
        } else if (song.value.attributes.year < 1900) {
            errorMessages.value.year = "Das Jahr muss über 1900 liegen!";
            continue;
        }

        // album
        if (typeof (song.value.attributes.album) != "string") {
            errorMessages.value.album = "Album" + has2beString;
            continue;
        } else if (song.value.attributes.album.length > 30) {
            errorMessages.value.album = "Das Album" + attributesLengthMsg;
            continue;
        }

        // duration
        if (song.value.duration === null) {
            errorMessages.value.duration = "Dauer" + requiredField;
            continue;
        } else if (typeof (song.value.duration) != "number") {
            errorMessages.value.duration = "Dauer" + has2beNumber;
            continue;
        } else if (song.value.duration < 1) {
            errorMessages.value.duration = "Dauer muss mind. 1 sein!";
            continue;
        } else if (song.value.duration > 65536) {
            errorMessages.value.duration = "Dauer muss kann nicht mehr als 65536 sein!";
            continue;
        }

        // rating
        if (song.value.rating === null) {
            errorMessages.value.rating = "Rating" + requiredField;
            continue;
        } else if (typeof (song.value.rating) != "number") {
            errorMessages.value.rating = "Raiting" + has2beNumber;
            continue;
        } else if (song.value.rating < 1) {
            errorMessages.value.rating = "Rating muss mind. 1 sein!";
            continue;
        } else if (song.value.rating > 5) {
            errorMessages.value.rating = "Dauer muss kann nicht mehr als 5 sein!";
            continue;
        }

        // validated
        alert("validated");
        if (requestType.value === "POST") {

        } else if (requestType.value === "PUT") {

        } else {
            console.error("Can't make request; Unknown requestType:", requestType.value);
        }
    } while (false);
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