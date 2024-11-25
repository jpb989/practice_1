import React, { useEffect, useState } from 'react'
import api from '../api/apiService';
import { useParams } from 'react-router-dom';

type Movie = {
    title: string;
    poster: string;
    release_date: string;
    rating?: string;
    description?: string;
    duration: string;
    language: string;

}

const MovieDetails = () => {
    const { id } = useParams<{ id: string }>();
    const [movie, setMovie] = useState<Movie | null>(null);
    

        useEffect(() => {
            const fetchMovie = async () => {
            try {
                const response = await api.get(`/movies/${id}`);
                setMovie(response.data);
            } catch (error) {
                console.error(`Error fetching movie details: ${error}`);
            }
            };
        
            fetchMovie();
        }, [id]);


    if (!movie) {
        return <p>Movie not found!</p>;
    }
    
    return (
        <div className="px-8 py-6">
            <h1 className="text-3xl font-bold mb-6 text-center">{movie.title}</h1>
            <img
                className="w-full max-h-96 object-contain mx-auto"
                src={movie.poster}
                alt={movie.title}
            />
            <p className="mt-4 text-lg text-gray-700 text-center">{movie.description}</p>
            <p className="mt-2 text-center">
                <strong>Release Date:</strong> {movie.release_date}
            </p>
            {movie.rating && (
                <p className="mt-2 text-center">
                <strong>Rating:</strong> {movie.rating}
                </p>
            )}
        </div>
    );
}

export default MovieDetails