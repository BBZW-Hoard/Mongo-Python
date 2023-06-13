<script setup>
import { onMounted } from 'vue';


onMounted(async () => {
    await getLocalStorageItems("selectedPlaylist");
})

/**
 * Zur überprüfung, ob ein Item im Local Storage existiert, wenn nicht wird es mit 0 als Wert erstellt 
 * @param { string } item variable, die überprüft wird
 * @param { string } value wert des items
 * @returns string -> value
 */
async function getLocalStorageItems(item) {
    let value = "";
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
async function setLocalStorageItems(item, value) {
    localStorage.setItem(item, value);
    return true;
}

</script>

<template></template>

<style scoped></style>