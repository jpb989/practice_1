import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../api/apiService";
import Modal from "../Components/Modal/Modal";
import Trailer from "../Components/Modal/Trailer";

type Movie = {
  title: string;
  poster_landscape: string;
  release_date: string;
  rating?: string;
  description?: string;
  duration: string;
  language: string;
  trailer?: string;
};

const MovieDetails = () => {
    const { id } = useParams<{ id: string }>();
    const [movie, setMovie] = useState<Movie | null>(null);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [trailerUrl, setTrailerUrl] = useState('');
    const navigate = useNavigate();

    const openTrailerModal = (url: string) => {
        setTrailerUrl(url);
        setIsModalOpen(true);
    };

    // Function to close the modal
    const closeTrailerModal = () => {
        setIsModalOpen(false);
        setTrailerUrl('');
    };

    useEffect(() => {
        const fetchMovie = async () => {
        try {
            const response = await api.get(`/movies/${id}`);
            setMovie(response.data);
            console.log(response.data);
        } catch (error) {
            console.error(`Error fetching movie details: ${error}`);
        }
    };

    fetchMovie();
    }, [id]);

    if (!movie) {
        return <p className="text-center text-gray-500 mt-10">Movie not found!</p>;
    }

  return (
        <div className="min-h-screen bg-gray-900 text-white">
        {/* Hero Section */}
        <div className="relative bg-cover bg-fill h-[500px]" style={{ backgroundImage: `url(${movie.poster_landscape})` }}>
            <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black"></div>
            <div className="absolute inset-0 flex items-end p-8">
            <div>
                <h1 className="text-4xl font-bold">{movie.title}</h1>
                <p className="mt-2 text-gray-300">
                {movie.language} | {movie.duration} mins | {movie.rating && `⭐ ${movie.rating}`}
                </p>
                <p className="mt-2 text-gray-300">Release Date: {movie.release_date}</p>
            </div>
            </div>
        </div>

        {/* Movie Description */}
        <div className="px-8 py-6">
            <h2 className="text-2xl font-semibold mb-4">About the Movie</h2>
            <p className="text-gray-400">{movie.description}</p>
        </div>

        {/* Booking Options */}
        <div className="px-8 py-6">
            <h2 className="text-2xl font-semibold mb-4">Book Tickets</h2>
            <div className="flex gap-4">
            <button 
                className="px-6 py-2 bg-red-600 text-white rounded hover:bg-red-500"
                onClick={() => navigate(`/show-timings/${id}`)}
            >
                Book Now
            </button>
            <button 
                className="px-6 py-2 bg-gray-800 text-white rounded hover:bg-gray-700"
                onClick={() => openTrailerModal(movie.trailer ? movie.trailer : "")}
            >
                Watch Trailer
            </button>
            </div>
        </div>

        {/* Additional Sections */}
        <div className="px-8 py-6">
            <h2 className="text-2xl font-semibold mb-4">Cast & Crew</h2>
            <p className="text-gray-500">Coming soon...</p>
        </div>
        <Modal isOpen={isModalOpen} onClose={closeTrailerModal}>
            <Trailer trailerUrl={trailerUrl} />
        </Modal>
        </div>
    );
};

export default MovieDetails;
