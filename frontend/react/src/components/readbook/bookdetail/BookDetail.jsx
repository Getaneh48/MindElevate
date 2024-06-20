import './bookdetail.scss';
import book_detail_icon from '../../../assets/images/book-detail.png';
import PropTypes from 'prop-types';
import { useEffect } from 'react';

export default function BookDetail({book_to_read, reading_info, setReadingInfo, validation_error, reset_form}) {

    const genres = [
        "Personal Growth",
        "Politics & Laws",
        "Technology",
        "Religion",
        "Science & Research",
        "Enviroment",
        "Academic & Education",
        "Biography",
        "Art",
        "Fiction & Litrature",
        "Business & Career",
        "Health and Fitness",
        "Lifestyle"
    ]

    const handleGenreSelection = (e) => {
        const genre = e.currentTarget.value;
        setReadingInfo({...reading_info, 'genre': genre});
        console.log(genre);
    }

    useEffect(() => {
        
    },[reset_form])

    return (
        <div className="book-detail-container">
            <div className="book-detail-header">
                <div className="icon"><img src={book_detail_icon} alt="" /></div>
                <span className="title">Book Detail</span>
            </div>
            <div className="book-detail-body">
                <div className="book-desc">
                    <p><span className="label">Title</span><span className="text">{book_to_read?.title}</span></p>
                    <p><span className="label">Authors</span><span className="text">{book_to_read?.authors}</span></p>
                    <p>
                        <span className="label">Genre</span>
                        {
                            "genre" in validation_error ? (
                                <select name="genre" className='text error' onChange={handleGenreSelection}>
                                    <option value=""></option>
                                    {
                                        genres.map((genre, index) => {
                                            return (
                                                <option value={genre} key={index}>{genre}</option>
                                            )
                                        })
                                    }

                                </select>
                            ) : (
                                <select name="genre" className='text' onChange={handleGenreSelection}>
                                    <option value=""></option>
                                    {
                                        genres.map((genre, index) => {
                                            return (
                                                <option value={genre} key={index}>{genre}</option>
                                            )
                                        })
                                    }

                                </select>
                            )
                        }
                        
                    </p>
                    <p><span className="label">Publication Year</span><span className="text">{book_to_read?.year}</span></p>
                    <p><span className="label">Pages</span><span className="text">{book_to_read?.pages}</span></p>
                    <p><span className="label">Subtitle</span><span className="text">{book_to_read?.subtitle}</span></p>
                </div>
                <div className="book-cover-img">
                    <img src={book_to_read?.image} alt="" />
                </div>
            </div>
        </div>
    )
}

BookDetail.propTypes = {
    book_to_read: PropTypes.object,
    reading_info: PropTypes.object,
    setReadingInfo: PropTypes.func,
    validation_error: PropTypes.object,
    reset_form: PropTypes.bool,
};