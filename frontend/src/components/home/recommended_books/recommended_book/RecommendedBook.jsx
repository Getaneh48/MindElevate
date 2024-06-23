import { useState } from 'react';
import './recommendedbook.scss';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router';

export default function RecommendedBook({rbook}) {
    const [hidden, setHidden] = useState(true);
    const navigate = useNavigate();

    const handleReadNow = () => {
        navigate(`/readbook/${rbook.id}/ext/${true}`)
    }
   
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
                            <div className="read-now"><button className='read-now-btn' onClick={handleReadNow}>Read Now</button></div>
                        </div>
                        <span className="close" onClick={()=>setHidden(!hidden)}>x</span>
                    </div>

                    
                    
                </div>
        </div>
    )
}

RecommendedBook.propTypes = {
    rbook: PropTypes.object.isRequired, // Adjust type if needed
};