class Song {
    name: string;
    attributes: {
        composer: string;
        genre: string;
        interpret: string;
        year: number;
        album: string;
    };
    duration: number;
    rating: number;
}

class Playlist {
    name: String;
    Songs: Song[];
}

class ErrorMessages {
    name: string | null;
}

const errorMessages: ErrorMessages = {
    name: null
}

/**
 * Function to validate a song object.

 * @param { Playlist } playlist - The playlist object to be validated.
 * @returns { Array } - An array containing a boolean value indicating whether the song is valid or not, and an object containing error messages if any.
 */
export function isValidated(playlist: Playlist): (boolean | ErrorMessages)[] {
    let has2beString = " muss ein String sein!";
    let requiredField = " ist ein Pflichtfeld!";

    // name
    if (playlist.name.trim().length === 0) {
        errorMessages.name = "Name" + requiredField;
        return [false, errorMessages];
    } else if (typeof (playlist.name) != "string") {
        errorMessages.name = "Name" + has2beString;
        return [false, errorMessages];
    } else if (playlist.name.length < 3) {
        errorMessages.name = "Der Name muss mehr als 3 Zeichen haben!";
        return [false, errorMessages];
    } else if (playlist.name.length > 25) {
        errorMessages.name = "Der Name muss weniger als 25 Zeichen haben!";
        return [false, errorMessages];
    }

    return [true, errorMessages];
}