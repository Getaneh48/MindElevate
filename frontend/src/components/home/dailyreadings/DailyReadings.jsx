import DailyReading from './dailyreading/DailyReading';
import './dailyreadings.scss';
import todays_reading_icon from '../../../assets/images/todays-reading.png';
import warning_icon from '../../../assets/images/warning.png';

import { useContext, useEffect, useState } from 'react';
import config from '../../../config/config';
import AccountContext from '../../../context/AccountContext';

export default function DailyReadings() {
    const {token} = useContext(AccountContext);
    const url = `${config.api_url}/books_reading/onprogress`;
    const [books_reading, setBooksReading] = useState([]);
    const [error, setError] = useState(false);

    useEffect(() => {

        const fetch_books_onreading = async ()=> {
            try {
                const options = {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                };
                const response = await fetch(url, options);
                if (response.ok) {
                    const responseData = await response.json();
                    console.log(responseData);
                    setBooksReading(responseData);
                } else {
                    console.log(response);
                }
            } catch (error) {
                console.log(error);
                if (error.message === 'Failed to fetch') {
                    setError(true);
                }
            }
        }

        fetch_books_onreading();

    },[]);

    return (
        <section className='daily-readings'>
            
            <div className="daily-readings-header">
                <img src={todays_reading_icon}/>
                <span className="title">Today&apos;s Reading</span>
            </div>
            <div className="daily-readings-body">
                <div className={`${error ? "message-area" : "message-area"}`}><img src={warning_icon} alt="Warning Icon" /><span className="error">Network Error</span></div>
                {
                    books_reading.map((breading, index) => {
                        return <DailyReading breading={breading} key={index}/>  
                    })
                    
                }
            </div>
            


        </section>
    )
}