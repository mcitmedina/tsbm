import './PersonalityProfile.css';

const PersonalityProfile = ({ profile }) => {
  if (!profile) {
    return null;
  }

  return (
    <div className="personality-profile">
      <h2 className="profile-title">{profile.title}</h2>
      
      <div className="profile-summary">
        <p>{profile.summary}</p>
      </div>

      <div className="profile-sections">
        <div className="profile-section">
          <h3>✨ Your Traits</h3>
          <ul>
            {profile.traits.map((trait, index) => (
              <li key={index}>{trait}</li>
            ))}
          </ul>
        </div>

        <div className="profile-section">
          <h3>💪 Your Strengths</h3>
          <ul>
            {profile.strengths.map((strength, index) => (
              <li key={index}>{strength}</li>
            ))}
          </ul>
        </div>

        <div className="profile-section">
          <h3>🌙 Your Challenges</h3>
          <ul>
            {profile.challenges.map((challenge, index) => (
              <li key={index}>{challenge}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default PersonalityProfile;

