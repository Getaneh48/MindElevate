import { useEffect, useState } from 'react';
import BookDetail from './bookdetail/BookDetail';
import './readbook.scss';
import ReadingGoal from './readinggoal/ReadingGoal';
import SearchBook from './searchbook/SearchBook';
import { useNavigate, useParams } from 'react-router';
import loading_icon from '../../assets/images/loading.gif';
import config from '../../config/config';

export default function ReadBook() {
    const navigate = useNavigate();
    const {id, ext} = useParams(null);
    const [book_to_read, setBookToRead] = useState(null);
    const [reading_info, setReadingInfo] = useState({});
    const [validation_error, setValidationError] = useState({})
    const [reset, setReset] = useState(false);
    const [show_progress, setShowProgress] = useState(false);

    

    useEffect(()=>{
        const fetchBookInfo = async () => {
            let api_url = ''
            if (ext == 'true') {
                api_url = `https://www.dbooks.org/api/book/${encodeURIComponent(id)}`;
            } else {
                api_url = `${config.api_url}/books/${encodeURIComponent(id)}`;
            }
            console.log(api_url)
            try {
                setShowProgress(true);
                const response = await fetch(`${api_url}`);
                if (response.ok){
                    const data = await response.json();
                    const bt_read = {
                        'title': data.title,
                        'authors': ext == 'true' ? data.authors : data.author,
                        'pages': data.pages,
                        'year': ext == 'true' ? data.year : data.pub_year,
                        'subtitle': data.subtitle,
                        'description': data.description,
                        'ref_id': data.id,
                        'image': ext == 'true' ? data.image : data.cover_image,
                    }

                    setBookToRead(bt_read)
                    
                }
                
                setShowProgress(false);
    
              } catch (error) {
                console.error('Error fetching data:', error);
                setShowProgress(false);
                if (error.message === 'Failed to fetch') {
                    alert('Network Error: Unable to get book information!');
                }
              }
        }

        if(id) {
           fetchBookInfo();
        }
        
    },[id])
    
    const isReadingInfoValid = () => {
        let valid = true;
        let verror = {};

        console.log(reading_info);
        if (reading_info != null) {
            if(!("pages_per_day" in reading_info) || reading_info["pages_per_day"] == ''){
               verror = {...verror, 'pages_per_day': 'required'};
               valid = false;
            }
            if (!("pages_per_hour" in reading_info) || reading_info["pages_per_hour"] == ''){
                verror = {...verror, 'pages_per_hour': 'required'};
                valid = false;
            }

            if (!("genre" in reading_info) || reading_info["genre"] == '') {
                verror = {...verror, 'genre': 'required'};
                valid = false;
            }

            if (!("days_to_finish" in reading_info) || reading_info["days_to_finish"] == '') {
                verror = {...verror, 'days_to_finish': 'required'};
                valid = false;
            }
        } else {
            valid = false;
            verror = {...verror, 'pages_per_day': 'required'};
            verror = {...verror, 'pages_per_hour': 'required'};
            verror = {...verror, 'days_to_finish': 'required'};
            verror = {...verror, 'genre': 'required'};
        }

        if (valid){
            return true
        } else {
            console.log('validation error');
            console.log(verror);
            setValidationError(verror);
            return false;
        }
    }

    const handleSaveBook = async () => {
       
        //now send the data to an api server
        if(isReadingInfoValid()) {
            setShowProgress(true);
            const data = {
                'book': book_to_read,
                'reading_info': reading_info,
            }

            try{
                const url = `${config.api_url}/booksreading`;
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                };

                // Make the fetch request
                const response = await fetch(url, options);
                console.log(response);
                if (response.ok) {
                    // Parse the response as JSON
                    const responseData = await response.json();
                    console.log(responseData);
                    if (responseData.success) {
                        alert("Data Saved!")
                        navigate('/melv')
                    } else {
                        alert(responseData.message)
                    }
                }

                setShowProgress(false);

            } catch(error) {
                setShowProgress(false);
                console.log(error);
                if (error.message === 'Failed to fetch') {
                    alert('Network Error: Unable to save book information!');
                }
            }

        }
    }

    const handleReset = () => {
        console.log('resetting the form...');
        setReset(!reset);
    }

    return (
        <div className="read-book-container">
            <section className={`${show_progress ? 'loading active' : 'loading'}`}> <img src={loading_icon} alt="Loading in progress" /></section>
            <SearchBook setBookToReadNow={setBookToRead} reset_form={reset} setShowProgress={setShowProgress}/>
            <BookDetail book_to_read={book_to_read} reading_info={reading_info} setReadingInfo={setReadingInfo} validation_error={validation_error} reset_form={reset}/>
            <ReadingGoal book_to_read={book_to_read} reading_info={reading_info} setReadingInfo={setReadingInfo} validation_error={validation_error} reset_form={reset}/>
            <section className="actions">
                <button className='save-reading' onClick={handleSaveBook}>Save</button>
                <button className='reset' onClick={handleReset}>Reset</button>
            </section>
        </div>
    )
}