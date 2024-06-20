//import { useEffect } from 'react';
import './booksonprogress.scss';
import PropTypes from 'prop-types';

export default function BooksOnProgress({books_reading, selected_book,setSelectedBook}) {
    const handleBookSelection = (e) => {
        const br_id = e.currentTarget.value;
        for(const index in books_reading) {
            console.log(books_reading[index]);
            if (books_reading[index].id == br_id){
                setSelectedBook(books_reading[index]);
                break;
            }
        }
    }

    return (
        <div className="books-on-progress-container">
            <span className="label">Books On Progress</span>
            <select className="books-on-progress" onChange={handleBookSelection}>
                <option value=""></option>
                {
                    books_reading?.map((breading, index) => {
                        return (
                            (breading?.id == selected_book?.id) ? (
                            
                                <option value={breading?.id} key={index} selected="selected">{breading?.book.title}</option>
                            ) : (
                                <option value={breading?.id} key={index}>{breading?.book.title}</option>
                            )
                        )
                        
                        
                    })
                }
            </select>
        </div>
    )
}

BooksOnProgress.propTypes = {
    books_reading: PropTypes.array,
    selected_book: PropTypes.object,
    setSelectedBook: PropTypes.func,
};