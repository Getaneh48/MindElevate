import './bookmarked_books.scss';
//import warning_icon from '../../assets/images/warning.png';
import loading_icon from '../../assets/images/loading.gif';
import bookmarked_icon from '../../assets/images/bookmarked-books.png';
import book_not_found_icon from '../../assets/images/book-not-found.png';

import { useEffect, useState } from 'react';
import BookmarkedBook from '../../components/home/bookmarked_books/BookmarkedBook';
import { useNavigate } from 'react-router';
import config from '../../config/config';

export default function BookmarkedBooks() {
    const [inprogress, setInProgress] = useState(true);
    const [bookmarks, setBookmarks] = useState([]);
    const navigate = useNavigate();
    
    const removeFromBookmark = async (id) => {
        if (confirm("Are you sure?")) {
            setInProgress(true);
            try {
                const url = `${config.api_url}/bookmarks`;
                const pdata = {'id': id}
                const response = await fetch(url, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(pdata),
                });
                if (response.ok) {
                    const data = await response.json();
                    setInProgress(false);
                    setBookmarks(bookmarks.filter(bookmark => bookmark.id != id));
                    alert(data.message);
                } else {
                    setInProgress(false);
                }
            } catch (error) {
                console.log(error);
                setInProgress(false);
            }
        }
    }

    const handleReadNow = async (book_id) => {
        navigate(`/melv/readbook/${book_id}/ext/${false}`)
    }

    useEffect(()=>{
        const fetchBookmarks = async () => {
            try {
                setInProgress(true);
                const url = `${config.api_url}/bookmarks`;
    
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    setBookmarks(data);
                    setInProgress(false)
                } else {
                    setInProgress(false);
                }
            } catch (error) {
                console.log(error);
                setInProgress(false);
            }
        }

        fetchBookmarks();
        
    },[])

    return (
        <section className="bm-container">
            <div className="bm-header">
                <img src={bookmarked_icon} alt="Books Read Icon" />
                <span className="bm-header-title">Bookmarked</span>
            </div>
            <div className="bm-container">
                <div className={`${inprogress ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
                {
                    bookmarks.length > 0 ? (
                        bookmarks?.map((bbook, index) => {
                            return (
                                <BookmarkedBook bbook={bbook} removeFromBookmark={removeFromBookmark} handleReadNow={handleReadNow} key={index} />
                            )
                        })
                    ) : (
                        <div className="not-results-found">
                            <img src={book_not_found_icon} alt="Bookmarked books list is empty" />
                        </div>
                    )
                    
                }
            </div>
        </section>
    )
}