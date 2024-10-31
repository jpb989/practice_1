import React from 'react'

const Navbar = () => {
  return (
    <nav className='bg-gray-800 text-white'>
      <div className='max-w-7xl mx-auto px-2 sm:px-6 lg:px-8'>
        <div className='relative-flex items-center justify-between h-16'>
        <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
    <button
      className="...your button classes..."
      aria-controls="mobile-menu"
      aria-expanded="false"
    >
      <span className="sr-only">Open main menu</span>
        {/* Add your SVG icons here for menu icon */}
      </button>
      </div>  
        <div className="flex-shrink-0">
          <img className="h-8" src="/path/to/logo.png" alt="Logo" />
        </div>


        </div>
      </div>
    </nav>
  )
}

export default Navbar