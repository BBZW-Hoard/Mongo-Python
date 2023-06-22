<script setup>
import { ref, defineProps, onMounted, reactive } from 'vue';

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


    if (id == 0) {
        console.log("new Song");
    } else {
        console.log("edit song with id:", id);
    }
})

function submit() {    
    if (song.value.name.trim().length === 0) errorMsg.value = "Name ist ein Pflichtfeld!";
    else if (song.value.name.length < 3 || song.value.name.length > 25) errorMsg.value = "Der Name muss mehr als 3 und weniger als 25 Zeichen haben!";
    else if (song.value.duration == null) errorMsg.value = "Dauer ist ein Pflichtfeld!";
    else if (song.value.duration == 0) errorMsg.value = "Dauer muss eine Zahl sein!";
    else if (song.value.rating == null) errorMsg.value = "Rating ist ein Pflichtfeld!";
    else if (song.value.rating == 0) errorMsg.value = "Rating muss eine Zahl sein!";
    else if (song.value.rating < 1 || song.value.rating > 5) errorMsg.value = "Rating kann nicht weniger als 1 oder mehr als 5 sein!";
    else {
        errorMsg.value = "validated";
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
                    :class="{ 'text-red-500': errorMessages.attributes.composer != null }">Komponist</label>
                <input id="composer" type="text" v-model="song.composer" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.attributes.composer != null, 'border-red-500': errorMessages.attributes.composer != null }"
                    placeholder="Komponist..." />
                <label for="composer" class="text-red-500 px-1">{{ errorMessages.attributes.composer }}</label>
            </div>
            <div>
                <label for="genre" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.attributes.genre != null }">Genre</label>
                <input id="genre" type="text" v-model="song.genre" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.attributes.genre != null, 'border-red-500': errorMessages.attributes.genre != null }"
                    placeholder="Genre..." />
                <label for="genre" class="text-red-500 px-1">{{ errorMessages.attributes.genre }}</label>
            </div>
            <div>
                <label for="interpret" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.attributes.interpret != null }">Interpret</label>
                <input id="interpret" type="text" v-model="song.interpret" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.attributes.interpret != null, 'border-red-500': errorMessages.attributes.interpret != null }"
                    placeholder="Interpret..." />
                <label for="interpret" class="text-red-500 px-1">{{ errorMessages.attributes.interpret }}</label>
            </div>
            <div>
                <label for="year" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.attributes.year != null }">Veröffentlichungsjahr</label>
                <input id="year" type="number" min="1900" :max="new Date().getFullYear()" v-model="song.year"
                    class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.attributes.year != null, 'border-red-500': errorMessages.attributes.year != null }"
                    :placeholder="new Date().getFullYear()" />
                <label for="year" class="text-red-500 px-1">{{ errorMessages.attributes.year }}</label>
            </div>
            <div>
                <label for="album" class="text-gray-600"
                    :class="{ 'text-red-500': errorMessages.attributes.album != null }">Album</label>
                <input id="album" type="text" v-model="song.album" class="input-field"
                    :class="{ 'focus:ring-opacity-0': errorMessages.attributes.album != null, 'border-red-500': errorMessages.attributes.album != null }"
                    placeholder="Album..." />
                <label for="album" class="text-red-500 px-1">{{ errorMessages.attributes.album }}</label>
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