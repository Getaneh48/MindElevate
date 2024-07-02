import { useEffect, useState } from 'react';
import './mostpopularbook.scss';
import PropTypes from 'prop-types';
import config from '../../config/config';

export default function MostPopularBook({book_title, setSelectedBook}) {
    const [book, setBook] = useState(null);

    useEffect(()=>{
        const fetchPopularBook = async () => {
            try {
                const url = `${config.api_url}/books/title/${book_title}`;
                const response = await fetch(url);
                if(response.ok) {
                    const resp_data = await response.json();
                    console.log(resp_data);
                    setBook(resp_data);
                }
            } catch (error) {
                console.log(error);
            }
        }

        fetchPopularBook();
    },[book_title])

    function handleShowDetail() {
        setSelectedBook(book)
    }
    return (
        <>
            <div className="most-popular-book">
                <div className="cover-image" onClick={handleShowDetail}>
                    <img src={book?.cover_image} alt="" />
                </div>
            </div>
        </>
        


    )
}

MostPopularBook.propTypes = {
    book_title: PropTypes.string.isRequired,
    setSelectedBook:PropTypes.func,
}