import './dailyreading.scss';
import pages_read_icon from '../../../../assets/images/pages_read.png';
import hour from '../../../../assets/images/24_hour.png';
import daily_badge from '../../../../assets/images/badges/daily_badge.png';
import progress_icon from '../../../../assets/images/progress_icon.png'
import PropTypes from 'prop-types';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';


export default function DailyReading({breading}) {
    const [today_reading, setTodayReading] = useState({'pages_read': 0, 'hours_read':0});
    const [goal_achieved, setGoalAchieved] = useState(false);

    useEffect(() => {
        if (breading?.reading_logs.length > 0) {
            let pages_read = 0;
            let hours_read = 0;
            for(let index in breading?.reading_logs){
                //console.log(rlog)
                pages_read += breading?.reading_logs[index].pages_read;
                hours_read += breading?.reading_logs[index].hours_read;
            }
            const reading = {
                'pages_read': pages_read,
                'hours_read': hours_read,
            }

            if(pages_read >= breading?.pages_per_day && hours_read >= breading?.hours_per_day){
                setGoalAchieved(true);
            }
            console.log(reading);
            setTodayReading(reading)
        } 
    }, [breading])

    return (
        <Link to={`/readingprogress/${breading?.id}`}>
        <article className='daily-reading'>
                <div className="book-info">
                    <div className="book-cover-image"><img src={breading?.book.cover_image} /></div>
                    <div className="book-desc">
                        <span className="book-title">{breading?.book.title}</span>
                        <span className="book-author">Authors - {breading?.book.author}</span>
                        <span className="genre">Genre - {breading?.book.genre.name}</span>
                        <span className="publication">Year - {breading?.book.pub_year}</span>
                        <span className="book-total-pages">Total Pages - {breading?.book.pages} pages</span>
                    </div>
                </div>
                <div className="daily-status">
                    <div className="pages-read">
                        <div className="icon"><img src={pages_read_icon} /></div>
                        <div className="pages-read-info"><span className="d-read">{today_reading?.pages_read}</span><span className="separator">/</span><span className="p-daily-goal">{breading?.pages_per_day}</span> <span className="text">Pages</span></div>
                    </div>

                    <div className="hours-read">
                        <div className="icon"><img src={hour} /></div>
                        <div className="hours-read-info"><span className="h-read">{today_reading?.hours_read}</span><span className="separator">/</span> <span className="h-daily-goal">{breading?.hours_per_day}</span> <span className="h-text">Hour</span></div>
                    </div>
                </div>
                <div className="right-info">
                    {goal_achieved ? (
                        <div className="badge">
                            <img src={daily_badge}/>
                        </div>
                    ) : (
                        <div className="percent-info">
                            <div className="icon"><img src={progress_icon} /></div>
                            <span className="percent">{parseInt((today_reading?.pages_read / breading?.pages_per_day) * 100)} %</span>
                        </div>
                    )}
                    
                    
                </div>
        </article>
        </Link>
    )
}
DailyReading.propTypes = {
    breading: PropTypes.object.isRequired,
};