import './recommendedbooks.scss';
import recommended_books_icon from '../../../assets/images/recommended_books.png'
import RecommendedBook from './recommended_book/RecommendedBook';
import { useEffect, useState } from 'react';
import loading_icon from '../../../assets/images/loading.gif';
import warning_icon from '../../../assets/images/warning.png';

export default function RecommendedBooks() {
    const [recommended_books, setRecommendedBooks] = useState([]);
    const [loading_recommendation, setLoadingRecommendation] = useState(false);
    const [error, setError] = useState(false);

    useEffect(()=>{
        const getRecommendation = async () => {
            const url = 'http://localhost:5001/api/v1/books_recommended';
            try {
                setLoadingRecommendation(true)
                const response = await fetch(url);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    setRecommendedBooks(data);
                    setLoadingRecommendation(false);
                }
            } catch (error) {
                console.log(error);
                if (error.message === 'Failed to fetch') {
                    setError(true);
                }
                setLoadingRecommendation(false);
            }
            
        }

        getRecommendation();
    },[])

    return (
        <section className="recommended_books_container">
            <div className="rbooks_header">
                    <img src={recommended_books_icon} alt="Handbook of Medical Herbs"/>
                    <div className="title">Recommended Books</div>
            </div>
            <div className={`${loading_recommendation ? "active loading-progress" : "loading-progress"}`}><img src={loading_icon} alt="Loading recommended books in progress" /></div>
            <div className="rbooks_body">
                <div className={`${error ? "error message-area" : "message-area"}`}><img src={warning_icon} alt="Warning icon" /><span className="error">Network Error</span></div>
                {
                    recommended_books ? (
                        recommended_books?.map((rbook, index) => {
                            return (
                                <RecommendedBook rbook={rbook} key={index} />
                            )
                        })
                    ) : (
                        <h3>No recommendation available</h3>
                    )
                    
                }
                
            </div>
        </section>
    )
}