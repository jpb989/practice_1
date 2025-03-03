import React, { useState } from 'react';

const DateSelector: React.FC = () => {
    const [selectedDate, setSelectedDate] = useState<number | null>(0);
    const currDate = new Date();

    // Generate an array of 5 dates starting from today
    const dates = Array.from({ length: 5 }, (_, i) => {
        const date = new Date(currDate);
        date.setDate(currDate.getDate() + i);
        return date;
    });

    const handleDateClick = (index: number) => {
        setSelectedDate(index);
    };

    return (
        <div className="h-screen flex flex-col">
            {/* Top Section: Movie Title and Date Selector */}
            <div className="flex justify-between items-center bg-gray-100 px-8 py-6">
                {/* Movie Title */}
                <h1 className="text-6xl font-bold text-gray-800">Movie Title</h1>

                {/* Date Selector */}
                <div className="flex gap-4">
                    {dates.map((date, index) => (
                        <button
                            key={index}
                            onClick={() => handleDateClick(index)}
                            className={`p-4 rounded-lg text-center cursor-pointer border ${
                                selectedDate === index
                                    ? 'bg-gray-800 text-white font-semibold border-gray-500'
                                    : 'bg-gray-200 text-gray-800 hover:bg-gray-300 border-gray-300'
                            }`}
                        >
                            <div className="text-lg font-bold">{date.getDate()}</div>
                            <div className="text-sm">{date.toLocaleString('en-US', { month: 'short' })}</div>
                        </button>
                    ))}
                </div>
            </div>

            {/* Bottom Section: Show Timings */}
            <div className="flex-grow p-8">
                <h2 className="text-3xl font-semibold mb-6">Show Timings</h2>

                {/* Theatres and Show Timings */}
                <div className="space-y-8">
                    {["Theatre 1", "Theatre 2", "Theatre 3"].map((theatre, index) => (
                        <div key={index} className="bg-gray-100 p-6 rounded-lg shadow-lg">
                            <h3 className="text-2xl font-semibold mb-4">{theatre}</h3>
                            <div className="flex gap-4">
                                {["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"].map((time, timeIndex) => (
                                    <button
                                        key={timeIndex}
                                        className="px-4 py-2 bg-gray-500 text-white rounded-lg font-semibold hover:bg-gray-800"
                                    >
                                        {time}
                                    </button>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default DateSelector;
