import { Link } from 'react-router-dom';
import './leftsidemainmenu.scss';
import home_icon_active from '../../../assets/images/Home-active.png';
import open_book from '../../../assets/images/open-book.png';
import bookmarked_books from '../../../assets/images/bookmarked_books.png';
import favorite_books from '../../../assets/images/favorite-books.png';
import reading_friends from '../../../assets/images/reading_friends.png';

export default function LeftSideMainMenu() {
    return (
        <div className='main-menu'>
            <nav>
                <ul>
                    <li>
                        <Link to="/"><img src={home_icon_active} /></Link>
                    </li>
                    <li>
                        <Link to="/"><img src={open_book} /></Link>
                    </li>
                    <li>
                        <Link to="/"><img src={bookmarked_books} /></Link>
                    </li>
                    <li>
                        <Link to="/"><img src={favorite_books} /></Link>
                    </li>
                    <li>
                        <Link to="/"><img src={reading_friends} /></Link>
                    </li>
                </ul>
            </nav>
        </div>
    )
}