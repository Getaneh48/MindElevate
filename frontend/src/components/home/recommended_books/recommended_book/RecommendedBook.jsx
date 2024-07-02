import { useEffect, useState } from 'react';
import './recommendedbook.scss';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router';
import config from '../../../../config/config';

export default function RecommendedBook({rbook, setBookmarkInfo}) {
    const [hidden, setHidden] = useState(true);
    const [genres, setGenres] = useState([]);
    const navigate = useNavigate();

    const handleReadNow = () => {
        navigate(`/readbook/${rbook.id}/ext/${true}`)
    }

    useEffect(()=> {
        const fetchGenres = async () => {
            try {
                const url = `${config.api_url}/books/genres`;
                const response = await fetch(url)
                if (response.ok) {
                    const data = await response.json();
                    setGenres(data)
                }
            } catch (error) {
                console.log(error)
            }
        }

        fetchGenres()
    },[])
   
    return (
        <div className="recommended_book_container" onClick={()=>setHidden(!hidden)}>
                <div className="cover-image">
                    <img src={rbook.image} alt="" />
                </div>
                
                <div className={hidden ? "hidden desc" : 'desc'}>
                    <div className="desc-body">
                        <div className="cover_image_full">
                            <img src={rbook.image} alt=""/>
                        </div>
                        <div className="book-desc">
                            <p><span className="label">Title</span><span className="book-title">{rbook.title}</span> </p>
                            <p><span className="label">Authors</span><span className="book-title">{rbook.authors}</span> </p>
                            <p><span className="label">Subtitle</span><span className="book-title">{rbook.subtitle}</span> </p>
                            <div className="actions">
                                <button className='read-now-btn' onClick={handleReadNow}>Read</button>
                                <button className="bookmark" onClick={()=>setBookmarkInfo({'genres': genres, 'book': rbook})}>Bookmark</button>
                            </div>
                            
                        </div>
                        <span className="close" onClick={()=>setHidden(!hidden)}>x</span>
                    </div>

                </div>
        </div>
    )
}

RecommendedBook.propTypes = {
    rbook: PropTypes.object.isRequired,
    setBookmarkInfo: PropTypes.func,
};