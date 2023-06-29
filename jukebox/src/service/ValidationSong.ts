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

class ErrorMessages {
    name: string | null;
    composer: string | null;
    genre: string | null;
    interpret: string | null;
    year: string | null;
    album: string | null;
    duration: string | null;
    rating: string | null;
}

const errorMessages: ErrorMessages = {
    name: null,
    composer: null,
    genre: null,
    interpret: null,
    year: null,
    album: null,
    duration: null,
    rating: null
}

/**
 * Function to validate a song object.

 * @param { Song } song - The song object to be validated.
 * @returns { Array } - An array containing a boolean value indicating whether the song is valid or not, and an object containing error messages if any.
 */
export function isValidated(song: Song): (boolean | ErrorMessages)[] {
    let attributesLengthMsg = " muss weniger als 30 Zeichen haben!";
    let has2beString = " muss ein String sein!";
    let has2beNumber = " muss eine Zahl sein!";
    let requiredField = " ist ein Pflichtfeld!";

    // name
    if (song.name.trim().length === 0) {
        errorMessages.name = "Name" + requiredField;
        return [false, errorMessages];
    } else if (typeof (song.name) != "string") {
        errorMessages.name = "Name" + has2beString;
        return [false, errorMessages];
    } else if (song.name.length < 3) {
        errorMessages.name = "Der Name muss mehr als 3 Zeichen haben!";
        return [false, errorMessages];
    } else if (song.name.length > 25) {
        errorMessages.name = "Der Name muss weniger als 25 Zeichen haben!";
        return [false, errorMessages];
    }

    // composer
    if (typeof (song.attributes.composer) != "string") {
        errorMessages.composer = "Komponist" + has2beString;
        return [false, errorMessages];
    } else if (song.attributes.composer.length > 30) {
        errorMessages.composer = "Der Komponist" + attributesLengthMsg;
        return [false, errorMessages];
    }

    // genre
    if (typeof (song.attributes.genre) != "string") {
        errorMessages.genre = "Genre" + has2beString;
        return [false, errorMessages];
    } else if (song.attributes.genre.length > 30) {
        errorMessages.genre = "Das Genre" + attributesLengthMsg;
        return [false, errorMessages];
    }

    // interpret
    if (typeof (song.attributes.interpret) != "string") {
        errorMessages.interpret = "Interpret" + has2beString;
        return [false, errorMessages];
    } else if (song.attributes.interpret.length > 30) {
        errorMessages.interpret = "Der Interpret" + attributesLengthMsg;
        return [false, errorMessages];
    }

    // year
    if (typeof (song.attributes.year) != "number") {
        errorMessages.year = "Jahr" + has2beNumber;
        return [false, errorMessages];
    } else if (song.attributes.year > new Date().getFullYear()) {
        errorMessages.year = "Das aktuelle Jahr kann nicht überstiegen werden!";
        return [false, errorMessages];
    } else if (song.attributes.year < 1900) {
        errorMessages.year = "Das Jahr muss über 1900 liegen!";
        return [false, errorMessages];
    }

    // album
    if (typeof (song.attributes.album) != "string") {
        errorMessages.album = "Album" + has2beString;
        return [false, errorMessages];
    } else if (song.attributes.album.length > 30) {
        errorMessages.album = "Das Album" + attributesLengthMsg;
        return [false, errorMessages];
    }

    // duration
    if (song.duration === null) {
        errorMessages.duration = "Dauer" + requiredField;
        return [false, errorMessages];
    } else if (typeof (song.duration) != "number") {
        errorMessages.duration = "Dauer" + has2beNumber;
        return [false, errorMessages];
    } else if (song.duration < 1) {
        errorMessages.duration = "Dauer muss mind. 1 sein!";
        return [false, errorMessages];
    } else if (song.duration > 65536) {
        errorMessages.duration = "Dauer muss kann nicht mehr als 65536 sein!";
        return [false, errorMessages];
    }

    // rating
    if (song.rating === null) {
        errorMessages.rating = "Rating" + requiredField;
        return [false, errorMessages];
    } else if (typeof (song.rating) != "number") {
        errorMessages.rating = "Raiting" + has2beNumber;
        return [false, errorMessages];
    } else if (song.rating < 1) {
        errorMessages.rating = "Rating muss mind. 1 sein!";
        return [false, errorMessages];
    } else if (song.rating > 5) {
        errorMessages.rating = "Dauer muss kann nicht mehr als 5 sein!";
        return [false, errorMessages];
    }

    return [true, errorMessages];
}
