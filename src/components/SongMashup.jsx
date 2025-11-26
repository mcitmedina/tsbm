import './SongMashup.css';

const SongMashup = ({ showgirlSong, poetsSong, mashupData }) => {
  return (
    <div className="song-mashup">
      <h2 className="mashup-title">Your Birthday Mashup</h2>
      
      <div className="songs-container">
        <div className="song-card showgirl">
          <div className="album-label">The Life of a Showgirl</div>
          <h3 className="song-title">{showgirlSong.title}</h3>
          {showgirlSong.featuring && (
            <p className="featuring">feat. {showgirlSong.featuring}</p>
          )}
          <p className="duration">{showgirlSong.duration}</p>
          
          {mashupData && (
            <div className="song-meaning">
              <h4>Song Meaning</h4>
              <p>{mashupData.songMeanings.showgirl}</p>
            </div>
          )}
        </div>

        <div className="mashup-symbol">+</div>

        <div className="song-card poets">
          <div className="album-label">The Tortured Poets Department</div>
          <h3 className="song-title">{poetsSong.title}</h3>
          {poetsSong.featuring && (
            <p className="featuring">feat. {poetsSong.featuring}</p>
          )}
          <p className="duration">{poetsSong.duration}</p>
          
          {mashupData && (
            <div className="song-meaning">
              <h4>Song Meaning</h4>
              <p>{mashupData.songMeanings.poets}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SongMashup;

