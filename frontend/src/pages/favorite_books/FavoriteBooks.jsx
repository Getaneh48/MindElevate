import './favorite_books.scss';
import warning_icon from '../../assets/images/warning.png';
import loading_icon from '../../assets/images/loading.gif';
import favorite_icon from '../../assets/images/favorite-books.png';

import { useState } from 'react';

export default function FavoriteBooks() {
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(false);
    const [favorites, setFavorites] = useState([]);

    return (
        <section className="fv-container">
            <div className="fv-header">
                <img src={favorite_icon} alt="Favorite Books Icon" />
                <span className="fv-header-title">Favorites</span>
            </div>
            <div className="fv-container">
                <div className={`${error ? "error message-area" : "message-area"}`}><img src={warning_icon} alt="" /><span className="error">Network Error</span></div>
                <div className={`${loading ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
            </div>
        </section>
    )
}