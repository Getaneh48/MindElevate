import { useEffect, useState } from 'react';
import './mostpopularbooks.scss';
import MostPopularBook from './MostPopularBook';
import popular_book_icon from '../../assets/images/popular-books.png';
import { useNavigate } from 'react-router';

export default function MostPopularBooks() {
    const [popular_books, setPopularBooks] = useState([]);
    const [selected_book, setSelectedBook] = useState(null);
    const navigate = useNavigate();

    useEffect(()=>{
        if (selected_book == null) {
            const fetchPopularBooks = async () => {
                try {
                    const url = 'http://localhost:5001/api/v1/booksread/most_pupular';
                    const response = await fetch(url);
                    if(response.ok) {
                        const resp_data = await response.json();
                        const pbooks = [];
                        for (const ind in resp_data) {
                            pbooks.push(ind)
                        }
                        setPopularBooks(pbooks);
                    }
                } catch (error) {
                    console.log(error);
                }
            }
    
            fetchPopularBooks();
        }
       
    },[selected_book])

    return (
        <div className="most-popular-books">
            <div className="most-popular-books-header">
                <img src={popular_book_icon} alt="Popular books icon" />
                <span className="most-popular-books-header-title">Most Popular Books</span>
            </div>
            <div className="most-popular-books-body">
                {
                    popular_books.length > 0 ? (
                        popular_books.map((title, index) => {
                            return (
                                <MostPopularBook book_title={title} setSelectedBook={setSelectedBook} key={index}/>
                            )
                        })
                        
                    ) : (
                        <h3>Not Found</h3>
                    )
                }
            </div>
            {
                selected_book ? (
                    <div className="book-detail-container">
                        <div className="bdc-top">
                            <div className="cover-image">
                                <img src={selected_book?.cover_image} alt={selected_book?.title} />
                            </div>
                            <div className="book-info">
                                <span className="book-title">{selected_book?.title}</span>
                                <span className="book-author">Authors - {selected_book?.author}</span>
                                <span className="genre">Genre - {selected_book?.genre.name}</span>
                                <span className="publication">Year - {selected_book?.pub_year}</span>
                                <span className="book-total-pages">Total Pages - {selected_book?.pages} pages</span>
                                {/* 
                                <span className="subtitle">{selected_book?.sub_title}</span>
                                <span className="description">{selected_book?.description}</span> */}
                            </div>
                            <span className="close" onClick={()=>setSelectedBook(null)}>x</span>
                        </div>

                        <div className="bdc-bottom">
                            <button onClick={()=>navigate(`/readbook/${selected_book.id}/ext/${false}`)}>Read Book</button>
                        </div>
                
                    </div>
                ) : (
                    ''
                )
            }
            
        </div>
    )
}