<script setup>
import { ref, defineProps, onMounted, reactive } from 'vue';
import Toast from "../components/Toast.vue";
import router from '../router/index.js';

const props = defineProps({
    id: {
        type: Number,
        required: true,
    }
})

let { id } = reactive(props);
const song = ref({
    id: 0,
    name: "",
    attributes: {
        composer: null,
        genre: null,
        interpret: null,
        year: null,
        album: null
    },
    duration: null,
    rating: null
})

onMounted(() => {
    id = Math.round(Math.random() * 13 + 1);
   

    if(id == 0) {
        console.log("new Song");
    } else {
        console.log("edit song with id:", id);
    }
})

const Error = ref(false);
const errorMsg = ref("");

function submit() {
    Error.value = true;

    if (song.value.name.trim().length === 0) errorMsg.value = "Name ist ein Pflichtfeld!";
    else if (song.value.name.length < 3 || song.value.name.length > 25) errorMsg.value = "Der Name muss mehr als 3 und weniger als 25 Zeichen haben!";
    else if (song.value.duration == null) errorMsg.value = "Dauer ist ein Pflichtfeld!";
    else if (song.value.duration == 0) errorMsg.value = "Dauer muss eine Zahl sein!";
    else if (song.value.rating == null) errorMsg.value = "Rating ist ein Pflichtfeld!";
    else if (song.value.rating == 0) errorMsg.value = "Rating muss eine Zahl sein!";
    else if (song.value.rating < 1 || song.value.rating > 5) errorMsg.value = "Rating kann nicht weniger als 1 oder mehr als 5 sein!";
    else {
        Error.value = false;
        errorMsg.value = "validated";
    }
}
</script>

<template>
    <div class="container mx-auto p-4">
        <Toast v-if="errorMsg.trim().length != 0" :isError="Error" :errorMessage="errorMsg" />
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="name" class="text-gray-600">Name <b>*</b></label>
                <input id="name" type="text" v-model="song.name" class="input-field" placeholder="Name..." required />
            </div>
            <div>
                <label for="composer" class="text-gray-600">Komponist</label>
                <input id="composer" type="text" v-model="song.composer" class="input-field" placeholder="Komponist..." />
            </div>
            <div>
                <label for="genre" class="text-gray-600">Genre</label>
                <input id="genre" type="text" v-model="song.genre" class="input-field" placeholder="Genre..." />
            </div>
            <div>
                <label for="interpret" class="text-gray-600">Interpret</label>
                <input id="interpret" type="text" v-model="song.interpret" class="input-field" placeholder="Interpret..." />
            </div>
            <div>
                <label for="year" class="text-gray-600">Veröffentlichungsjahr</label>
                <input id="year" type="number" min="1900" :max="new Date().getFullYear()" v-model="song.year"
                    class="input-field" :placeholder="new Date().getFullYear()" />
            </div>
            <div>
                <label for="album" class="text-gray-600">Album</label>
                <input id="album" type="text" v-model="song.album" class="input-field" placeholder="Album..." />
            </div>
            <div class="md:col-span-2">
                <hr class="my-4 border-gray-200" />
            </div>
            <div>
                <label for="duration" class="text-gray-600">Dauer in Minuten <b>*</b></label>
                <input id="duration" type="number" min="1" max="65536" v-model="song.duration" class="input-field"
                    placeholder="6" required />
            </div>
            <div>
                <label for="rating" class="text-gray-600">Rating <b>*</b></label>
                <input id="rating" type="number" min="1" max="5" v-model="song.rating" class="input-field" placeholder="3.4"
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