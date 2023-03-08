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
    },
    {
        path: "/effects-library",
        name: "EffectsLibrary",
        component: () => import("./views/EffectsLibrary.vue"),
    },
    {
        path: "/projects",
        name: "Projects",
        component: () => import("./views/ManageProjects.vue"),
        children: [
            {
                path: "",
                name: "NewProject",
                component: () => import("./views/projects/NewProject.vue"),
            },
            {
                path: "import",
                name: "ImportProject",
                component: () => import("./views/projects/ImportProject.vue"),
            }
        ]
    },
    {
        path: "/configs",
        name: "Configs",
        component: () => import("./views/ManageConfigs.vue"),
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;