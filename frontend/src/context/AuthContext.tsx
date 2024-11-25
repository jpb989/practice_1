import React, { createContext, useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { refreshTokenRequest } from '../utils/auth';
import { getAccessToken, getRefreshToken } from '../utils/cookies';

interface AuthContextType {
    isAuthenticated: boolean;
    setIsAuthenticated: React.Dispatch<React.SetStateAction<boolean>>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(!!getAccessToken());
    const navigate = useNavigate();

    useEffect(() => {
        const refreshToken = async () => {
            const success = await refreshTokenRequest();
            setIsAuthenticated(success);
            const access = getAccessToken();
            if (!success && access) {
                navigate('/logout');
            }
        };

        refreshToken();
    }, [navigate]);

    return (
        <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
};
