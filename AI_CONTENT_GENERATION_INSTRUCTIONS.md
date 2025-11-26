# AI Content Generation Instructions

## Overview
This file contains instructions for generating the song mashup content for the Taylor Swift Birthday Mashup website.

## Task
Generate personality profiles and song meanings for all valid birthday combinations (month 1-12, day 1-31).

## File to Update
`src/data/songMashups.json`

## Data Structure
Each entry should follow this format:

```json
{
  "MONTH-DAY": {
    "month": MONTH_NUMBER,
    "day": DAY_NUMBER,
    "showgirlSong": "SONG_TITLE_FROM_SHOWGIRL_ALBUM",
    "poetsSong": "SONG_TITLE_FROM_POETS_ALBUM",
    "songMeanings": {
      "showgirl": "2-3 sentence summary of the song's themes, emotions, and meaning",
      "poets": "2-3 sentence summary of the song's themes, emotions, and meaning"
    },
    "personalityProfile": {
      "title": "Creative personality archetype name (e.g., 'The Tragic Romantic', 'The Fearless Dreamer')",
      "traits": [
        "Trait 1 based on song combination",
        "Trait 2 based on song combination",
        "Trait 3 based on song combination",
        "Trait 4 based on song combination"
      ],
      "strengths": [
        "Strength 1 derived from song themes",
        "Strength 2 derived from song themes",
        "Strength 3 derived from song themes"
      ],
      "challenges": [
        "Challenge 1 based on song themes",
        "Challenge 2 based on song themes",
        "Challenge 3 based on song themes"
      ],
      "summary": "A 3-4 sentence horoscope-like personality description that weaves together the themes of both songs into a cohesive personality profile. Should feel mystical and insightful like a horoscope reading."
    }
  }
}
```

## Song Mappings

### The Life of a Showgirl (Month 1-12)
1. "The Fate of Ophelia"
2. "Elizabeth Taylor"
3. "Opalite"
4. "Father Figure"
5. "Eldest Daughter"
6. "Ruin the Friendship"
7. "Actually Romantic"
8. "Wish List"
9. "Wood"
10. "Cancelled!"
11. "Honey"
12. "The Life of a Showgirl"

### The Tortured Poets Department (Day 1-31)
1. "Fortnight"
2. "The Tortured Poets Department"
3. "My Boy Only Breaks His Favorite Toys"
4. "Down Bad"
5. "So Long, London"
6. "But Daddy I Love Him"
7. "Fresh Out the Slammer"
8. "Florida!!!"
9. "Guilty as Sin?"
10. "Who's Afraid of Little Old Me?"
11. "I Can Fix Him (No Really I Can)"
12. "Loml"
13. "I Can Do It with a Broken Heart"
14. "The Smallest Man Who Ever Lived"
15. "The Alchemy"
16. "Clara Bow"
17. "The Black Dog"
18. "Imgonnagetyouback"
19. "The Albatross"
20. "Chloe or Sam or Sophia or Marcus"
21. "How Did It End?"
22. "So High School"
23. "I Hate It Here"
24. "Thank You Aimee"
25. "I Look in People's Windows"
26. "The Prophecy"
27. "Cassandra"
28. "Peter"
29. "The Bolter"
30. "Robin"
31. "The Manuscript"

## Important Notes

1. **Valid Combinations**: Not all day/month combinations are valid (e.g., February 30th doesn't exist). Generate entries for all mathematically possible combinations (12 months × 31 days = 372 entries), but the website will only display valid dates.

2. **Personality Profiles**: Should blend the themes of both songs creatively. Think about how the emotional journey of the Showgirl song (month) combines with the Poets song (day) to create a unique personality type.

3. **Tone**: Keep the tone mystical, insightful, and positive (like a horoscope). Even when songs have darker themes, frame personality traits constructively.

4. **Song Meanings**: Base these on the actual Taylor Swift songs if you have knowledge of them, or create thematically appropriate interpretations based on the song titles.

## Example Entry

See the placeholder entry at "1-1" in the current `songMashups.json` file for the structure.

## Validation
After generation, ensure:
- All 372 combinations (1-1 through 12-31) are present
- JSON is valid and properly formatted
- All required fields are present for each entry
- Song titles match exactly with the lists above

