import React, { createContext, useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { refreshTokenRequest } from '../utils/auth';
import { getAccessToken } from '../utils/cookies';

interface AuthContextType {
    isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(!!getAccessToken());
    const navigate = useNavigate();

    useEffect(() => {
        const refreshToken = async () => {
            const success = await refreshTokenRequest();
            setIsAuthenticated(success);
            if (!success) navigate('/login');
        };
        
        refreshToken();
    }, [navigate]);

    return (
        <AuthContext.Provider value={{ isAuthenticated }}>
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
