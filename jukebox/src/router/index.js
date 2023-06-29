import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ManageSongView from "../views/ManageSongView.vue";
import ManagePlaylistView from "../views/ManagePlaylistView.vue";
import DeleteSongView from "../views/DeleteSongView.vue";
import DeletePlaylistView from "../views/DeletePlaylistView.vue";
import testView from "../views/testView.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: "/manage-song/:id",
            name: "mangeSong",
            component: ManageSongView
        },
        {
            path: "/manage-playlist/:id",
            name: "managePlaylist",
            component: ManagePlaylistView
        },
        {
            path: "/delete-song/:id",
            name: "deleteSong",
            component: DeleteSongView
        },
        {
            path: "/delete-playlist/:id",
            name: "deletePlaylist",
            component: DeletePlaylistView
        },
        {
            path: "/test",
            name: "test",
            component: testView
        }
    ],
});

export default router;