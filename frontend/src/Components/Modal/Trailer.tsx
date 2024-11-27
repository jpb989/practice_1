import React from 'react';

interface TrailerProps {
  trailerUrl: string;
}

const Trailer: React.FC<TrailerProps> = ({ trailerUrl }) => {
  return (
    <div className="w-full h-[315px]">
      <iframe
        width="100%"
        height="100%"
        src={trailerUrl}
        title="Movie Trailer"
        className="border-0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    </div>
  );
};

export default Trailer;
