import { useEffect } from 'react';
import AddBookBtn from '../../components/home/addbookbtn/AddBookBtn';
import BooksReadByGenre from '../../components/home/books_read_by_genere/BooksReadByGenre';
import DailyReadings from '../../components/home/dailyreadings/DailyReadings';
import RecommendedBooks from '../../components/home/recommended_books/RecommendedBooks';
import './home.scss';

export default function Home() {
    useEffect(() => {
        const api_url = 'http://localhost:5001/api/v1/status';
        const checkApiServerStatus = async () => {
            try{
                const response = await fetch(`${api_url}`);
                const data = await response.json();
                console.log(data);
            } catch (error) {
                if (error.message === 'Failed to fetch') {
                    console.log('unable to communicate with the api server');
                    // alert('API Server unavailable!');
                }
            }
            
        }
        checkApiServerStatus();
    },[])
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