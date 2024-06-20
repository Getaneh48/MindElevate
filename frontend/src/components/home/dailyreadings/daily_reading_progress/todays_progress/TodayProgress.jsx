import { useEffect } from 'react';
import './today_progress.scss';
import PropTypes from 'prop-types';
import {useState} from 'react';
import daily_badge from '../../../../../assets/images/badges/daily_badge.png';

export default function TodayProgress({selected_book}) {
    const [today_pages_read, setTodayPagesRead] = useState(0);
    const [goal_achieved, setGoalAchieved] = useState(false);

    useEffect(()=>{
        let pread = 0;
        console.log(selected_book)
        if(selected_book.reading_logs.length > 0){
            for( let index in selected_book?.reading_logs) {
                const rlog = selected_book?.reading_logs[index];
                console.log(rlog);
                pread += rlog.pages_read;
                
            }

            if(pread >= selected_book?.pages_per_day) {
                setGoalAchieved(true);
            }
            console.log(pread);
            setTodayPagesRead(pread);
        }
    },[selected_book])
    return (
        <div className="today-progress-container">
            <span className="label">Today&apos;s Progress</span>
            <div className="pages-per-goal">
                <span className="pages_read">{today_pages_read}</span>
                <span className="separator">/</span>
                <span className="pages_goal"><span>{selected_book?.pages_per_day}</span> <span className="label">pages</span></span>
            </div>

            {
                goal_achieved ? (
                    <div className="badge">
                        <img src={daily_badge} alt="" />
                    </div>
                ) : (
                    <div className="progress-in-percent">
                        <span className="count">{parseInt((today_pages_read / selected_book?.pages_per_day) * 100)}</span>
                        <span className="text">%</span>
                    </div>
                )
            }
            
        </div>
    )
 
}

TodayProgress.propTypes = {
    selected_book: PropTypes.object,
}