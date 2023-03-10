import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://' + import.meta.env.VITE_BACKEND_ADDRESS,
});

export default axiosInstance;