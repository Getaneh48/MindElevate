import DailyReading from './dailyreading/DailyReading';
import './dailyreadings.scss';
import open_book from '../../../assets/images/open-book-2.png';

export default function DailyReadings() {
    const books_reading = [
        {
            'book' : {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'total_pages': '400',
                'cover_image':null,
            },
            'pages_per_day': 20,
            'pages_read': 20,
            'hours_read': 2,
            'goal_achieved': true,
        },
        {
            'book' : {
                'title': 'Secrets of the millionair mind',
                'author': 'T. Harv Eker',
                'total_pages': '320',
                'cover_image':null,
            },
            'pages_per_day': 20,
            'pages_read': 10,
            'hours_read': 2,
            'goal_achieved': false,
        },
    ]

    return (
        <section className='daily-readings'>
            <div className="daily-readings-header">
                <img src={open_book}/>
                <span className="title">Daily Readings</span>
            </div>
            <div className="daily-readings-body">
                {
                    books_reading.map((breading, index) => {
                        console.log(breading);
                        return <DailyReading breading={breading} key={index}/>  
                    })
                    
                }
            </div>
            


        </section>
    )
}