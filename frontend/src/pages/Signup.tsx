import Form from '../Components/Form/Form'
import { loginInputs } from './Login';

const Signup = () => {
    const signupInputs = [
        ...loginInputs,
        { type: 'text', name: 'name', placeholder: 'Full Name' }
    ];

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg">
            <Form
                title="Sign Up"
                buttonText="Create Account"
                onSubmit={(data) => console.log("Signup Data:", data)}
                inputFields={signupInputs}
                alternateLink={{ prompt: "Already have an account?", text: 'Login', url: '/login' }}
            />
        </div>
    </div>
  )
}

export default Signup