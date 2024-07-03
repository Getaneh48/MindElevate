import './daily_reading_progress.scss';
import reading_progress_icon from '../../../../assets/images/reading-progress.png';
import BooksOnProgress from './books_on_progress/BooksOnProgress';
import { useParams } from 'react-router';
import { useEffect, useState } from 'react';
import DetailReadingProgress from './detail_reading_progress/DetailReadingProgress';
//import GeneralProgress from './general_progress/GeneralProgress';
import config from '../../../../config/config';

export default function DailyReadingProgress() {
    const {id} = useParams(null);
    const [books_reading, setBooksReading] = useState([]);
    const [selected_book, setSelectedBook] = useState(null);
    const url = `${config.api_url}/books_reading/onprogress`;

    useEffect(()=> {
        const fetch_books_onreading = async ()=> {
            try {
                const response = await fetch(url);
                if (response.ok) {
                    const responseData = await response.json();
                    console.log(responseData);
                    setBooksReading(responseData);
                } else {
                    console.log(response);
                }
            } catch (error) {
                console.log(error);
            }
        }

        fetch_books_onreading();
    },[]);

    useEffect(()=> {
        console.log(id);
        if (id != null) {
            console.log(books_reading)
            if (books_reading != null) {
                let found = null;
                for(let ind in books_reading) {
                    let br = books_reading[ind]
                    if (br.id == id) {
                        found = br;
                        console.log(found);
                        break;
                    }
                }

                if (found != null) {
                    setSelectedBook(found);
                }
            }
        } else {
            setSelectedBook(books_reading[0]);
        }
    },[id, books_reading])

    return (
        <div className="daily-reading-progress-container">
            <div className="daily-reading-progress-header">
                <img src={reading_progress_icon} alt="Reading progress icon" className="header-icon"/>
                <span className="daily-reading-progress-title">Daily Reading Progress</span>
            </div>

            <div className="daily-reading-progress-body">
                {
                    selected_book && books_reading.length > 0 ? (
                        <>
                        <BooksOnProgress books_reading={books_reading} selected_book={selected_book} setSelectedBook={setSelectedBook}/>
                        <DetailReadingProgress selected_book={selected_book}/>
                        </>
                    ) : (
                        <h3>Not found</h3>
                    )
                }
                
            </div>
        </div>

        
    )
}
