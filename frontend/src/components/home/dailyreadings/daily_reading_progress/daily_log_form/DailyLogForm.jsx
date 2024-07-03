import { useState } from 'react';
import './daily_log_form.scss';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router';
import config from '../../../../../config/config';

export default function DailyLogForm({selected_book, setShowDailyLogForm}) {
    const [pages_read, setPagesRead] = useState('');
    const [hours_read, setHoursRead] = useState('');
    const navigate = useNavigate();

    const handleShowForm = () => {
        setShowDailyLogForm(false)
    }

    const handleSavingReadingLog = async() => {
        if (selected_book) {
            if (pages_read > selected_book.book.pages){
                alert("Pages read cannot be greater than total pages of the book!");
                setPagesRead('');
                return;
            }
            if (hours_read > 24){
                alert("Hours read cannot be greater than 24 hour!");
                setHoursRead('');
                return;
            }

            const reading_log = {
                'br_id': selected_book.id,
                'pages_read': parseInt(pages_read),
                'hours_read': parseInt(hours_read),
            }
            console.log(reading_log);

            const url = `${config.api_url}/books_reading/${selected_book.id}/logs`;
            try {
                    const response = await fetch(url, {
                        method: 'POST',
                        headers: { 
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(reading_log),
                    });

                    if(response.ok) {
                        const data = await response.json();
                        console.log(data);
                        if (data.success) {
                            alert('Daily Log added successfully!');
                            navigate('/melv');
                        } else {
                            alert(data.message);
                        }
                    } else {
                        alert('Unknown Error Occured!');
                        console.log(response);
                    }
            } catch (error) {
                console.log(error);
            }
        }
    }

    return (
        <div className={'daily-log-form'}>
            <div className="daily-log-form-header">
                <span className="dlf-header-title">Add Today&apos;s Log</span>
                <span className="dlg-form-close" onClick={handleShowForm}>x</span>
            </div>
            <div className="daily-log-form-body">
                <div className="dlgf-frm-group">
                    <span className="input-label">Pages Read</span>
                    <input value={pages_read} onChange={(e)=>setPagesRead(e.currentTarget.value)} type="text" className='pages_read_input'/>
                </div>
                <div className="dlgf-frm-group">
                <span className="input-label">Hours Read</span>
                <input value={hours_read} onChange={(e)=>setHoursRead(e.currentTarget.value)} type="text" className='hours_read_input'/>
                </div>
            </div>
            <div className="daily-log-form-footer">
                <button className="save" onClick={handleSavingReadingLog}>Save</button>
            </div>
        </div>
    )
}

DailyLogForm.propTypes = {
    selected_book: PropTypes.object,
    setShowDailyLogForm: PropTypes.func,
}