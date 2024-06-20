import './reading_goal.scss';
import PropTypes from 'prop-types';

export default function ReadingGoal({selected_book}) {
    return (
        <div className="reading-goal-continer">
            <div className="page-goal">
                <span className="label">Daily Goal</span>
                <div className="page-goal-text">
                    <span className="count">{selected_book?.pages_per_day}</span>
                    <span className="text">pages</span>
                </div>
            </div>
            <div className="finish-goal">
                <span className="label">Finishing Goal</span>
                <div className="finish-goal-text">
                    <span className="text1">In</span>
                    <span className="count">{selected_book?.expected_completion_day}</span>
                    <span className="text">Days</span>
                </div>
            </div>
        </div>
    )
}

ReadingGoal.propTypes = {
    selected_book: PropTypes.object,
}