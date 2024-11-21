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
    <nav className="bg-gray-800 p-4 shadow-lg text-white text-2xl">
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
            <>
              <button className='bg-white text-black'><Link to="/login">Login</Link></button>
              <button className='bg-white text-black'><Link to="/signup">Signup</Link></button>
            </>
          }
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
