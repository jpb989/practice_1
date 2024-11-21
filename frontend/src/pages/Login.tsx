import React, { useEffect } from 'react';
import Form from '../Components/Form/Form'
import api from '../api/apiService';
import { getAccessToken, getRefreshToken, setAccessToken, setRefreshToken } from '../utils/cookies';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
export const loginInputs = [
  { type: 'email', name: 'email', placeholder: 'Email' },
  { type: 'password', name: 'password', placeholder: 'Password' }
];


const Login = () => {
  
  const navigate = useNavigate();
  const handleSubmit = async (data: React.FormEvent<HTMLFormElement>) => {
    // data.preventDefault();
    try {
      const response = await api.post("token/", data);
      console.log(response);
      setAccessToken(response.data.access);
      setRefreshToken(response.data.refresh);
      navigate("/");
    } catch (error) {
      console.log(`Error: ${error}`);
    }
    
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg">
        <Form
          title="Login"
          buttonText="Log In"
          // onSubmit={(data) => console.log("Login Data:", data)} handleSubmit
          onSubmit={handleSubmit}
          inputFields={loginInputs}
          alternateLink={{ prompt: "Don't have an account?", text: 'Sign Up', url: '/signup' }}
        />
      </div>
    </div>
  )
}

export default Login