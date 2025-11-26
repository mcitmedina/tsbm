import { useState } from 'react'
import './App.css'
import BirthdayInput from './components/BirthdayInput'
import SongMashup from './components/SongMashup'
import PersonalityProfile from './components/PersonalityProfile'
import { getSongByMonth, getSongByDay, getMashupKey } from './data/songs'
import songMashupsData from './data/songMashups.json'

function App() {
  const [selectedBirthday, setSelectedBirthday] = useState(null);
  const [showResults, setShowResults] = useState(false);

  const handleBirthdaySubmit = (month, day) => {
    const showgirlSong = getSongByMonth(month);
    const poetsSong = getSongByDay(day);
    const mashupKey = getMashupKey(month, day);
    const mashupData = songMashupsData[mashupKey];

    setSelectedBirthday({
      month,
      day,
      showgirlSong,
      poetsSong,
      mashupData
    });
    setShowResults(true);
  };

  const handleReset = () => {
    setShowResults(false);
    setSelectedBirthday(null);
  };

  return (
    <div className="app">
      {!showResults ? (
        <BirthdayInput onSubmit={handleBirthdaySubmit} />
      ) : (
        <div className="results">
          <button onClick={handleReset} className="back-btn">
            ← Try Another Birthday
          </button>

          <SongMashup
            showgirlSong={selectedBirthday.showgirlSong}
            poetsSong={selectedBirthday.poetsSong}
            mashupData={selectedBirthday.mashupData}
          />

          {selectedBirthday.mashupData && (
            <PersonalityProfile profile={selectedBirthday.mashupData.personalityProfile} />
          )}
        </div>
      )}
    </div>
  )
}

export default App
