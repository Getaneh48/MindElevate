
import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import ReadBook from './components/readbook/ReadBook';
import DailyReadingProgress from './components/home/dailyreadings/daily_reading_progress/DailyReadingProgress';
import BooksRead from './pages/booksread/BooksRead';
import BookmarkedBooks from './pages/bookmarked_books/BookmarkedBooks';
import FavoriteBooks from './pages/favorite_books/FavoriteBooks';
import LandingPage from './pages/landing_page/LandingPage';
import Login from './pages/accounts/Login';
import Register from './pages/accounts/Register';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/login" element={<Login />} />
        <Route exact path="/register" element={<Register />} />
        <Route exact path="/" element={<LandingPage />} />
        <Route exact path="/melv" element={<MainLayout />}>
            <Route exact path="readbook" element={<ReadBook />} />
            <Route exact path="readbook/:id/ext/:ext" element={<ReadBook />} />
            <Route exact path="readingprogress" element={<DailyReadingProgress />} />
            <Route exact path="readingprogress/:id" element={<DailyReadingProgress />} />
            <Route exact path="booksread" element={<BooksRead />} />
            <Route exact path="bookmarked" element={<BookmarkedBooks />} />
            <Route exact path="favorites" element={<FavoriteBooks />} />
        </Route>
      </Routes>
    </Router>
  )
}

export default App
