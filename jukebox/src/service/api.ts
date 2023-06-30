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

export async function prepareForEdit(id: number, object: any, requestType: any, router: any, url: string) {
    if (id == 0) {   // create new entry
        requestType.value = "POST";
    } else {
        requestType.value = "PUT";
        try {
            // loading entry with id from database
            let request = await axios.get((`http://localhost:5000/${url}/${id}`));
            object.value = request.data;
        } catch (e) {
            console.error("error in request:", e);
            router.push({ name: "Error404", params: { pathMatch: "/E404" }, replace: true })
        }
    }
}