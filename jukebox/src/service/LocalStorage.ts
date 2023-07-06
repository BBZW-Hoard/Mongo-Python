/**
 * Zur überprüfung, ob ein Item im Local Storage existiert, wenn nicht wird es mit 0 als Wert erstellt 
 * @param { string } item variable, die überprüft wird
 * @param { string } value wert des items
 * @returns string -> value
 */
export async function getLocalStorageItems(item: string) {
    let value: string = "";
    if (localStorage.getItem(item)) value = localStorage.getItem(item);
    else {
        setLocalStorageItems(item, "0");
        value = "0";
    }

    return value;
}

/**
 * Zur erstellung eines Local Storage Items
 * @param { string } item variable, die aktualisiert wird
 * @param { string } value wert des items
 * @returns boolean
 */
export async function setLocalStorageItems(item: string, value: string) {
    localStorage.setItem(item, value);
    return true;
}