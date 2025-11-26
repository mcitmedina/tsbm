#!/usr/bin/env python3
"""
Generate all 372 Taylor Swift birthday mashup combinations
with personality profiles and song meanings.
"""

import json

# Song lists
SHOWGIRL_SONGS = [
    "The Fate of Ophelia", "Elizabeth Taylor", "Opalite", "Father Figure",
    "Eldest Daughter", "Ruin the Friendship", "Actually Romantic", "Wish List",
    "Wood", "Cancelled!", "Honey", "The Life of a Showgirl"
]

POETS_SONGS = [
    "Fortnight", "The Tortured Poets Department", "My Boy Only Breaks His Favorite Toys",
    "Down Bad", "So Long, London", "But Daddy I Love Him", "Fresh Out the Slammer",
    "Florida!!!", "Guilty as Sin?", "Who's Afraid of Little Old Me?",
    "I Can Fix Him (No Really I Can)", "Loml", "I Can Do It with a Broken Heart",
    "The Smallest Man Who Ever Lived", "The Alchemy", "Clara Bow", "The Black Dog",
    "Imgonnagetyouback", "The Albatross", "Chloe or Sam or Sophia or Marcus",
    "How Did It End?", "So High School", "I Hate It Here", "Thank You Aimee",
    "I Look in People's Windows", "The Prophecy", "Cassandra", "Peter",
    "The Bolter", "Robin", "The Manuscript"
]

# Song meanings
SHOWGIRL_MEANINGS = {
    "The Fate of Ophelia": "A haunting exploration of tragic beauty and doomed romance, channeling Shakespearean tragedy with themes of madness, love, and inevitable fate. It speaks to those who feel destined for dramatic, all-consuming emotional experiences.",
    "Elizabeth Taylor": "A glamorous meditation on Hollywood romance, legendary love affairs, and the price of living life in the spotlight. This song celebrates passionate, unapologetic love while acknowledging its complexities and the strength required to love boldly.",
    "Opalite": "A shimmering reflection on transformation and inner light, using the metaphor of this mystical stone to explore personal growth and finding beauty in change. It's about discovering your own radiance even when the world tries to dim your shine.",
    "Father Figure": "An exploration of seeking guidance, protection, and stability in relationships, examining the complex dynamics of looking for authority and comfort in romantic connections. It delves into the psychology of dependency and care.",
    "Eldest Daughter": "A powerful anthem about responsibility, caretaking, and the weight of expectations placed on those who always put others first. It honors the strength and sacrifice of being the reliable one while acknowledging the burden it creates.",
    "Ruin the Friendship": "A bold declaration about crossing the line from friendship to romance, exploring the risk and reward of admitting deeper feelings. It's about choosing honesty over safety and being brave enough to want more.",
    "Actually Romantic": "A celebration of genuine, uncomplicated romance that defies cynicism and embraces sincerity. This song is an ode to believing in love without irony, finding magic in simple gestures and authentic connection.",
    "Wish List": "A dreamy exploration of desires, hopes, and the things we long for in love and life. It captures the vulnerability of admitting what you truly want and the courage it takes to ask for it.",
    "Wood": "An earthy, grounded meditation on natural connection, simplicity, and finding strength in organic, unpretentious love. It's about authenticity, roots, and the beauty of something real and unpolished.",
    "Cancelled!": "A defiant response to public judgment and cancel culture, celebrating resilience and refusing to be defined by others' opinions. It's about reclaiming your narrative and standing strong in your truth.",
    "Honey": "A sweet, golden exploration of warmth, comfort, and the healing power of gentle love. This song captures the soothing nature of genuine affection and the way tenderness can mend what's broken.",
    "The Life of a Showgirl": "A theatrical exploration of performance, identity, and the price of living in the spotlight. It examines the duality of public persona versus private self, celebrating glamour while acknowledging the loneliness of always being on stage."
}

