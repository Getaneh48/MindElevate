import { useContext, useEffect } from 'react';
import './general_progress.scss';
import PropTypes from 'prop-types';
import {useState} from 'react';
import config from '../../../../../config/config';
import AccountContext from '../../../../../context/AccountContext';

export default function GeneralProgress({selected_book}) {
    const {token} = useContext(AccountContext);
    const [total_pages_read, setTotalPagesRead] = useState(0);
    

    useEffect(()=>{
        const getAllLogs = async () => {
            try {
                const url = `${config.api_url}/books_reading/${selected_book.id}/logs`;
                const options = {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                };
                const response = await fetch(url, options);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);

                    let total = 0;
                    for(const index in data) {
                        total += data[index].pages_read;
                    }
                    setTotalPagesRead(total);
                }
            } catch (error) {
                if (error.message == '') {
                    console.log('Network error');
                }
            }
        }

        getAllLogs();
        
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