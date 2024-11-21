import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';  // Import useNavigate from react-router-dom
import api from '../api/apiService';
import { deleteTokens, getAccessToken, getRefreshToken } from '../utils/cookies';

const Logout = () => {
    const navigate = useNavigate();  // Use useNavigate hook
    useEffect(() => {
        const logout = async () => {
            const refresh = getRefreshToken();
            const access = getAccessToken();
            try {
                const response = await api.post("/logout/", {
                    "refresh": refresh,
                    "access": access,
                });

                // Check if the status is in the success range
                if (response.status >= 200 && response.status < 300) {
                    deleteTokens();
                    navigate('/');
                }
            } catch (error) {
                console.error(`Error: ${error}`);
            }
        };

        logout(); // Call the logout function
    }, [navigate]);  // Run this effect when the component mounts

    return null;  // Since you're logging out and redirecting, you don't need to render anything
};

export default Logout;
