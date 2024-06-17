import { useEffect, useState } from 'react';
import './book.scss';
import PropTypes from 'prop-types';

export default function Book({book, selectedBook, setSelectedBook, setBookToRead}) {
    const [showDetail, setShowDetal] = useState(false);
    const api_url = `https://www.dbooks.org/api/book/${encodeURIComponent(book.id)}`;

    useEffect(()=>{
        if(selectedBook?.id !== book.id) {
            setShowDetal(false);
        }
    },[book, selectedBook]);

    const handleShowDetail = () => {
        setShowDetal(!showDetail);
        setSelectedBook(book);
    }

    const handleReadBookBtn = async () => {
        
        try {
            const response = await fetch(`${api_url}`);
            const data = await response.json();
            const book_to_read = {
                'title': data.title,
                'authors': data.authors,
                'pages': data.pages,
                'year': data.year,
                'subtitle': data.subtitle,
                'description': data.description,
                'ref_id': data.id,
                'image': data.image
            }

            setBookToRead(book_to_read);
            setShowDetal(false);

          } catch (error) {
            console.error('Error fetching data:', error);
          }

    }

    return (
        <div className="book-container">
            <div className="book-cover-image" onClick={handleShowDetail}><img src={book.image} alt={book.title} /></div>
            <div className={`${showDetail ? "book-detail" : "hide book-detail"}`}>
                <div className="cover-image-container">
                    <img src={book.image} alt={book.title} />
                </div>
                <div className="book-desc">
                    <p><span className="label">Title</span> <span className="book-title">{book.title}</span></p>
                    <p><span className="label">Author</span> <span className="book-author">{book.authors}</span></p>
                    <p><span className="label">Subtitle</span> <span className="book-title">{book.subtitle}</span></p>
                    <button className='read-book' onClick={handleReadBookBtn}>Read Book</button>
                </div>
                <span className="close" onClick={()=>setShowDetal(false)}>x</span>
            </div>
        </div>
    )
}

Book.propTypes = {
    book: PropTypes.object.isRequired,
    setSelectedBook: PropTypes.func,
    setBookToRead: PropTypes.func,
    selectedBook: PropTypes.object,
};