import React, { createContext, useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/apiService';
import { getAccessToken, setAccessToken, getRefreshToken } from '../utils/cookies';

interface AuthContextType {
    isAuthenticated: boolean;
    refreshToken: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(!!getAccessToken());
    const navigate = useNavigate();

    const refreshToken = async () => {
        const token = getRefreshToken();
        if (!token) {
            setIsAuthenticated(false);
            navigate('/login');
            return;
        }
        
        try {
            const response = await api.post('/api/token/refresh', { refresh: token });
            setAccessToken(response.data.access);
            setIsAuthenticated(true);
        } catch (error) {
            console.error("Failed to refresh token", error);
            setIsAuthenticated(false);
            navigate('/login');
        }
    };

    useEffect(() => {
        refreshToken();
    }, []);

    return (
        <AuthContext.Provider value={{ isAuthenticated, refreshToken }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider");
    }
    return context;
};
