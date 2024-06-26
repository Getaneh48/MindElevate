import { useEffect} from 'react';
import './monthselector.scss';
import PropTypes from 'prop-types';
export default function MonthSelector({setSelectedMonth}){
    const current_month = new Date().getMonth();
    const months = [
      'January', 'February', 'March', 'April',
      'May', 'June', 'July', 'August',
      'September', 'October', 'November', 'December'
    ];

    useEffect(()=> {
        setSelectedMonth(current_month);
    },[current_month, setSelectedMonth])
  
    return (
      <select className="month-selector" onChange={(e)=>setSelectedMonth(e.currentTarget.value)}>
        {months.map((month, index) => {
            return (
                
                    index == current_month ? (
                        <option key={index} value={index} selected="selected">{month}</option>
                    ): (
                        <option key={index} value={index}>{month}</option>
                    )
                
            )
            
          
        })}
      </select>
    );
  }

  MonthSelector.propTypes = {
    setSelectedMonth: PropTypes.number,
  }
  