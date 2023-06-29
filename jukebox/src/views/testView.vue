<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
const fileGet = ref();
const file = ref();
const songId = "2"
function handleFileUpload(event) {
    file.value = event.target.files[0];
}
const config = {
    headers: {
        'content-type': 'multipart/form-data',
        'Accept': 'application/json'
    }
};
async function getFile() {
    let response = await axios.get("http://localhost:5000/files/" + songId);
    return response.data
}
async function submitFile() {
    let formData = new FormData();
    formData.append('songId', songId);
    formData.append('file', file.value);
    let response = await axios.post("http://localhost:5000/files", formData, config.headers);
    console.log(response.data)
    fileGet.value = await getFile()
}

</script>

<template>
    <div class="container">
        <div>
            <div>
                File: {{ fileGet }}
            </div>
            <h2>Single File</h2>
            <hr />
            <label>File
                <input type="file" @change="handleFileUpload($event)" />
            </label>
            <br>
            <button v-on:click="submitFile()">Submit</button>
        </div>
    </div>
</template>

<style scoped></style>