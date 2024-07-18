import './bookdetail.scss';
import book_detail_icon from '../../../assets/images/book-detail.png';
import PropTypes from 'prop-types';
import { useContext, useEffect, useState } from 'react';
import config from '../../../config/config';
import AccountContext from '../../../context/AccountContext';

export default function BookDetail({book_to_read, reading_info, setReadingInfo, validation_error, reset_form}) {
    const {token} = useContext(AccountContext);
    const [genres, setGenres] = useState([]);

    const handleGenreSelection = (e) => {
        const genre = e.currentTarget.value;
        setReadingInfo({...reading_info, 'genre': genre});
        console.log(genre);
    }

    useEffect(() => {
        const fetchGenres = async () => {
            const url = `${config.api_url}/books/genres`;
            const options = {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            };
            try {
                const response = await fetch(url, options);
                if (response.ok) {
                    const data = await response.json();
                    setGenres(data)
                }
            } catch (error) {
                console.log(error)
            }
        }

        fetchGenres();
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
                                                <option value={genre.id} key={index}>{genre.name}</option>
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
                                                <option value={genre.id} key={index}>{genre.name}</option>
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