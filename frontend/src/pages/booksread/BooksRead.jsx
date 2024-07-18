import './booksread.scss';
import warning_icon from '../../assets/images/warning.png';
import books_read_icon from '../../assets/images/books-read.png';
import loading_icon from '../../assets/images/loading.gif';
import book_not_found from '../../assets/images/book-not-found.png';

import { useContext, useEffect, useState } from 'react';
import BookRead from './bookread/BookRead';
import BooksReadByGenre from '../../components/home/books_read_by_genere/BooksReadByGenre';
import MostPopularBooks from '../../components/most_popular_books/MostPopularBooks';
import config from '../../config/config';
import AccountContext from '../../context/AccountContext';

export default function BooksRead() {
    const {token} = useContext(AccountContext)
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(false);
    const [books_read, setBooksRead] = useState([]);

    useEffect(()=> {
        const url = `${config.api_url}/booksread`;
        const fetchReadBooks = async () => {
            try {
                setLoading(true)
                const options = {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                };
                const response = await fetch(url, options);
                console.log(response)
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    setLoading(false);
                    setBooksRead(data);
                } else {
                    setLoading(false);
                    if (response.status == 500) {
                        console.log("Server Error");
                    }
                }
            } catch (error) {
                console.log(error);
                if (error.message === 'Failed to fetch') {
                    setError(true);
                }
                setLoading(false);
            }
        }

        fetchReadBooks();
    },[]);

    return (
        <section className="books-read-container">
            <div className="books-read-header">
                <img src={books_read_icon} alt="Books Read Icon" />
                <span className="books-read-header-title">Books Read</span>
            </div>
            <div className="books-read-container-body">
                <div className={`${error ? "error message-area" : "message-area"}`}><img src={warning_icon} alt="" /><span className="error">Network Error</span></div>
                <div className={`${loading ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
                {
                    books_read.length > 0 ? (
                        books_read.map((book, index) => {
                            return (
                                <BookRead bookr={book} key={index} />
                            )
                        })
                    ) : (
                        <div className="not-found">
                            <img src={book_not_found} alt="Book data not found" />
                        </div>
                    )
                }
            </div>

            <div className="most-popular-books-container">
                <MostPopularBooks />
            </div>
            <div className="books-rbg">
                <BooksReadByGenre />
            </div>
            
        </section>
    )
}