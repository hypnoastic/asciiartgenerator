import React from 'react';
import { useNavigate } from 'react-router-dom';
import './navbar.css'

export default function Navbar() {
    const navigate = useNavigate();

    return (
        <nav className="navbar">
            <h1 className="nav-title" onClick={() => navigate('/')}>ASCII Image Converter</h1>
            <button className="about-btn" onClick={() => navigate('/about')}>About</button>
        </nav>
    );
}