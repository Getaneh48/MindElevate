import AddBookBtn from '../../components/home/addbookbtn/AddBookBtn';
import BooksReadByGenre from '../../components/home/books_read_by_genere/BooksReadByGenre';
import DailyReadings from '../../components/home/dailyreadings/DailyReadings';
import RecommendedBooks from '../../components/home/recommended_books/RecommendedBooks';
import './home.scss';

export default function Home() {
    return (
        <div className="home-container">
            <section className="home-components">
                <DailyReadings />
                <RecommendedBooks />
                <BooksReadByGenre />
            </section>
            <AddBookBtn />
        </div>
    )
}