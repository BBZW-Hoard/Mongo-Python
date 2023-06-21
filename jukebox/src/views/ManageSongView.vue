<script setup>
import { ref, defineProps } from 'vue';
import Toast from "../components/Toast.vue";
import router from '../router/index.js';

defineProps({
    name: {
        type: String,
        required: false,
    },
    composer: {
        type: String,
        required: false,
    },
    genre: {
        type: String,
        required: false,
    },
    interpret: {
        type: String,
        required: false,
    },
    year: {
        type: Number,
        required: false,
    },
    album: {
        type: String,
        required: false,
    },
    duration: {
        type: Number,
        required: false
    },
    rating: {
        type: Number,
        required: false
    }
})

/* const _attributes = ref({
    composer: "",
    genre: "",
    interpret: "",
    year: 0,
    album: ""
}); */

const Error = ref(false);
const errorMsg = ref("");

/* data */
const _name = ref("");
const _duration = ref();
const _rating = ref();
/* attributes */
const _composer = ref("");
const _genre = ref("");
const _interpret = ref("");
const _year = ref();
const _album = ref("");

function submit() {
    if (_name.value.trim().length === 0) {
        return "Name ist ein Pflichtfeld.";
    } else if (_name.value.length < 3 || _name.value.length > 25) {
        return "Der Name muss mehr als 3 und weniger als 25 Zeichen haben.";
    } else if (_duration.value == null) {
        return "Dauer ist ein Pflichtfeld.";
    } else if (_duration.value == 0) {
        return "Dauer kann nicht 0 sein.";
    } else if (_rating.value == null) {
        return "Rating ist ein Pflichtfeld.";
    } else if (_rating.value < 1 || _rating.value > 5) {
        return "Rating kann nicht weniger als 1 oder mehr als 5 sein.";
    }

    return false;
}
</script>

<template>
    <div class="container mx-auto p-4">
        <Toast v-if="errorMsg.trim().length != 0" :isError="Error" :errorMessage="errorMsg" />
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="name" class="text-gray-600">Name <b>*</b></label>
                <input id="name" type="text" v-model="_name" class="input-field" placeholder="Name..." required />
            </div>
            <div>
                <label for="composer" class="text-gray-600">Komponist</label>
                <input id="composer" type="text" v-model="_composer" class="input-field" placeholder="Komponist..." />
            </div>
            <div>
                <label for="genre" class="text-gray-600">Genre</label>
                <input id="genre" type="text" v-model="_genre" class="input-field" placeholder="Genre..." />
            </div>
            <div>
                <label for="interpret" class="text-gray-600">Interpret</label>
                <input id="interpret" type="text" v-model="_interpret" class="input-field" placeholder="Interpret..." />
            </div>
            <div>
                <label for="year" class="text-gray-600">Veröffentlichungsjahr</label>
                <input id="year" type="number" min="1900" :max="new Date().getFullYear()" v-model="_year"
                    class="input-field" :placeholder="new Date().getFullYear()" />
            </div>
            <div>
                <label for="album" class="text-gray-600">Album</label>
                <input id="album" type="text" v-model="_album" class="input-field" placeholder="Album..." />
            </div>
            <div class="md:col-span-2">
                <hr class="my-4 border-gray-200" />
            </div>
            <div>
                <label for="duration" class="text-gray-600">Dauer in Minuten <b>*</b></label>
                <input id="duration" type="number" min="1" max="65536" v-model="_duration" class="input-field"
                    placeholder="6" required />
            </div>
            <div>
                <label for="rating" class="text-gray-600">Rating <b>*</b></label>
                <input id="rating" type="number" min="1" max="5" v-model="_rating" class="input-field" placeholder="3.4"
                    required />
            </div>
            <p><b>Mit einem * versehene Felder, sind Pflichtfelder.</b></p>
            <div class="md:col-span-2">
                <button class="btn" @click="submit()">Speichern</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>