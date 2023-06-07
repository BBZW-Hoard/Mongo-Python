<template>
    <div class="flex h-screen">
        <div class="w-64 bg-gray-800 text-white p-4" :class="{ 'hidden': !sidebarOpen }">
            <div class="flex items-center mb-4">
                <button class="mr-2 text-white hover:text-gray-300" @click="sidebarOpen = false">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 30.657 55.657">
                        <line id="Linie_5" data-name="Linie 5" x2="25" y2="25" transform="translate(2.828 2.828)"
                            fill="none" stroke="#fff" stroke-linecap="round" stroke-width="4" />
                        <line id="Linie_6" data-name="Linie 6" x1="25" y2="25" transform="translate(2.828 27.828)"
                            fill="none" stroke="#fff" stroke-linecap="round" stroke-width="4" />
                    </svg>
                </button>
                <span class="text-lg font-semibold">Playlists</span>
            </div>
            <div>
                <button class="flex items-center justify-between w-full mb-2 focus:outline-none" @click="togglePlaylist1">
                    <span class="truncate">
                        Playlist 1
                    </span>
                    <svg class="w-4 h-4 text-gray-400 transform transition-transform"
                        :class="{ 'rotate-180': isPlaylist1Open }" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M4.293 12l4.853-4.853a1 1 0 111.414 1.414L6.414 12l4.646 4.646a1 1 0 11-1.414 1.414L4.293 12zm15.414 0l-4.853 4.853a1 1 0 01-1.414-1.414L17.586 12l-4.646-4.646a1 1 0 011.414-1.414L19.707 12z" />
                    </svg>
                    <svg :class="{ 'rotate-180': isPlaylist1Open }" xmlns="http://www.w3.org/2000/svg" width="16"
                        height="16" viewBox="0 0 55.655 31.657">
                        <line id="Linie_3" data-name="Linie 3" x2="24" y2="26" transform="translate(28.828 2.828)"
                            fill="none" stroke="#fff" stroke-linecap="round" stroke-width="4" />
                        <line id="Linie_4" data-name="Linie 4" x1="26" y2="26" transform="translate(2.828 2.828)"
                            fill="none" stroke="#fff" stroke-linecap="round" stroke-width="4" />
                    </svg>

                </button>
                <div v-show="isPlaylist1Open">
                    <div class="flex items-center mb-2">
                        <span class="truncate">Item 2 with a very long title that gets cut off with three dots</span>
                        <div class="ml-auto flex">
                            <button class="p-1 hover:bg-green-500 rounded-full" title="Play">
                                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 36.266 36.896">
                                    <g id="Polygon_1" data-name="Polygon 1" transform="translate(37 1.448) rotate(90)"
                                        fill="#fff" stroke-linecap="round" stroke-linejoin="round">
                                        <path
                                            d="M 27.4398307800293 35.00000381469727 L 6.56017017364502 35.00000381469727 C 4.450650215148926 35.00000381469727 2.535579919815063 33.92471313476562 1.437360048294067 32.12359237670898 C 0.339139997959137 30.32247352600098 0.2602500021457672 28.12758255004883 1.226320028305054 26.25226402282715 L 11.66615009307861 5.986713409423828 C 12.69958019256592 3.980643272399902 14.74339008331299 2.734453201293945 17 2.734453201293945 C 19.25661087036133 2.734453201293945 21.3004207611084 3.980643272399902 22.3338508605957 5.986713409423828 L 32.773681640625 26.25226402282715 C 33.73974990844727 28.12758255004883 33.66085815429688 30.32247352600098 32.56264114379883 32.12359237670898 C 31.46442031860352 33.92471313476562 29.54935073852539 35.00000381469727 27.4398307800293 35.00000381469727 Z"
                                            stroke="none" />
                                        <path
                                            d="M 17 4.734447479248047 C 15.59436225891113 4.734447479248047 14.18872451782227 5.457172393798828 13.44409942626953 6.902624130249023 L 3.004270553588867 27.16817283630371 C 1.632869720458984 29.83031272888184 3.565549850463867 33.00000381469727 6.560169219970703 33.00000381469727 L 27.4398307800293 33.00000381469727 C 30.43445014953613 33.00000381469727 32.36713027954102 29.83031272888184 30.99572944641113 27.16817283630371 L 20.55590057373047 6.902624130249023 C 19.81127548217773 5.457172393798828 18.40563774108887 4.734447479248047 17 4.734447479248047 M 17 0.7344436645507812 C 20.0088005065918 0.7344436645507812 22.73387908935547 2.396034240722656 24.11178970336914 5.070793151855469 L 34.55162811279297 25.33634185791016 C 35.8397216796875 27.83677291870117 35.73453140258789 30.7632942199707 34.27024078369141 33.1647834777832 C 32.80595016479492 35.5662727355957 30.25252914428711 37.00000381469727 27.4398307800293 37.00000381469727 L 6.560169219970703 37.00000381469727 C 3.747470855712891 37.00000381469727 1.194049835205078 35.5662727355957 -0.2702407836914062 33.1647834777832 C -1.734531402587891 30.7632942199707 -1.8397216796875 27.83677291870117 -0.5516281127929688 25.33635330200195 L 9.888200759887695 5.070793151855469 C 11.26609992980957 2.396041870117188 13.99118041992188 0.7344436645507812 17 0.7344436645507812 Z"
                                            stroke="none" fill="#000" />
                                    </g>
                                </svg>
                            </button>
                            <button class="p-1 hover:bg-red-500 rounded-full ml-2" title="Delete">
                                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 55.657 55.657">
                                    <line id="Linie_1" data-name="Linie 1" x2="50" y2="50"
                                        transform="translate(2.828 2.828)" fill="none" stroke="#fff" stroke-linecap="round"
                                        stroke-width="4" />
                                    <line id="Linie_2" data-name="Linie 2" x2="50" y2="50"
                                        transform="translate(52.828 2.828) rotate(90)" fill="none" stroke="#fff"
                                        stroke-linecap="round" stroke-width="4" />
                                </svg>
                            </button>
                        </div>
                    </div>
                    <!-- Add more items here -->
                </div>
            </div>
            <!-- Add more playlists here -->
        </div>
        <div class="flex-grow bg-gray-100">
            <!-- Content of your website -->
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const sidebarOpen = ref(true);
const isPlaylist1Open = ref(true);

function togglePlaylist1() {
    isPlaylist1Open.value = !isPlaylist1Open.value;
}
</script>

<style scoped></style>