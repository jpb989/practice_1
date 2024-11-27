import { useNavigate } from 'react-router-dom';
import api from '../api/apiService';
import Form from '../Components/Form/Form'
import { loginInputs } from './Login';

const Signup = () => {
    const signupInputs = [
        { type: 'text', name: 'name', placeholder: 'Full Name' },
        ...loginInputs,
        { type: 'password', name: 'confirm_password', placeholder: 'Confirm Password' },
    ];
    const navigate = useNavigate();

    const handleSubmit = async (data: React.FormEvent<HTMLFormElement>) => {
        // data.preventDefault();
        console.log("Signup Data:", data);
        try {
          const response = await api.post("api/register/", data);
        //   console.log(response);
          navigate("/login");
        } catch (error) {
          console.log(`Error: ${error}`);
        }
        
      }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg">
            <Form
                title="Sign Up"
                buttonText="Create Account"
                onSubmit={(data) => handleSubmit(data)}
                inputFields={signupInputs}
                alternateLink={{ prompt: "Already have an account?", text: 'Login', url: '/login' }}
            />
        </div>
    </div>
  )
}

export default Signup