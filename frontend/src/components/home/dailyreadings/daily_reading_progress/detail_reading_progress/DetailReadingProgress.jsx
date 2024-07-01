import { useState } from 'react';
import DailyLogForm from '../daily_log_form/DailyLogForm';
import GeneralProgress from '../general_progress/GeneralProgress';
import ReadingGoal from '../reading_goal/ReadingGoal';
import TodayProgress from '../todays_progress/TodayProgress';
import './detail_reading_progress.scss';
import PropTypes from 'prop-types';
import open_book_4 from '../../../../../assets/images/open-book-4.png';
import DailyProgressChart from '../daily_progress_by_chart/DailyProgressChart';

export default function DetailReadingProgress({selected_book}) {
    const [show_daily_log_form, setShowDailyLogForm] = useState(false);

    console.log(selected_book);
    return (
        <div className="detail-reading-progress-container">
            <div className="progress-info-container">
                <div className="book-info-container">
                    <div className="book-info">
                        <div className="cover-image">
                            <img src={selected_book?.book.cover_image ? selected_book?.book.cover_image : open_book_4} alt="Book Cover Image" />
                        </div>
                        <div className="book-basic-info">
                            <span className="title">{selected_book?.book.title}</span>
                            <span className="authors">Authors - {selected_book?.book.author}</span>
                            <span className="genre">Genre - {selected_book?.book.genre.name}</span>
                            <span className="pub_year">Publication - {selected_book?.book.pub_year}</span>
                            <span className="pages">Pages - {selected_book?.book.pages}</span>
                        </div>
                    </div>
                    <div className="actions">
                        <span className="label" onClick={()=>setShowDailyLogForm(true)}>Add Daily Log</span>
                        <span className="icon" onClick={()=>setShowDailyLogForm(true)}>+</span>
                    </div>
                </div>
                <div className={`${show_daily_log_form ? 'daily-log-form-container' : 'hide daily-log-form-container'}`}>
                    <DailyLogForm selected_book={selected_book} setShowDailyLogForm={setShowDailyLogForm}/>
                </div>

                <div className="reading-goals-container">
                    <ReadingGoal selected_book={selected_book} />
                    <DailyProgressChart selected_book={selected_book}/>
                </div>

                <div className="todays-progress-conta">
                    <TodayProgress selected_book={selected_book}/>
                </div>
            </div>
            <div className="reading-history-chart-container"></div>
            <div className="general-progress-container">
                <GeneralProgress selected_book={selected_book} />
            </div>
        </div>
    )
}

DetailReadingProgress.propTypes = {
    selected_book: PropTypes.object,
}