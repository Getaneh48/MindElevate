import './favorite_books.scss';
import loading_icon from '../../assets/images/loading.gif';
import favorite_icon from '../../assets/images/favorite-books.png';

import { useContext, useEffect, useState } from 'react';
import FavoriteBook from './FavoriteBook';
import book_not_found_icon from '../../assets/images/book-not-found.png';
import MostPopularBooks from '../../components/most_popular_books/MostPopularBooks';
import RecommendedBooks from '../../components/home/recommended_books/RecommendedBooks';
import config from '../../config/config';
import AccountContext from '../../context/AccountContext';

export default function FavoriteBooks() {
    const [loading, setLoading] = useState(false);
    const [favorites, setFavorites] = useState([]);
    const {token} = useContext(AccountContext);

    useEffect(()=>{
        const url = `${config.api_url}/favorites`;
        const fetchFavorites = async () => {
            try {
                setLoading(true);
                const options = {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                };
                const response = await fetch(url, options);
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
            <div className="fv-container-body">
                <div className={`${loading ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
                {
                    favorites.length > 0 ? (
                        favorites?.map((fbook, index) => {
                            return (
                                <FavoriteBook fbook={fbook} favorites={favorites} setFavorites={setFavorites} key={index} />
                            )
                        })
                    ) : (
                        <div className="not-results-found">
                            <img src={book_not_found_icon} alt="Favorite books not found" />
                        </div>
                    )
                    
                }
            </div>
            <div className="most-popular-books-container">
                <MostPopularBooks />
            </div>

            <div className="recommended-books-container">
                <RecommendedBooks />
            </div>
        </section>
    )
}