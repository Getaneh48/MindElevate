import './bookread.scss';
import PropTypes from 'prop-types';
import share_icon from '../../../assets/images/share.png';
import like_icon from '../../../assets/images/like.png';
import liked_icon from '../../../assets/images/liked.png';
import favorite_icon from '../../../assets/images/favorite.png';
import favorite_marked from '../../../assets/images/favorite-marked.png';
import open_book_icon from '..//../../assets/images/open-book-4.png';
import getBadge from '../../../datas/badges';
import { useEffect, useState } from 'react';
import config from '../../../config/config';

export default function BookRead({bookr}) {
    const [is_favorite, setIsFavorite] = useState(bookr.is_favorite);
    const [is_liked, setIsLiked] = useState(bookr.is_liked);
    console.log(bookr);

    useEffect(()=>{
        setIsFavorite(bookr.is_favorite);
    },[bookr])

    const handleFavorite = async (favorite) => {
        try {
            let url = ''
            if (favorite) {
                url = `${config.api_url}/favorites/add`;
            } else {
                url = `${config.api_url}/favorites/remove`;
            }
            
            const data = {
                'br_id': bookr.id,
            }

            const response = await fetch(url, {
                method: 'PUT',
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json",
                }
            });
            if (response.ok) {
                const resp_data = await response.json();
                if(resp_data.success) {
                    console.log(resp_data);
                    setIsFavorite(!is_favorite);
                }
                console.log(resp_data);
            }
        } catch (error) {
            console.log(error);
        }
    }

    const handleLike = async () => {
        try {            
            const url = `${config.api_url}/booksreading/like`;
            const data = {
                'br_id': bookr.id,
                'is_liked': !is_liked,
            }

            const response = await fetch(url, {
                method: 'PUT',
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json",
                }
            });
            if (response.ok) {
                const resp_data = await response.json();
                if(resp_data.success) {
                    console.log(resp_data);
                    setIsLiked(!is_liked);
                }
                console.log(resp_data);
            }
        } catch (error) {
            console.log(error);
        }
    }
    console.log(is_favorite);
    return (
        <div className="book-read-container">
            <div className="cover-image"><img src={bookr.book.cover_image ? bookr.book.cover_image : open_book_icon} alt="" /></div>
            <div className="book-info">
                <span className="title">{bookr.book.title}</span>
                <span className="authors">{bookr.book.author}</span>
                <div className="bottom-info">
                    <span className="pages">{bookr.book.pages} pages</span>
                    <span className="genre">[ {bookr.book.genre.name} ]</span>
                    <span className="pub_year">{bookr.book.pub_year}</span>
                    
                </div>
                
                
            </div>

            <div className="book-actions">
                {
                    <img src={is_favorite ? favorite_marked : favorite_icon} alt="Mark the book as favorite" onClick={()=> handleFavorite(!is_favorite)} className='fav'/>
                }
                {
                    <img src={is_liked ? liked_icon : like_icon} alt="Like book" onClick={handleLike}/>
                }
                
                <img src={share_icon} alt="Share book" />
            </div>

            <div className="assigned-badge">
                {
                    bookr.badge_id ? (
                        <img src={getBadge(bookr.badge.btype)} alt="badge" />
                    ) : ( '')
                }
            </div>
            
        </div>
    )
}

BookRead.propTypes = {
    bookr: PropTypes.object,
}