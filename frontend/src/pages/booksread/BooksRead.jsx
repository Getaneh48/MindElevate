import './booksread.scss';
import warning_icon from '../../assets/images/warning.png';
import books_read_icon from '../../assets/images/books-read.png';
import loading_icon from '../../assets/images/loading.gif';

import { useEffect, useState } from 'react';
import BookRead from './bookread/BookRead';

export default function BooksRead() {
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(false);
    const [books_read, setBooksRead] = useState([]);

    useEffect(()=> {
        const url = 'http://localhost:5001/api/v1/booksread';
        const fetchReadBooks = async () => {
            try {
                setLoading(true)
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    setLoading(false);
                    setBooksRead(data);
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
            <div className="books-read-container">
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
                        <h3>Books Not Found</h3>
                    )
                }
            </div>
        </section>
    )
}