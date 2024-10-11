import axios, { AxiosInstance } from "axios";

const djangoAxiosInst: AxiosInstance = axios.create({
    baseURL: process.env.NEXT_PUBLIC_DJANGO_API_URL,
    timeout: 2500,
});

const fastapiAxiosInst: AxiosInstance = axios.create({
    baseURL: process.env.NEXT_PUBLIC_FAST_API_URL,
    timeout: 2500,
});

export default { djangoAxiosInst, fastapiAxiosInst };
