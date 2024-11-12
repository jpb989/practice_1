import Form from '../Components/Form/Form'
export const loginInputs = [
  { type: 'email', name: 'email', placeholder: 'Email' },
  { type: 'password', name: 'password', placeholder: 'Password' }
];
const Login = () => {

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg">
        <Form
          title="Login"
          buttonText="Log In"
          onSubmit={(data) => console.log("Login Data:", data)}
          inputFields={loginInputs}
          alternateLink={{ prompt: "Don't have an account?", text: 'Sign Up', url: '/signup' }}
        />
      </div>
    </div>
  )
}

export default Login