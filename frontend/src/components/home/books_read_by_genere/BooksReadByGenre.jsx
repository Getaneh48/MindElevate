import './booksreadbygenre.scss';
import bb_genre_icon from '../../../assets/images/books-by-genre.png';
import acadamic_icon from '../../../assets/images/genre/academic-icon.png';
import art_icon from '../../../assets/images/genre/art-icon.png';
import business_icon from '../../../assets/images/genre/Business-and-Career.png';
import fiction_icon from '../../../assets/images/genre/fiction-icon.png';
import lifestyle_icon from '../../../assets/images/genre/Lifestyle.png';
import poletics_icon from '../../../assets/images/genre/Poletics-and-Law.png';
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import religion_icon from '../../../assets/images/genre/religion.png';
import enviroment_icon from '../../../assets/images/genre/Enviroment.png';
import health_icon from '../../../assets/images/genre/Health-and-Fitness.png';
import technology_icon from '../../../assets/images/genre/Technology.png';
import biography_icon from '../../../assets/images/genre/Biography.png';
import fiction_career_icon from '../../../assets/images/genre/Fiction-and-Literature.png';


function CountBooksByGenre({genre, count}) {
    const icons = {
        'Lifestyle': lifestyle_icon,
        'Politics & Laws': poletics_icon,
        'Technology': technology_icon,
        'Academic & Education': acadamic_icon,
        'Personal Growth': '',
        'Religion': religion_icon,
        'Science & Research': fiction_icon,
        'Enviroment': enviroment_icon,
        'Biography': biography_icon,
        'Health and Fitness': health_icon,
        'Fiction & Litrature': fiction_career_icon,
        'Business & Career': business_icon,
        'Art': art_icon
    }

    return (
        <div className="count-books-container">
            <div className="item">
                <span className="b-count">{count}</span>
                <img src={icons[genre]} alt="" />
            </div>
            <Link to="/"><span className="label">{genre}</span></Link>
           
        </div>
    )
}

export default function BooksReadByGenre() {
    const [genres, setGenres] = useState(null);

    useEffect(() => {
        const fetchGenres = async () => {
            try {
                const url = 'http://localhost:5001/api/v1/booksread/by_genres';
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    setGenres(data);
                } else {
                    console.log(response);
                }
            } catch (error) {
                console.log(error);
            }
            
        }
        fetchGenres();
    },[])


    return (
        <div className="books-read-by-genere-container">
            
            <div className="brbg_header">
                <img src={bb_genre_icon} alt="Books Read by Genre"/>
                <div className="title">Books Read by Genre</div>
            </div>
            <div className="brbg_body">
                {
                    genres ? (
                    Object.keys(genres).map((key, index) => {
                        return (
                            <CountBooksByGenre key={index} genre={key} count={genres[key]} />
                        )
                    })) : (
                        ''
                    )
                }
            </div>
        </div>
    )
}

CountBooksByGenre.propTypes = {
    genre: PropTypes.string,
    count: PropTypes.number,
}