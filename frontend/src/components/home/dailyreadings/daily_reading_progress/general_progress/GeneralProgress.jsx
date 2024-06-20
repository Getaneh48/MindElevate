import { useEffect } from 'react';
import './general_progress.scss';
import PropTypes from 'prop-types';
import {useState} from 'react';

export default function GeneralProgress({selected_book}) {
    const [total_pages_read, setTotalPagesRead] = useState(0);
    

    useEffect(()=>{
        let total = 0;
        for(const index in selected_book?.reading_logs) {
            total += selected_book?.reading_logs[index].pages_read;
        }
        setTotalPagesRead(total);
    },[selected_book])
    return (
        <div className="general-progress">
            <span className="label">General Progress</span>
            <div className="pages-read-container">
                <span className="pages_read">{total_pages_read}</span>
                <span className="separator">/</span>
                <div className="total_pages"><span>{selected_book?.book.pages} </span><span className="label">pages</span></div>
            </div>

            <div className="progress-in-percent">
                <span className="count">{parseInt((total_pages_read / selected_book?.book.pages) * 100)}</span>
                <span className="text">%</span>
            </div>
        </div>
    )
 
}

GeneralProgress.propTypes = {
    selected_book: PropTypes.object,
}