import React, { useEffect, useState } from 'react';
import api from '../api/apiService';

type movieList = {
  title: string;
  poster: string;
  release_date: string;
  rating?: string;
}

const Home = () => {
  const [movies, setMovies] = useState<movieList[]>([]);

  useEffect(() => {
    const fetchMovies = async () => {
        try {
          const response = await api.get("movies/");
          console.log(response.data.results);
          setMovies(response.data.results);
        } catch (error) {
          console.log(`Error: ${error}`);
        }

    };

    fetchMovies();
  }, []);

  return (
    <div className="px-8 py-6">
      <h1 className="text-3xl font-bold mb-6 text-center">Movie Posters</h1>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-6">
        {movies.map((movie, index) => (
          <div
            key={index}
            className="max-w-xs w-full rounded overflow-hidden shadow-lg transition-transform transform hover:scale-105 bg-white"
          >
            <img
              className="w-full h-60 object-cover"
              src={movie.poster}
              alt={movie.title}
            />
            <div className="px-4 py-4">
              <h2 className="font-bold text-lg mb-2 text-center">{movie.title}</h2>
              <p className="text-gray-600 text-sm text-center">
              {movie.rating ? (
                <span className="flex items-center justify-center gap-1">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    className="w-6 h-6 text-yellow-500"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.006 5.404.434c1.164.093 1.636 1.545.749 2.305l-4.117 3.527 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.117-3.527c-.887-.76-.415-2.212.749-2.305l5.404-.434 2.082-5.005Z"
                      clipRule="evenodd"
                    />
                  </svg>
                  {movie.rating}
                </span>
              ) : (
                movie.release_date
              )}
              </p>
              
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
