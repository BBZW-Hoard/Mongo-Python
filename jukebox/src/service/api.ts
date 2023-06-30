import { ref } from 'vue';
import axios from 'axios';
import { isValidated as isValidatedSong } from "./ValidationSong";
import { isValidated as isValidatedPlaylist } from "./ValidationPlaylist";

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

export async function submit(errorMessages: any, requestType: any, object: any, router: any, url: string) {
    let validated: any = true;

    /* set all key-values from errorMessages to null */
    try {
        Object.assign(errorMessages.value, Object.fromEntries(Object.keys(errorMessages.value).map(key => [key, null])));
    } catch (e) {
        console.error("Could not clear values from errorMessages object", e);
    }

    let result
    if (url == "songs")
        result = isValidatedSong(object.value);
    else
        result = isValidatedPlaylist(object.value);

    validated = result[0];
    errorMessages.value = result[1];

    if (validated) {
        // validated
        alert("validated");

        if (requestType.value === "POST") {
            try {
                let response = await axios.post(`http://localhost:5000/${url}/`, object.value, config.headers);
                if (url == "songs")
                    await submitFile(response.data._id)
            } catch (e) {
                console.error("error:", e);  // Handle the error
            }
        } else if (requestType.value === "PUT") {
            try {
                let response = await axios.put((`http://localhost:5000/${url}/${object.value._id}`), object.value, config.headers);
                if (url == "songs")
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