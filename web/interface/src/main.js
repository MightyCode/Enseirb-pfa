import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import store from './store';
import ScaleLoader from 'vue-spinner/src/ScaleLoader.vue';

createApp(App)
    .use(router)
    .use(store)
    .component('ScaleLoader', ScaleLoader)
    .mount('#app');
