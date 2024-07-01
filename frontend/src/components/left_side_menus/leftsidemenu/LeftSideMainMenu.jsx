import { Link } from 'react-router-dom';
import './leftsidemainmenu.scss';
//import home_icon_active from '../../../assets/images/Home-active.png';
//import home_icon from '../../../assets/images/Home.png';
import books_read_active_icon from '../../../assets/images/books-read-2-active.png';
import books_read_icon from '../../../assets/images/books-read-2.png';
//import open_book from '../../../assets/images/open-book.png';
import dashboard_icon from '../../../assets/images/dashboard.png';
import dashboard_active_icon from '../../../assets/images/dashboard-active.png';
import bookmarked_books from '../../../assets/images/bookmarked_books.png';
import bookmarked_books_active from '../../../assets/images/bookmarked_book_active.png';
import favorite_books from '../../../assets/images/favorite-books-2.png';
import favorite_books_active from '../../../assets/images/favorite-books-active.png';
import reading_friends from '../../../assets/images/reading_friends.png';
import { useState } from 'react';

export default function LeftSideMainMenu() {
    const [active_menu_id, setActiveMenu] = useState(1);
    return (
        <div className='main-menu'>
            <nav>
                <ul>
                    <li>
                        <Link to="/melv" onClick={()=>setActiveMenu(1)}>
                            {
                                active_menu_id == 1 ? (
                                    <img src={dashboard_active_icon} alt="Dashboard icon active"/>
                                ) : (
                                    <img src={dashboard_icon} alt="Dashboard" />
                                )
                            }
                            
                        </Link>
                    </li>
                    <li>
                        <Link to="/melv/booksread" onClick={()=>setActiveMenu(2)}>
                            {
                                    active_menu_id == 2 ? (
                                        <img src={books_read_active_icon} />
                                    ) : (
                                        <img src={books_read_icon} alt="Book Read" />
                                    )
                            }
                        
                        </Link>
                    </li>
                    <li>
                        <Link to="/melv/bookmarked" onClick={()=>setActiveMenu(3)}>
                            {
                                    active_menu_id == 3 ? (
                                        <img src={bookmarked_books_active} />
                                    ) : (
                                        <img src={bookmarked_books} />
                                    )
                            }
                            
                        </Link>
                    </li>
                    <li>
                        <Link to="/melv/favorites" onClick={()=>setActiveMenu(4)}>
                        {
                                active_menu_id == 4 ? (
                                    <img src={favorite_books_active} />
                                ) : (
                                    <img src={favorite_books} />
                                )
                        }
                        </Link>
                    </li>
                    <li>
                        <Link to="/melv"><img src={reading_friends} /></Link>
                    </li>
                </ul>
            </nav>
        </div>
    )
}