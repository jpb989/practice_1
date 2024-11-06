import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';

type LinkProps = {
  to: string;
  label: string;
}

interface DropdownProps {
  options: Array<LinkProps>;
  className?: string;
  trigger?: React.ReactNode;
}

const Dropdown: React.FC<DropdownProps> = ({ options, className, trigger }) => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const toggleDropdown = () => setIsOpen(prev => !prev);
  const closeDropdown = () => setIsOpen(false);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        closeDropdown();
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="relative" ref={dropdownRef}>
      <div onClick={toggleDropdown} className="cursor-pointer">
        {trigger}
      </div>
      {isOpen && (
        <div className={`absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-md shadow-lg top-full ${className}`}>
          {options.map((option, index) => (
            <Link 
              key={index} 
              to={option.to} 
              className="block px-4 py-2 text-gray-700 hover:bg-gray-100"
              onClick={closeDropdown}
            >
              {option.label}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dropdown;
