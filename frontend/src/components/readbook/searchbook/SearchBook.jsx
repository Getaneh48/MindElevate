import search_icon from '../../../assets/images/search-icon.png';
import add_book from '../../../assets/images/add-book.png';

import './searchbook.scss';
import { useEffect, useState } from 'react';
import Book from './Book';
import PropTypes from 'prop-types';

export default function SearchBook({setBookToReadNow, reset_form, setShowProgress}) {
    const [searchTerm, setSearchTerm] = useState('');
    const [books, setBooks] = useState([]);
    const [showresult, setShowResult] = useState(false);
    const [selectedBook, setSelectedBook] = useState(null);
    const [bookToRead, setBookToRead] = useState(null);

    const api_url = `https://www.dbooks.org/api/search/`;

    useEffect(()=>{
        if (reset_form) {
            setSearchTerm('');
        }
        if (searchTerm == '') {
            setShowResult(false);
        }
        if(bookToRead != null) {
            setShowResult(false);
            setBookToReadNow(bookToRead);
        }

        

    },[searchTerm, bookToRead, setShowResult, setBookToReadNow, reset_form]);
  
    const handleSearch = async () => {
        if (searchTerm == ''){
            return;
        }

        setShowProgress(true);
        try {
            const response = await fetch(`${api_url + encodeURIComponent(searchTerm)}`);
            if (response.ok) {
                const data = await response.json();
                setBooks(data.books);
                setShowResult(true);
            }

            setShowProgress(false);
            
        } catch (error) {
            console.error('Error fetching data:', error);
            setShowProgress(false);
            if (error.message === 'Failed to fetch') {
                alert('Network Error: Unable to get book information!');
            }
        }
    };

    const handleCloseSearchResult = () => {
        setShowResult(false);
    }


    return (
        <div className="search-book-container">
            <div className="search-book-header">
                <div className="icon">
                    <img src={add_book} alt="Add a book for reading" />
                </div>
                <span className="search-book-title">Add Book</span>
            </div>
            <div className="search-book-body">
                <div className="search-book-search-fields">
                    <input type='text' className="search-input" value={searchTerm} onChange={(e)=>setSearchTerm(e.currentTarget.value)}placeholder='Title, Author, Genre'/>
                    <div className="search-btn" onClick={handleSearch}>
                        <img src={search_icon} alt="search book" />
                    </div>
                </div>
                <div className={`${showresult ? "search-book-results" : 'hide search-book-results'}`}>
                    {
                        books.map((book, index) => {
                            return (
                                <Book book={book} selectedBook={selectedBook} setSelectedBook={setSelectedBook} setBookToRead={setBookToRead} key={index}/>
                            )
                        })
                    }
                    <span className="close" onClick={handleCloseSearchResult}>x</span>
                </div>
            </div>
        </div>
    )
}

SearchBook.propTypes = {
    setBookToReadNow: PropTypes.func.isRequired,
    reset_form: PropTypes.bool,
    setShowProgress: PropTypes.func,
}