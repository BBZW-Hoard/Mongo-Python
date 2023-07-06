import { ref } from 'vue';
import router from '../router/index.js';
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

/**
 * Sets the value of the file reference based on the uploaded file from the event.
 * @param {Event} event - The file upload event containing the selected file.
 */
export function handleFileUpload(event: any): void {
    file.value = event.target.files[0];
}

/**
 * Retrieves the file associated with the specified song Id from the backend.
 * @param {string} songId - The Id of the song to fetch the file for.
 * @returns {Promise<any>} - A promise that resolves to the fetched file data.
 */
export async function getFile(songId: string): Promise<any> {
    let response = await axios.get("http://localhost:5000/files/" + songId);

    return response.data;
}

/**
 * Submits the file associated with the specified song Id to the backend.
 * @param {string} songId - The Id of the song to submit the file for.
 */
export async function submitFile(songId: string): Promise<void> {
    if (file.value == null) {
        return
    }

    let formData = new FormData();

    formData.append('songId', songId);
    formData.append('file', file.value);

    await axios.post("http://localhost:5000/files", formData, configFile.headers);
}

/**
 * returns the song / playlist object that will be edited
 * if the song can't be found in database, redirect to E404 page
 * @param id id of the object or 0 -> if 0, a new object will be generated
 * @param object edited object
 * @param requestType POST or PUT request (defined by id)
 * @param url url of the request (songs / playlists)
 */
export async function prepareForEdit(id: number, object: any, requestType: any, url: string): Promise<void> {
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

/**
 * Submits a POST or PUT request with the provided object data.
 * Performs validation on the object data and updates error messages accordingly.
 * Navigates to the root URL ("/") after successful submission.
 * @param errorMessages error messages array with strings
 * @param requestType POST or PUT request (defined by Id)
 * @param object submited object
 * @param router vue router class
 * @param url url of the request (songs / playlists)
 * @returns {Promise<void>} - A promise that resolves once the submission process is complete.
 */
export async function submit(errorMessages: any, requestType: any, object: any, url: string): Promise<void> {
    let validated: any = true;

    /* set all key-values from errorMessages to null */
    try {
        Object.assign(errorMessages.value, Object.fromEntries(Object.keys(errorMessages.value).map(key => [key, null])));
    } catch (e) {
        console.error("Could not clear values from errorMessages object", e);
    }

    let result: any = "";
    if (url == "songs") result = isValidatedSong(object.value);
    else result = isValidatedPlaylist(object.value);

    validated = result[0];
    errorMessages.value = result[1];

    if (validated) {
        if (requestType.value === "POST") {
            try {
                let response = await axios.post(`http://localhost:5000/${url}/`, object.value, config.headers);
                if (url == "songs") await submitFile(response.data._id)
            } catch (e) {
                console.error("error:", e);  // Handle the error
            }
        } else if (requestType.value === "PUT") {
            try {
                let response = await axios.put((`http://localhost:5000/${url}/${object.value._id}`), object.value, config.headers);
                if (url == "songs") await submitFile(response.data._id)
            } catch (e) {
                console.error("error:", e); // Handle the error
            }
        } else {
            console.error("Can't make request; Unknown requestType:", requestType.value);
        }

        router.push({ path: '/' })
    }
}