POETS_MEANINGS = {
    "Fortnight": "A bittersweet reflection on a fleeting romance that burned bright but brief, exploring the tension between temporary connection and lasting impact. It captures the melancholy of knowing something beautiful is destined to end yet choosing to experience it anyway.",
    "The Tortured Poets Department": "An introspective journey into the minds of artists who transform pain into beauty, examining the relationship between suffering and creativity. It's a love letter to those who feel too deeply and think too much.",
    "My Boy Only Breaks His Favorite Toys": "A poignant examination of self-destructive patterns in love, exploring why we sometimes destroy what we cherish most. It speaks to the tragedy of loving someone who can't help but hurt what they hold dear.",
    "Down Bad": "A raw confession of being completely undone by love or heartbreak, capturing that feeling of being knocked off your feet emotionally. It's about vulnerability, losing control, and the overwhelming nature of intense feeling.",
    "So Long, London": "A melancholic farewell to a chapter of life, a place, or a relationship, filled with nostalgia and the bittersweet acceptance of moving on. It honors what was while embracing what must be, finding grace in goodbye.",
    "But Daddy I Love Him": "A rebellious declaration of choosing love despite disapproval, channeling the spirit of defying authority for matters of the heart. It's about standing up for your choices and refusing to let others dictate your happiness.",
    "Fresh Out the Slammer": "A liberation anthem about breaking free from constraints, whether literal or metaphorical, and the exhilaration of newfound freedom. It captures that first breath of independence and the wild joy of escape.",
    "Florida!!!": "A wild exploration of escape, chaos, and the allure of starting over in a place where nobody knows your name. It's about running toward something or away from everything, seeking reinvention and anonymity.",
    "Guilty as Sin?": "A provocative examination of desire, temptation, and the fine line between thought and action. It questions whether wanting something forbidden is itself a transgression, exploring the morality of fantasy.",
    "Who's Afraid of Little Old Me?": "A powerful reclamation of personal power, challenging those who underestimated or tried to diminish you. It's a battle cry of self-assertion, refusing to be small, and showing your teeth to those who thought you were harmless.",
    "I Can Fix Him (No Really I Can)": "A self-aware exploration of the savior complex in relationships, acknowledging the futile hope of changing someone while being unable to resist trying. It's both critique and confession, humor and heartbreak.",
    "Loml": "A devastating reflection on a love that felt like 'the one,' examining how the greatest loves can become the deepest losses. It's about mourning what could have been and accepting what never will be.",
    "I Can Do It with a Broken Heart": "An anthem of resilience and performance, about showing up and functioning even when you're falling apart inside. It celebrates strength through vulnerability and the courage to keep going.",
    "The Smallest Man Who Ever Lived": "A scathing takedown of someone who proved themselves small through their actions, exploring disappointment and the power of seeing someone's true character. It's about outgrowing who hurt you and recognizing their limitations.",
    "The Alchemy": "An exploration of transformation and chemistry, examining how the right connection can change everything. It speaks to the magical process of two people creating something entirely new together through their combination.",
    "Clara Bow": "A meditation on fame, beauty standards, and the cyclical nature of stardom, comparing modern celebrity to Old Hollywood glamour. It examines the price of being an icon and the fleeting nature of public adoration.",
    "The Black Dog": "A haunting exploration of depression, dark moods, and the shadows that follow us, using Churchill's metaphor to examine mental health struggles with poetic honesty. It's about living with darkness and finding ways to cope.",
    "Imgonnagetyouback": "A determined declaration of winning back what was lost, whether love, power, or self-respect. It's about strategic resilience, refusing to accept defeat, and plotting your comeback with confidence.",
    "The Albatross": "A literary exploration of burden and bad luck, using Coleridge's metaphor to examine how past mistakes or associations can weigh us down. It's about carrying what you can't escape and the curse of reputation.",
    "Chloe or Sam or Sophia or Marcus": "A meditation on interchangeability and the fear of being replaceable in love, questioning whether you're truly special or just another name in a list. It explores insecurity, identity, and the need to matter.",
    "How Did It End?": "A retrospective examination of a relationship's demise, piecing together the moments that led to the end. It's about seeking understanding in aftermath and the human need to make sense of loss.",
    "So High School": "A nostalgic dive into young love and the intensity of teenage emotions, capturing both the sweetness and drama of first relationships. It celebrates youthful passion and the way early love shapes us.",
    "I Hate It Here": "A confession of dissatisfaction and escapism, about mentally checking out when reality becomes unbearable. It's about the fantasy worlds we create to survive and the refuge of imagination.",
    "Thank You Aimee": "A complex expression of gratitude toward someone who hurt you, acknowledging how adversity shaped you into who you are. It's about finding strength through struggle and thanking your enemies for making you stronger.",
    "I Look in People's Windows": "A poignant meditation on longing and observation, capturing the ache of being outside looking in. It explores nostalgia, yearning for connection, and the bittersweet act of witnessing others' lives from a distance.",
    "The Prophecy": "A mystical exploration of fate, destiny, and the question of whether our futures are written or ours to create. It examines the tension between control and surrender, asking the universe for answers.",
    "Cassandra": "A powerful piece about speaking truth that no one believes, channeling the Greek prophetess cursed to be ignored. It's about the frustration of seeing what others refuse to acknowledge and being proven right too late.",
    "Peter": "A tender exploration of lost innocence and the boy who never grew up, examining the choice between eternal youth and mature love. It's about what we sacrifice to grow and the bittersweet nature of leaving childhood behind.",
    "The Bolter": "An examination of the flight response in relationships, about those who run when things get real. It explores the pattern of leaving before you can be left and the fear of intimacy that drives escape.",
    "Robin": "A gentle, protective meditation on innocence, childhood, and the desire to shield the vulnerable from harsh realities. It's about preserving what's pure and the fierce love that wants to keep someone safe.",
    "The Manuscript": "A reflective piece about looking back on your own story, examining your life as if it were written by someone else. It's about perspective, authorship, rewriting your narrative, and finding meaning in your chapters."
}

