import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './Components/Navbar'
import Home from './pages/Home'
import Profile from './pages/Profile'
import Login from './pages/Login'
import Signup from './pages/Signup'
import ProtectedRoute from './ProtectedRoute'
import { AuthProvider } from './context/AuthContext'
import Logout from './pages/Logout'
import MovieDetails from './pages/MovieDetails'
import ShowTimings from './pages/ShowTimings'

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/movies/:id" element={<MovieDetails/>} />
          <Route path="/show-timings/:id" element={<ShowTimings/>} />
          {/* Redirect to homepage if authenticated */}
          <Route element={<ProtectedRoute requireAuth={false} redirectPath="/" />}>
            <Route path="/login" element={<Login/>} />
            <Route path="/signup" element={<Signup/>} />
          </Route>

          {/* Redirect to login if not authenticated */}
          <Route element={<ProtectedRoute requireAuth={true} redirectPath="/login" />}>
            <Route path="/profile" element={<Profile/>} />
            <Route path="/logout" element={<Logout/>} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  )
}

export default App
