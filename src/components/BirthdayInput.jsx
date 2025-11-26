import { useState } from 'react';
import './BirthdayInput.css';

const BirthdayInput = ({ onSubmit }) => {
  const [month, setMonth] = useState('');
  const [day, setDay] = useState('');

  const months = [
    { value: 1, label: 'January' },
    { value: 2, label: 'February' },
    { value: 3, label: 'March' },
    { value: 4, label: 'April' },
    { value: 5, label: 'May' },
    { value: 6, label: 'June' },
    { value: 7, label: 'July' },
    { value: 8, label: 'August' },
    { value: 9, label: 'September' },
    { value: 10, label: 'October' },
    { value: 11, label: 'November' },
    { value: 12, label: 'December' }
  ];

  const getDaysInMonth = (monthValue) => {
    if (!monthValue) return 31;
    // February has 29 days (accounting for leap years)
    if (monthValue === 2) return 29;
    // April, June, September, November have 30 days
    if ([4, 6, 9, 11].includes(monthValue)) return 30;
    // All other months have 31 days
    return 31;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (month && day) {
      onSubmit(parseInt(month), parseInt(day));
    }
  };

  const maxDays = getDaysInMonth(parseInt(month));
  const days = Array.from({ length: maxDays }, (_, i) => i + 1);

  return (
    <div className="birthday-input">
      <h1 className="title">✨ Your Taylor Swift Birthday Mashup ✨</h1>
      <p className="subtitle">Discover your unique song combination and personality profile</p>
      
      <form onSubmit={handleSubmit} className="birthday-form">
        <div className="input-group">
          <label htmlFor="month">Birth Month</label>
          <select
            id="month"
            value={month}
            onChange={(e) => {
              setMonth(e.target.value);
              // Reset day if it's now invalid for the new month
              if (day > getDaysInMonth(parseInt(e.target.value))) {
                setDay('');
              }
            }}
            required
          >
            <option value="">Select Month</option>
            {months.map(m => (
              <option key={m.value} value={m.value}>{m.label}</option>
            ))}
          </select>
        </div>

        <div className="input-group">
          <label htmlFor="day">Birth Day</label>
          <select
            id="day"
            value={day}
            onChange={(e) => setDay(e.target.value)}
            required
            disabled={!month}
          >
            <option value="">Select Day</option>
            {days.map(d => (
              <option key={d} value={d}>{d}</option>
            ))}
          </select>
        </div>

        <button type="submit" className="submit-btn" disabled={!month || !day}>
          Find My Mashup 🎵
        </button>
      </form>
    </div>
  );
};

export default BirthdayInput;

