import { useEffect, useState } from 'react';
import BookDetail from './bookdetail/BookDetail';
import './readbook.scss';
import ReadingGoal from './readinggoal/ReadingGoal';
import SearchBook from './searchbook/SearchBook';
import { useNavigate, useParams } from 'react-router';

export default function ReadBook() {
    const navigate = useNavigate();
    const {id} = useParams(null);
    const [book_to_read, setBookToRead] = useState(null);
    const [reading_info, setReadingInfo] = useState({});
    const [validation_error, setValidationError] = useState({})
    const [reset, setReset] = useState(false);

    

    useEffect(()=>{
        const fetchBookInfo = async () => {
            const api_url = `https://www.dbooks.org/api/book/${encodeURIComponent(id)}`;
            try {
                const response = await fetch(`${api_url}`);
                const data = await response.json();
                const bt_read = {
                    'title': data.title,
                    'authors': data.authors,
                    'pages': data.pages,
                    'year': data.year,
                    'subtitle': data.subtitle,
                    'description': data.description,
                    'ref_id': data.id,
                    'image': data.image
                }

                setBookToRead(bt_read)
    
              } catch (error) {
                console.error('Error fetching data:', error);
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

    const handleSaveBook = () => {
       
        //now send the data to an api server
        if(isReadingInfoValid()) {
            const data = {
                'book': book_to_read,
                'reading_info': reading_info,
            }

            console.log(data);
            console.log('saving data...');

            navigate('/')
        }
    }

    const handleReset = () => {
        console.log('resetting the form...');
        setReset(!reset);
    }

    return (
        <div className="read-book-container">
            <SearchBook setBookToReadNow={setBookToRead} reset_form={reset}/>
            <BookDetail book_to_read={book_to_read} reading_info={reading_info} setReadingInfo={setReadingInfo} validation_error={validation_error} reset_form={reset}/>
            <ReadingGoal book_to_read={book_to_read} reading_info={reading_info} setReadingInfo={setReadingInfo} validation_error={validation_error} reset_form={reset}/>
            <section className="actions">
                <button className='save-reading' onClick={handleSaveBook}>Save</button>
                <button className='reset' onClick={handleReset}>Reset</button>
            </section>
        </div>
    )
}