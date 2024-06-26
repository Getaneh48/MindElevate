import './bookmarkedbook.scss';
import remove_bookmark_icon from '../../../assets/images/remove-bookmark.png';
import read_book_icon from '../../../assets/images/read-book.png';
import PropTypes from 'prop-types';

export default function BookmarkedBook({bbook, removeFromBookmark, handleReadNow  }) {
    return (
        <div className="bookmarked-book">
            <div className="cover-image"><img src={bbook?.book?.cover_image} alt="" /></div>
            <div className="book-info">
                <span className="title">{bbook?.book?.title}</span>
                <span className="authors">{bbook?.book?.author}</span>
                <div className="bottom-info">
                    <span className="pages">{bbook?.book?.pages} pages</span>
                    <span className="genre">[ {bbook?.book?.genre?.name} ]</span>
                    <span className="pub_year">{bbook.book?.pub_year}</span>
                </div>
                
                
            </div>

            <div className="book-actions">
                <img src={read_book_icon} alt="add book to reading list" onClick={()=>handleReadNow(bbook.id)}/>
                <img src={remove_bookmark_icon} alt="Remove from Bookmark Icon" onClick={()=>removeFromBookmark(bbook.id)} />
            </div>
        </div>
    )
}

BookmarkedBook.propTypes = {
    bbook: PropTypes.object.isRequired,
    removeFromBookmark: PropTypes.func,
    handleReadNow: PropTypes.func,
}