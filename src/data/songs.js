// The Life of a Showgirl - Month mapping (1-12)
export const showgirlSongs = [
  { id: 1, title: "The Fate of Ophelia", duration: "3:46" },
  { id: 2, title: "Elizabeth Taylor", duration: "3:28" },
  { id: 3, title: "Opalite", duration: "3:55" },
  { id: 4, title: "Father Figure", duration: "3:32" },
  { id: 5, title: "Eldest Daughter", duration: "4:06" },
  { id: 6, title: "Ruin the Friendship", duration: "3:40" },
  { id: 7, title: "Actually Romantic", duration: "2:43" },
  { id: 8, title: "Wish List", duration: "3:27" },
  { id: 9, title: "Wood", duration: "2:30" },
  { id: 10, title: "Cancelled!", duration: "3:31" },
  { id: 11, title: "Honey", duration: "3:01" },
  { id: 12, title: "The Life of a Showgirl", duration: "4:01", featuring: "Sabrina Carpenter" }
];

// The Tortured Poets Department - Day mapping (1-31)
export const poetsSongs = [
  { id: 1, title: "Fortnight", duration: "3:48", featuring: "Post Malone" },
  { id: 2, title: "The Tortured Poets Department", duration: "4:53" },
  { id: 3, title: "My Boy Only Breaks His Favorite Toys", duration: "3:23" },
  { id: 4, title: "Down Bad", duration: "4:21" },
  { id: 5, title: "So Long, London", duration: "4:22" },
  { id: 6, title: "But Daddy I Love Him", duration: "5:40" },
  { id: 7, title: "Fresh Out the Slammer", duration: "3:30" },
  { id: 8, title: "Florida!!!", duration: "3:35", featuring: "Florence and the Machine" },
  { id: 9, title: "Guilty as Sin?", duration: "4:14" },
  { id: 10, title: "Who's Afraid of Little Old Me?", duration: "5:34" },
  { id: 11, title: "I Can Fix Him (No Really I Can)", duration: "2:36" },
  { id: 12, title: "Loml", duration: "4:37" },
  { id: 13, title: "I Can Do It with a Broken Heart", duration: "3:38" },
  { id: 14, title: "The Smallest Man Who Ever Lived", duration: "4:05" },
  { id: 15, title: "The Alchemy", duration: "3:16" },
  { id: 16, title: "Clara Bow", duration: "3:36" },
  { id: 17, title: "The Black Dog", duration: "3:58" },
  { id: 18, title: "Imgonnagetyouback", duration: "3:42" },
  { id: 19, title: "The Albatross", duration: "3:03" },
  { id: 20, title: "Chloe or Sam or Sophia or Marcus", duration: "3:33" },
  { id: 21, title: "How Did It End?", duration: "3:58" },
  { id: 22, title: "So High School", duration: "3:48" },
  { id: 23, title: "I Hate It Here", duration: "4:03" },
  { id: 24, title: "Thank You Aimee", duration: "4:23" },
  { id: 25, title: "I Look in People's Windows", duration: "2:11" },
  { id: 26, title: "The Prophecy", duration: "4:09" },
  { id: 27, title: "Cassandra", duration: "4:00" },
  { id: 28, title: "Peter", duration: "4:43" },
  { id: 29, title: "The Bolter", duration: "3:58" },
  { id: 30, title: "Robin", duration: "4:00" },
  { id: 31, title: "The Manuscript", duration: "3:44" }
];

// Helper function to get song by month
export const getSongByMonth = (month) => {
  return showgirlSongs[month - 1];
};

// Helper function to get song by day
export const getSongByDay = (day) => {
  return poetsSongs[day - 1];
};

// Helper function to generate mashup key
export const getMashupKey = (month, day) => {
  return `${month}-${day}`;
};

