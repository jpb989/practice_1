/// <reference types="vite/client" />

import axios, { AxiosError, InternalAxiosRequestConfig } from "axios";
import { getAccessToken } from '../utils/cookies';
import { useAuth } from '../context/AuthContext';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

const addBearerToken = (config: InternalAxiosRequestConfig) => {
    const token = getAccessToken();
    if (token && config.headers) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
};

api.interceptors.request.use(
    (config) => addBearerToken(config),
    (error: AxiosError) => Promise.reject(error)
);

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const { refreshToken } = useAuth();
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            await refreshToken();
            addBearerToken(originalRequest);
            return api(originalRequest);
        }

        return Promise.reject(error);
    }
);

export default api;
