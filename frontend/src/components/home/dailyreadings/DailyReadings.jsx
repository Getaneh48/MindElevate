import DailyReading from './dailyreading/DailyReading';
import './dailyreadings.scss';
import open_book from '../../../assets/images/open-book-2.png';
import { useEffect, useState } from 'react';

export default function DailyReadings() {
    const url = 'http://localhost:5001/api/v1//books_reading/onprogress';
    const [books_reading, setBooksReading] = useState([]);

    useEffect(() => {

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

    return (
        <section className='daily-readings'>
            <div className="daily-readings-header">
                <img src={open_book}/>
                <span className="title">Today&apos;s Reading</span>
            </div>
            <div className="daily-readings-body">
                {
                    books_reading.map((breading, index) => {
                        return <DailyReading breading={breading} key={index}/>  
                    })
                    
                }
            </div>
            


        </section>
    )
}