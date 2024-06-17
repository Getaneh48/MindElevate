import './readinggoal.scss';
import reading_goal_icon from '../../../assets/images/reading-goal.png';
import PropTypes from 'prop-types';
import { useEffect, useState} from 'react';

export default function ReadingGoal({book_to_read, reading_info, setReadingInfo, validation_error, reset_form}) {
    const [pages_per_day, setPagesPerDay] = useState('');
    const [pages_per_hour, setPagesPerHour] = useState('');
    const [days_to_finish, setDaysToFinish] = useState('');

    const handlePagesPerDay = (e) => {
        setPagesPerDay(e.currentTarget.value);
        if(reading_info != null){
            setReadingInfo({...reading_info, 'pages_per_day': e.currentTarget.value});
        }
    }

    const handlePagesPerHour = (e) => {
        setPagesPerHour(e.currentTarget.value);
        if(reading_info != null) {
            setReadingInfo({...reading_info, 'pages_per_hour': e.currentTarget.value});
        }
    }

    const handleDaysToFinish = (e) => {
        setDaysToFinish(e.currentTarget.value);
        if(reading_info != null){
            setReadingInfo({...reading_info, 'days_to_finish': e.currentTarget.value});
        }
        
    }

    useEffect(() => {
        setPagesPerDay('');
        setPagesPerHour('');
        setDaysToFinish('');
    },[book_to_read, reset_form]);

    return (
        <div className="reading-goal-container">
            <div className="reading-goal-header">
                <div className="reading-goal-icon"><img src={reading_goal_icon} alt="Reading Goal Icon" /></div>
                <div className="reading-goal-title">Reading Goal</div>
            </div>
            <div className="reading-goal-body">
                <div className="form-group">
                    <p>
                        <span className="label">Pages / Day</span>
                        {
                            ("pages_per_day" in validation_error) ? (
                                <input  type="text" value={pages_per_day} onInput={handlePagesPerDay} className="error"/>
                            ) : (
                                <input  type="text" value={pages_per_day} onInput={handlePagesPerDay}/>
                            )
                        }
                        
                    </p>
                    <p>
                        <span className="label">Hours / Day</span>
                        {
                            ("pages_per_hour" in validation_error) ? (
                                <input type="text" value={pages_per_hour} onInput={handlePagesPerHour} className="error"/>
                            ): (
                                <input type="text" value={pages_per_hour} onInput={handlePagesPerHour}/>
                            )
                        }
                        
                    </p>
                    
                    <p>
                        <span className="label">Days to Finish</span>
                        {
                            ("days_to_finish" in validation_error) ? (
                                <input type="text" value={days_to_finish} onInput={handleDaysToFinish} className="error"/>
                            ): (
                                <input type="text" value={days_to_finish} onInput={handleDaysToFinish} />
                            )
                        }
                        
                    </p>
                </div>
                    
            </div>
            
        </div>
    )
}

ReadingGoal.propTypes = {
    book_to_read: PropTypes.object,
    validation_error: PropTypes.object,
    reading_info: PropTypes.object,
    setReadingInfo: PropTypes.func,
    reset_form: PropTypes.bool,
};