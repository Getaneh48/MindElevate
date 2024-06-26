import './dailyprogresschart.scss';
import prev_icon from '../../../../../assets/images/prev.png';
import next_icon from '../../../../../assets/images/next.png';
import { BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';
import PropTypes from 'prop-types';
import MonthSelector from '../../../../month_selector/MonthSelector';
import { useEffect, useState } from 'react';



const MyBarChart = ({ data, max_page }) => {
    // Format date for x-axis labels
    const formatDate = (dateStr) => {
      const date = new Date(dateStr);
      return date.toLocaleDateString();
    };
  
    return (
      <BarChart width={700} height={300} data={data}>
        <XAxis dataKey="date" tickFormatter={formatDate}/>
        <YAxis  domain={[0, max_page]}/>
        <Tooltip />
        <Bar dataKey="total_pages" fill="#1a5678" />
      </BarChart>
    );
  };
  
export default function DailyProgressChart({selected_book}) {
    const [selected_month, setSelectedMonth] = useState(0);
    const [week, setWeek] = useState(1);
    const [datas, setData] = useState(null);
    const [all_readings, setAllReadings] = useState([]);
    
    function getNumberOfWeeksInMonth(year, month) {
        // Create a date object at the first day of the specified month
        const date = new Date(year, month, 1);
      
        // Get the day of the week (0 for Sunday, 6 for Saturday)
        const firstDay = date.getDay();
      
        // Get the last date of the month
        const lastDate = new Date(year, month + 1, 0);
      
        // Calculate the number of days in the month
        const numDays = lastDate.getDate();
      
        // Adjust for weeks starting on Sunday (add 1 if first day is Sunday)
        let adjustedDays = numDays + (firstDay === 0 ? 1 : 0);
      
        // Calculate the number of complete weeks (adjusted days divided by 7 with ceiling)
        let numWeeks = Math.ceil(adjustedDays / 7);
      
        // Check if there are any extra days in the last week
        if (firstDay === 6 && numDays >= 7) {
          // Add an extra week if the month starts on Saturday and has at least 7 days
          numWeeks++;
        }
      
        return numWeeks;
    }

    function incrementDateByOneDay(date, format = 'yyyy-MM-dd') {
        // Create a copy of the date object
        const newDate = new Date(date.getTime());
      
        // Add one day to the milliseconds since epoch
        newDate.setDate(newDate.getDate() + 1);
      
        // Format the date string based on the provided format
        const formattedDate = newDate.toLocaleDateString('en-US', { format });
      
        // Return the formatted date string
        return formattedDate;
    }

    function getStartandEndDateOfWeek(week)  {
        const startDate = new Date(new Date().getFullYear(), selected_month, week * 7);
        const endDate = new Date(startDate.getTime() + (7 * 24 * 60 * 60 * 1000) - 1); // Last day of the week (subtract 1 millisecond)

        return {
            'start_date': startDate.toLocaleDateString(),
            'end_date': endDate.toLocaleDateString(),
        }
    }

    useEffect(()=>{
        const fetchAllLogs = async () => {
            const url = `http://localhost:5001/api/v1/books_reading/${selected_book.id}/logs/all`;
            const response = await fetch(url);
            if (response.ok) {
                const logs = await response.json();
                console.log(logs);
                setAllReadings(logs);
            } else {
                if (response.status == 404) {
                    console.log(response.statusText);
                }
            }
        }

        fetchAllLogs();
    },[selected_book.id]);

    useEffect(()=>{
       setWeek(1); // reset the week to the start for every month change
       
    },[selected_month]);

    useEffect(()=> {
        
        const result = getStartandEndDateOfWeek(week);
        
        let dt = result.start_date;
        const datas = [];
        
        while (new Date(dt).getTime() <= new Date(result.end_date).getTime()) {
            let found = false;
            for (const index in all_readings)
            {
                const formatted_date = new Date(all_readings[index].date).toLocaleDateString()
                if (formatted_date == dt){
                    datas.push(all_readings[index]);
                    found = true;
                }
            }
            if (found == false) {
                datas.push({
                    date: dt,
                    total_pages: 0,
                })
            }
            dt = incrementDateByOneDay(new Date(dt), 'yyyy-MM-dd');
        }

        console.log(datas);
        setData(datas);
        
    }, [week, selected_month, all_readings])

    // Handle next week button click
  const handleNextWeek = () => {
    const numWeeksInMonth = getNumberOfWeeksInMonth(new Date().getFullYear(), selected_month);
    if (week < numWeeksInMonth - 2) {
      setWeek(week + 1);
      console.log(week);
    }
  };

  // Handle previous week button click
  const handlePrevWeek = () => {
    if (week > 0) {
      setWeek(week - 1);
      console.log(week);
    }
  };



    return (
        <div className="daily-progress-chart-container">
            
            <div className="daily-progress-chart-header">
                <MonthSelector setSelectedMonth={setSelectedMonth}/>
            </div>

            <div className="daily-progress-chart-body">
                <div className="prev" onClick={handlePrevWeek}>
                    <img src={prev_icon} alt="" />
                </div>
                <div className="daily-chart-content">
                    <MyBarChart data={datas} max_page={selected_book.book.pages} />
                </div>
                <div className="next" onClick={handleNextWeek}>
                    <img src={next_icon} alt="" /></div>
            </div>
            
        </div>
    )
}

MyBarChart.propTypes = {
    data: PropTypes.array,
    max_page: PropTypes.number,
}

DailyProgressChart.propTypes = {
    selected_book: PropTypes.object.isRequired,
}