import { createRouter, createWebHashHistory } from "vue-router";
import store from "./store";

const routes = [
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
        path: "/vis-project",
        name: "VisualizeProject",
        component: () => import("./views/VisualizeProject.vue"),
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
                meta: {
                    doesNotRequireProject: true
                }
            },
            {
                path: "import",
                name: "ImportProject",
                component: () => import("./views/projects/ImportProject.vue"),
                meta: {
                    doesNotRequireProject: true
                }
            }
        ],
        meta: {
            doesNotRequireProject: true
        }
    },
    {
        path: "/configs",
        name: "Configs",
        component: () => import("./views/ManageConfigs.vue"),
        children: [
            {
                path: "",
                name: "NewConfig",
                component: () => import("./views/configs/NewConfig.vue"),
                meta: {
                    doesNotRequireConfig: true,
                    doesNotRequireProject: true
                }
            },
            {
                path: "import",
                name: "ImportConfig",
                component: () => import("./views/configs/ImportConfig.vue"),
                meta: {
                    doesNotRequireConfig: true,
                    doesNotRequireProject: true
                }
            }
        ],
        meta: {
            doesNotRequireConfig: true,
            doesNotRequireProject: true
        }
    },
    {
        path: "/configs/env",
        name: "ConfigEnv",
        component: () => import("./views/configs/ConfigEnv.vue"),
        meta: {
            doesNotRequireProject: true
        }
    },
    {
        // Redirect to /projects
        path: "/",
        redirect: "/edit-project",
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    // If no active config, and /configs is not in the path, redirect to /configs
    if (store.state.activeConfig === null && to.meta.doesNotRequireConfig !== true) {
        next({ path: "/configs/" });
    } else if (store.state.activeConfig !== null && store.state.activeProject === null && to.meta.doesNotRequireProject !== true) {
        next({ path: "/projects/" });
    } else {
        next();
    }
});


export default router;