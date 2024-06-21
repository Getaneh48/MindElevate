import './bookmarked_books.scss';
import warning_icon from '../../assets/images/warning.png';
import loading_icon from '../../assets/images/loading.gif';
import bookmarked_icon from '../../assets/images/bookmarked-books.png';

import { useState } from 'react';

export default function BookmarkedBooks() {
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(false);

    return (
        <section className="bm-container">
            <div className="bm-header">
                <img src={bookmarked_icon} alt="Books Read Icon" />
                <span className="bm-header-title">Bookmarked</span>
            </div>
            <div className="bm-container">
                <div className={`${error ? "error message-area" : "message-area"}`}><img src={warning_icon} alt="" /><span className="error">Network Error</span></div>
                <div className={`${loading ? "active loading" : "loading"}`}><img src={loading_icon} alt="Loading content" /></div>
            </div>
        </section>
    )
}