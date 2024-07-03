import './favoritebook.scss';
import remove_favorite_icon from '../../assets/images/remove-favorite.png';
import open_book_icon from '../../assets/images/open-book-4.png';

import PropTypes from 'prop-types';
import config from '../../config/config';

export default function FavoriteBook({fbook, favorites, setFavorites}) {
    const removeFromFavorite = async () => {
        const data = {
            id: fbook.id,
        }
        const url = `${config.api_url}/favorites/remove`;
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })

            if (response.ok) {
                const data = await response.json()
                console.log(data);
                
                setFavorites(favorites.filter(fav => fav.id != fbook.id))
            }
        } catch (error) {
            console.log(error);
        }
    }
    return (
        <div className="favorite-book">
            <div className="cover-image"><img src={fbook?.book.cover_image ? fbook?.book.cover_image : open_book_icon} alt="" /></div>
            <div className="book-info">
                <span className="title">{fbook?.book.title}</span>
                <span className="authors">{fbook?.book.author}</span>
                <div className="bottom-info">
                    <span className="pages">{fbook?.book.pages} pages</span>
                    <span className="genre">[ {fbook?.book.genre?.name} ]</span>
                    <span className="pub_year">{fbook.book.pub_year}</span>
                </div>
                
                
            </div>

            <div className="book-actions">
                <img src={remove_favorite_icon} alt="Remove from Favorite Icon" onClick={removeFromFavorite} />
            </div>
        </div>
    )
    
}

FavoriteBook.propTypes = {
    fbook: PropTypes.object.isRequired,
    favorites: PropTypes.array,
    setFavorites: PropTypes.func,
}