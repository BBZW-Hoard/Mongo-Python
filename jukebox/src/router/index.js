import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ListsView from "../views/ListsView.vue";
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
            path: "/lists",
            name: "lists",
            component: ListsView
        },
        {
            path: "/test",
            name: "test",
            component: testView
        }
    ],
});

export default router;