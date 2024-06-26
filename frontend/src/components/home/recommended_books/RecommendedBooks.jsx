import './recommendedbooks.scss';
import recommended_books_icon from '../../../assets/images/recommended_books.png'
import RecommendedBook from './recommended_book/RecommendedBook';
import { useEffect, useRef, useState } from 'react';
import loading_icon from '../../../assets/images/loading.gif';

export default function RecommendedBooks() {
    const [recommended_books, setRecommendedBooks] = useState([]);
    const [loading_recommendation, setLoadingRecommendation] = useState(false);
    const [bookmarkInfo, setBookmarkInfo] = useState(null);
    const selected_genre = useRef();
    const [inprogress, setInProgress] = useState(false);
    const [error, setError] = useState(null);

    useEffect(()=>{
        const getRecommendation = async () => {
            const url = 'http://localhost:5001/api/v1/books_recommended';
            try {
                setLoadingRecommendation(true)
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    setRecommendedBooks(data);
                    setLoadingRecommendation(false);
                } else {
                    if (response.status == 503) {
                        console.log(response.statusText)
                        setError(response.statusText);
                        setLoadingRecommendation(false);
                    }
                }

            } catch (error) {
                console.log(error);
                
                setLoadingRecommendation(false);
            }
            
        }

        getRecommendation();
    },[]);

    const handleBookmark = async () => {
        try {
            setInProgress(true);
            const url = 'http://localhost:5001/api/v1/bookmarks/new';
            const book_api_url = `https://www.dbooks.org/api/book/${encodeURIComponent(bookmarkInfo.book.id)}`;
            const response = await fetch(book_api_url);
            if (response.ok) {
                const book_data = await response.json();
                console.log(book_data);
                if (book_data.status == 'ok') {
                    const book_info = {
                        title: book_data.title,
                        author: book_data.authors,
                        genre_id: selected_genre.current.value,
                        pub_year: book_data.year,
                        pages: book_data.pages,
                        cover_image: book_data.image,
                        subtitle: book_data.subtitle,
                        description: book_data.description,
                    }

                    const resp = await fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(book_info),
                    });
                    if (resp.ok) {
                        const data = await resp.json();
                        console.log(data)
                        if(data.success) {
                            setBookmarkInfo(null);
                            setInProgress(false);
                            alert(data.message);
                        } else {
                            alert(data.message);
                        }

                    } else {
                        console.log(resp);
                        setInProgress(false);
                    }
                } else {
                    setInProgress(false);
                }
            }
        } catch (error) {
            console.log(error)
        }
    }

    return (
        <section className="recommended_books_container">
            <div className="rbooks_header">
                    <img src={recommended_books_icon} alt="Handbook of Medical Herbs"/>
                    <div className="title">Recommended Books</div>
            </div>
            <div className={`${loading_recommendation ? "active loading-progress" : "loading-progress"}`}><img src={loading_icon} alt="Loading recommended books in progress" /></div>
            <div className="rbooks_body">
                {
                    recommended_books ? (
                        recommended_books?.map((rbook, index) => {
                            return (
                                <RecommendedBook rbook={rbook} setBookmarkInfo={setBookmarkInfo}key={index} />
                            )
                        })
                    ) : (
                        <h3>No recommendation available</h3>
                    )
                    
                }

                {
                    error ? (
                        <div className="error_info">
                            <span>{error}</span>
                        </div>
                    ) : (
                        ''
                    )
                }

            </div>
            {
                    bookmarkInfo ? (
                        <div className="genre-selection-container">
                            <div className="genre-selection-header">
                                <span className='title'>Genre</span>
                                <span className="close" onClick={()=>setBookmarkInfo(null)}>x</span>
                            </div>
                            <div className="genre-selection-body">
                                {
                                    bookmarkInfo['genres'].length > 0 ? (
                                        <select className='genres-selection' ref={selected_genre}>
                                            <option value="">Select Genre</option>
                                            {
                                                bookmarkInfo['genres'].map((genre, index) => {
                                                    return (
                                                        <option value={genre.id} key={index}>{genre.name}</option>
                                                    )
                                                })
                                            }
                                        </select>
                                    ) : (
                                        'Non Found'
                                    )
                                }
                            </div>
                            <div className="genre-selection-actions">
                                {
                                    inprogress ? (
                                        <div className="genre-selection-action">
                                            <img src={loading_icon} alt="saving in porgress" />
                                             <button className="bookmark-now">Bookmark Now</button>
                                        </div>
                                       
                                    ) : (
                                        <button className="bookmark-now" onClick={handleBookmark}>Bookmark Now</button>
                                    )
                                }
                                
                            </div>
                        </div>
                    ) : (
                        ''
                    )
                }
        </section>
    )
}