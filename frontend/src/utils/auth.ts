import api from '../api/apiService';
import { getRefreshToken, setAccessToken } from './cookies';

export const refreshTokenRequest = async (): Promise<boolean> => {
    const token = getRefreshToken();
    if (!token) return false;

    try {
        const response = await api.post('/token/refresh/', { refresh: token });
        setAccessToken(response.data.access);
        return true;
    } catch {
        return false;
    }
};
