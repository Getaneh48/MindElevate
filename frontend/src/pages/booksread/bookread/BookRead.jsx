import './bookread.scss';
import PropTypes from 'prop-types';

export default function BookRead({bookr}) {
    return (
        <div className="book-read-container">
            <div className="book-info">
                <div className="cover-image"></div>
                <span className="authors"></span>
                
            </div>

            <div className="book-actions">

            </div>
            
        </div>
    )
}

BookRead.propTypes = {
    bookr: PropTypes.object,
}