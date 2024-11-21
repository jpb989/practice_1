import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from './context/AuthContext';

interface ProtectedRouteProps {
    redirectPath: string;
    requireAuth: boolean;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ redirectPath, requireAuth }) => {
    const { isAuthenticated } = useAuth();

    if (requireAuth && !isAuthenticated) {
        // Redirect to login if not authenticated
        return <Navigate to={redirectPath} replace />;
    }

    if (!requireAuth && isAuthenticated) {
        // Redirect to homepage if authenticated
        return <Navigate to={redirectPath} replace />;
    }

    return <Outlet />;
};

export default ProtectedRoute;
