import './booksreadbygenre.scss';
import bb_genre_icon from '../../../assets/images/books-by-genre.png';
import PropTypes from 'prop-types';
import acadamic_icon from '../../../assets/images/genre/academic-icon.png';
import art_icon from '../../../assets/images/genre/art-icon.png';
import business_icon from '../../../assets/images/genre/business-icon.png';
import fiction_icon from '../../../assets/images/genre/fiction-icon.png';
import { Link } from 'react-router-dom';


function CountBooksByGenre({genre, count}) {
    const icons = {
        'Art': art_icon,
        'Business': business_icon,
        'Fiction': fiction_icon,
        'Academic': acadamic_icon,
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

    const lists = [
        {
            'genre': 'Art',
            'count': 0
        },
        {
            'genre': 'Business',
            'count': 2,
        },
        {
            'genre': 'Fiction',
            'count': 10,
        },
        {
            'genre': 'Academic',
            'count': 3
        }
    ];

    return (
        <section className="books-read-by-genere-container">
            <div className="brbg_header">
                <img src={bb_genre_icon} alt="Books Read by Genre"/>
                <div className="title">Books Read by Genre</div>
            </div>
            <div className="brbg_body">
                {
                    lists.map((list, index) => {
                        return (
                            <CountBooksByGenre key={index} genre={list.genre} count={list.count} />
                        )
                    })
                }
            </div>
        </section>
    )
}

CountBooksByGenre.propTypes = {
    genre: PropTypes.string.isRequired,
    count: PropTypes.number.isRequired,
};