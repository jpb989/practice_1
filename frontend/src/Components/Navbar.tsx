import React from 'react';
import { Link } from 'react-router-dom';
import { UserCircleIcon } from '@heroicons/react/16/solid';
import Dropdown from './Dropdown';

const dropdown_options = [
  { to: "/profile", label: "Profile" },
  { to: "/login", label: "Login" },
];

const Navbar: React.FC = () => {
  return (
    <nav className="bg-gray-800 p-4 shadow-lg text-white text-2xl">
      <div className="flex items-center w-full">
        <div className='flex space-x-4'>
          <Link to="/" className="hover:text-gray-300 transition">Home</Link>
        </div>
        <div className='ml-auto'>
          <Dropdown 
            options={dropdown_options} 
            trigger={<UserCircleIcon className="h-8 w-8 cursor-pointer hover:text-gray-300 transition" />}
            className='text-xl'
          />
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
