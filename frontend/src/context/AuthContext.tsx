import React, { createContext, useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { refreshTokenRequest } from '../utils/auth';
import { getAccessToken } from '../utils/cookies';

interface AuthContextType {
    isAuthenticated: boolean;
    setIsAuthenticated: React.Dispatch<React.SetStateAction<boolean>>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(!!getAccessToken());
    const [loading, setLoading] = useState(true);  // Add a loading state to wait for token check
    const navigate = useNavigate();

    useEffect(() => {
        const refreshToken = async () => {
            const success = await refreshTokenRequest();
            setIsAuthenticated(success);  // Set authentication status
            setLoading(false);  // Once the check is done, set loading to false
            if (!success) navigate('/login');  // Redirect if not authenticated
        };

        refreshToken();
    }, [navigate]);

    if (loading) {
        return <div>Loading...</div>;  // Show loading while checking auth status
    }

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
