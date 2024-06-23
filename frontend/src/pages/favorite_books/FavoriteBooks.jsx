import './favorite_books.scss';
import loading_icon from '../../assets/images/loading.gif';
import favorite_icon from '../../assets/images/favorite-books.png';

import { useEffect, useState } from 'react';
import FavoriteBook from './FavoriteBook';

export default function FavoriteBooks() {
    const [loading, setLoading] = useState(false);
    const [favorites, setFavorites] = useState([]);

    useEffect(()=>{
        const url = 'http://localhost:5001/api/v1/favorites';
        
        const fetchFavorites = async () => {
            try {
                setLoading(true);
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    setFavorites(data);
                    setLoading(false);
                } else {
                    if (response.status == 404){
                        console.log("Resource not found");
                    }
                    setLoading(false);
                }
            } catch (error) {
                console.log(error);
                setLoading(false);
            }

        }
        
        fetchFavorites();
    },[])

    return (
        <section className="fv-container">
            <div className="fv-header">
                <img src={favorite_icon} alt="Favorite Books Icon" />
                <span className="fv-header-title">Favorites</span>
            </div>
            <div className="fv-container">
                <div className={`${loading ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
                {
                    favorites.length > 0 ? (
                        favorites?.map((fbook, index) => {
                            return (
                                <FavoriteBook fbook={fbook} favorites={favorites} setFavorites={setFavorites} key={index} />
                            )
                        })
                    ) : (
                        'None Found'
                    )
                    
                }
            </div>
        </section>
    )
}