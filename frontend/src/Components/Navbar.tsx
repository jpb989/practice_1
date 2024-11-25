import React from 'react';
import { Link } from 'react-router-dom';
import { UserCircleIcon } from '@heroicons/react/16/solid';
import Dropdown from './Dropdown';
import { useAuth } from '../context/AuthContext';

const dropdown_options = [
  { to: "/profile", label: "Profile" },
  { to: "/logout", label: "Logout" },
];

const Navbar: React.FC = () => {
  const { isAuthenticated } = useAuth();

  return (
    <nav className="bg-gray-800 py-3 px-6 h-18 border-b border-gray-700 shadow-sm text-white text-lg font-semibold">
      <div className="flex items-center w-full">
        <div className='flex space-x-4'>
          <Link to="/" className="hover:text-gray-300 transition">Home</Link>
        </div>
        <div className='ml-auto'>
          { isAuthenticated ? 
            <Dropdown 
            options={dropdown_options} 
            trigger={<UserCircleIcon className="h-8 w-8 cursor-pointer hover:text-gray-300 transition" />}
            className='text-xl'
            />
          :
          <div className="grid grid-cols-2 gap-3">
            <button className="bg-gray-700 text-gray-300 hover:bg-gray-600 hover:text-white px-4 py-2 rounded-lg transition-all duration-200">
              <Link to="/login">Login</Link>
            </button>
            <button className="bg-indigo-500 text-white hover:bg-indigo-400 px-4 py-2 rounded-lg transition-all duration-200">
              <Link to="/signup">Signup</Link>
            </button>
          </div>
        
          }
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
