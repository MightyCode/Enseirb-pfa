import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
    {
        path: "/",
        name: "Home",
        component: () => import("./views/Home.vue"),
    },
    {
        path: "/new-project",
        name: "NewProject",
        component: () => import("./views/NewProject.vue"),
    },
    {
        path: "/edit-project",
        name: "EditProject",
        component: () => import("./views/EditProject.vue"),
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;