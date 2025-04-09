import './About.css'
import React from 'react';

const About = () => {
    return (
        <div className="about-page">
            <h2>About ASCII Image Converter</h2>
            <p>This project converts any uploaded image into a high-resolution ASCII art image using a FastAPI backend and a React frontend.</p>

            <h3>⚙️ How it works:</h3>
            <ol>
                <li>You upload an image via the frontend.</li>
                <li>The image is sent to the FastAPI backend.</li>
                <li>The backend processes the image into grayscale and maps brightness levels to characters.</li>
                <li>The result is drawn using a monospaced font into a high-resolution image and sent back.</li>
                <li>You can then download the ASCII-rendered image.</li>
            </ol>

            <h3>🛠️ Tech Stack:</h3>
            <ul>
                <li><strong>Frontend:</strong> React, HTML, CSS (Dark theme UI)</li>
                <li><strong>Backend:</strong> FastAPI, OpenCV, Pillow</li>
                <li><strong>Deployment:</strong> Local or Cloud (optional)</li>
            </ul>

            <p>Made with ❤️ by an enthusiastic developer.</p>
        </div>
    );
};

export default About;