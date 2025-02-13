import React from 'react';

interface TrailerProps {
  trailerUrl: string;
}

const Trailer: React.FC<TrailerProps> = ({ trailerUrl }) => {
  return (
    <div className="relative w-full" style={{ paddingBottom: '56.25%' }}>
      <iframe
        src={trailerUrl}
        title="Movie Trailer"
        className="absolute top-0 left-0 w-full h-full"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    </div>
  );
};

export default Trailer;
