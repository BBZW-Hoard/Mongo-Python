<script setup>
import { ref, onMounted, watch, inject } from 'vue';
import { useRoute } from 'vue-router';
import { getLocalStorageItems, setLocalStorageItems } from '../service/LocalStorage.ts';
import { config } from '../service/api.ts';
import router from '../router/index.js';
import axios from 'axios';


const route = useRoute();
const id = ref(route.params.id);
const { playlists, getPlaylists } = inject('playlists')

watch(
  () => route.params.id,
  async (newId, oldId) => {
    id.value = route.params.id
    await loadPlaylist()
  }
)

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

async function loadPlaylist(){
    try {
        // loading entry with id from database
        let request = await axios.get(("http://localhost:5000/playlists/" + id.value));
        playlist.value = request.data;
    } catch (e) {
        console.error("error in request:", e);
        router.push({ name: "Error404", params: { pathMatch: "/E404" }, replace: true })
    }
}

/**
 * get playlist object form database, to show all the data to the user
 */
onMounted(async () => {
    await loadPlaylist()
})

/**
 * deletes playlist from backend
 * redirect the homepage with reload to show the changes
 */
async function submit() {
    try {
        // if selectedPlaylist is the one to be deleted, unselect it
        if(await getLocalStorageItems("selectedPlaylist") == playlist.value._id) {
            await setLocalStorageItems("selectedPlaylist", "null");
        }
        
        await axios.delete(('http://localhost:5000/playlists/' + playlist.value._id), config.headers);
    } catch (e) {
        console.error(e); // Handle the error
    }
    await getPlaylists();
    router.push({ path: '/', replace: true });
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