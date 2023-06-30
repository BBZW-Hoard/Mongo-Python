import { ref } from 'vue';
import axios from 'axios';

// axios headers config
export const config: any = {
    headers: {
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
};

const configFile: any = {
    headers: {
        'content-type': 'multipart/form-data',
        'Accept': 'application/json'
    }
};

const file = ref();
export function handleFileUpload(event) {
    file.value = event.target.files[0];
}

export async function getFile(songId) {
    let response = await axios.get("http://localhost:5000/files/" + songId);
    return response.data
}

export async function submitFile(songId) {

    let formData = new FormData();
    formData.append('songId', songId);
    formData.append('file', file.value);
    let response = await axios.post("http://localhost:5000/files", formData, configFile.headers);
    console.log(response.data)
}