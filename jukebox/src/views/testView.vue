<script setup>
import { ref } from 'vue';
import axios from 'axios';
const file = ref();
function handleFileUpload(event) {
    file.value = event.target.files[0];
}
const config = {
    headers: {
        'content-type': 'multipart/form-data',
        'Accept': 'application/json'
    }
};

async function submitFile() {
    let formData = new FormData();
    formData.append('file', file.value);
    let response = await axios.post("http://localhost:5000/files", formData, config.headers);
    console.log(response.data)
}
</script>

<template>
    <div class="container">
        <div>
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