def generate_mashups():
    """Generate all 372 mashup combinations."""
    mashups = {}
    
    for month in range(1, 13):
        for day in range(1, 32):
            key = f"{month}-{day}"
            showgirl_song = SHOWGIRL_SONGS[month - 1]
            poets_song = POETS_SONGS[day - 1]
            
            mashups[key] = create_mashup_entry(month, day, showgirl_song, poets_song)
            
    return mashups

def create_mashup_entry(month, day, showgirl_song, poets_song):
    """Create a single mashup entry with personality profile."""
    # Get song meanings
    showgirl_meaning = SHOWGIRL_MEANINGS[showgirl_song]
    poets_meaning = POETS_MEANINGS[poets_song]
    
    # Generate personality profile based on song combination
    profile = generate_personality_profile(showgirl_song, poets_song)
    
    return {
        "month": month,
        "day": day,
        "showgirlSong": showgirl_song,
        "poetsSong": poets_song,
        "songMeanings": {
            "showgirl": showgirl_meaning,
            "poets": poets_meaning
        },
        "personalityProfile": profile
    }

def generate_personality_profile(showgirl_song, poets_song):
    """Generate a unique personality profile for each song combination."""
    # This will be populated with specific combinations
    # For now, creating a template that will be filled in
    return {
        "title": "The Placeholder",
        "traits": ["Trait 1", "Trait 2", "Trait 3", "Trait 4"],
        "strengths": ["Strength 1", "Strength 2", "Strength 3"],
        "challenges": ["Challenge 1", "Challenge 2", "Challenge 3"],
        "summary": "Summary placeholder"
    }

if __name__ == "__main__":
    print("Generating all 372 Taylor Swift birthday mashups...")
    mashups = generate_mashups()
    
    output_file = "src/data/songMashups.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mashups, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {len(mashups)} mashup combinations")
    print(f"✅ Saved to {output_file}")

