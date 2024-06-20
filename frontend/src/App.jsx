
import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import ReadBook from './components/readbook/ReadBook';
import DailyReadingProgress from './components/home/dailyreadings/daily_reading_progress/DailyReadingProgress';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<MainLayout />}>
            <Route exact path="readbook" element={<ReadBook />} />
            <Route exact path="readbook/:id" element={<ReadBook />} />
            <Route exact path="readingprogress" element={<DailyReadingProgress />} />
            <Route exact path="readingprogress/:id" element={<DailyReadingProgress />} />
        </Route>
      </Routes>
    </Router>
  )
}

export default App
