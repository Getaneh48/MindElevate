import './dailyreading.scss';
import pages_read_icon from '../../../../assets/images/pages_read.png';
import hour from '../../../../assets/images/24_hour.png';
import open_book from '../../../../assets/images/open-book-2.png';
import daily_badge from '../../../../assets/images/badges/daily_badge.png';
import progress_icon from '../../../../assets/images/progress_icon.png'
import PropTypes from 'prop-types';


export default function DailyReading({breading}) {
    
    return (
        <article className='daily-reading'>
                <div className="book-info">
                    <div className="book-cover-image"><img src={open_book} /></div>
                    <div className="book-desc">
                        <span className="book-title">Title - {breading?.book.title}</span>
                        <span className="book-author">Author - {breading?.book.author}</span>
                        <span className="book-total-pages">Total Pages - {breading?.book.total_pages} pages</span>
                    </div>
                </div>
                <div className="daily-status">
                    <div className="pages-read">
                        <div className="icon"><img src={pages_read_icon} /></div>
                        <div className="pages-read-info"><span className="d-read">{breading?.pages_read}</span><span className="separator">/</span><span className="p-daily-goal">{breading?.pages_per_day}</span> <span className="text">Pages</span></div>
                    </div>

                    <div className="hours-read">
                        <div className="icon"><img src={hour} /></div>
                        <div className="hours-read-info"><span className="h-read">{breading?.hours_read}</span> <span className="h-text">Hour</span></div>
                    </div>
                </div>
                <div className="right-info">
                    {breading?.goal_achieved ? (
                        <div className="badge">
                            <img src={daily_badge}/>
                        </div>
                    ) : (
                        <div className="percent-info">
                            <div className="icon"><img src={progress_icon} /></div>
                            <span className="percent">{(breading?.pages_read / breading?.pages_per_day) * 100} %</span>
                        </div>
                    )}
                    
                    
                </div>
        </article>
    )
}
DailyReading.propTypes = {
    breading: PropTypes.object.isRequired,
};