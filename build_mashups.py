#!/usr/bin/env python3
import json

# Complete song lists
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

# Song meanings - Based on official sources and music journalism
SHOWGIRL_MEANINGS = {
    "The Fate of Ophelia": "References Shakespeare's Hamlet, depicting Swift as Ophelia pledging loyalty to an honorable Prince Hamlet. Swift credits her partner for saving her from Ophelia's tragic fate of madness and drowning, transforming a story of being driven mad by love into one of being rescued by it.",
    "Elizabeth Taylor": "Named after the legendary actress, this song contemplates the nature of romance and fame over an orchestral pop soundscape. It explores passionate love lived in the spotlight, channeling the glamour and complexity of Hollywood's golden age.",
    "Opalite": "A pop rock celebration of the happiness that comes from being with the right partner. Using the metaphor of this luminous stone, it explores joy, transformation, and the radiance of finding true love.",
    "Father Figure": "Interpolating George Michael's 1987 song, this track portrays Swift as the ringleader of her career, facing other strong, powerful men in the industry. It's about authority, power dynamics, and taking control of your own narrative.",
    "Eldest Daughter": "A minor-key piano ballad about insecurities and awareness of public perception, ultimately finding resolution in a happy relationship. It speaks to the burden of responsibility and the relief of finally being cared for.",
    "Ruin the Friendship": "A teen pop and '90s country-influenced song about regretting not pursuing a romance with a high school friend. It explores the what-ifs of missed romantic opportunities and the courage it takes to cross that line.",
    "Actually Romantic": "A pop-punk and guitar pop track interpreted as a response to being the subject of another artist's song. Swift finds herself flattered by another woman's obsession with her, celebrating genuine romance over cynicism.",
    "Wish List": "A power ballad with '80s synth-pop influences where Swift sings about wanting a peaceful domestic partnership over riches or recognition. It's about redefining success as love and contentment rather than fame.",
    "Wood": "A dance and funk-pop track using redwood tree imagery as a double entendre. It's playful and earthy, celebrating natural connection and physical attraction with wit and charm.",
    "Cancelled!": "Swift positions herself among fallen public figures over atmospheric stomping beats. A defiant anthem about surviving public ridicule and cancel culture, refusing to be diminished by criticism.",
    "Honey": "An R&B-influenced country pop and synth-pop ballad about the enjoyment of being with someone genuine. It celebrates authentic love free from passive-aggression or arrogance, sweet and healing like honey.",
    "The Life of a Showgirl": "Featuring Sabrina Carpenter, this mid-tempo pop ballad tells the story of Kitty, a Las Vegas showgirl navigating the challenges of show business. It's a character study exploring performance, ambition, and the price of success in entertainment."
}

POETS_MEANINGS = {
    "Fortnight": "A song about a torrid, short-lived and forbidden love affair between two former lovers who have moved on and married other people. Now neighbors, they make small talk while harboring resentment and longing. Themes include fatalism, lost dreams, and the lingering effects of a romance that lasted only two weeks but continues to ruin their lives.",
    "The Tortured Poets Department": "An exploration of the intense, dramatic relationship between two creative people who see themselves as tortured artists. Swift examines the self-awareness of knowing you're being overly dramatic while still feeling deeply, capturing the delusion and intensity of artistic romance.",
    "My Boy Only Breaks His Favorite Toys": "A song about self-destructive patterns in relationships, exploring how some people destroy what they love most. It examines the cycle of being someone's favorite but also being the one they hurt repeatedly.",
    "Down Bad": "About feeling completely devastated and undone by a relationship, using space and alien metaphors to describe being left behind. It captures the disorientation and loss of feeling abandoned after an intense connection.",
    "So Long, London": "A melancholic goodbye to a long-term relationship and the city where it took place. Swift reflects on trying to save a dying relationship, the exhaustion of that effort, and finally accepting it's time to leave.",
    "But Daddy I Love Him": "A defiant anthem about choosing your own path in love despite others' disapproval. Swift channels rebellious energy, refusing to let public opinion or authority figures dictate her romantic choices.",
    "Fresh Out the Slammer": "About the rush of freedom after ending a restrictive relationship and immediately running to someone new. It captures the reckless energy of newfound liberation and not wasting time before pursuing what you really want.",
    "Florida!!!": "Featuring Florence + The Machine, this song explores Florida as a place to escape, reinvent yourself, and hide from your past. It's about running away from consequences and seeking anonymity in chaos.",
    "Guilty as Sin?": "Explores the tension between fantasy and reality, questioning whether desiring someone while in another relationship constitutes betrayal. It examines the morality of thoughts versus actions and the guilt of emotional infidelity.",
    "Who's Afraid of Little Old Me?": "A fierce reclamation of power, challenging those who underestimated her or tried to make her small. Swift embraces being seen as dangerous or unhinged, refusing to be diminished by public perception.",
    "I Can Fix Him (No Really I Can)": "A self-aware examination of the savior complex in dating, where Swift acknowledges the futility of trying to change a bad boy while admitting she can't help but try anyway.",
    "Loml": "Short for 'love of my life,' this devastating ballad mourns a relationship that felt destined but ended. It explores the pain of losing what you thought was your forever person and the betrayal of that loss.",
    "I Can Do It with a Broken Heart": "About performing and functioning publicly while privately falling apart. Swift describes putting on a show during her Eras Tour while dealing with heartbreak, celebrating resilience through pain.",
    "The Smallest Man Who Ever Lived": "A scathing takedown of an ex who proved himself small through his actions. Swift expresses anger and disappointment at someone who didn't live up to expectations, calling out cowardice and pettiness.",
    "The Alchemy": "Using football metaphors, this song celebrates new love with Travis Kelce. It explores the chemistry and transformation that comes from finding the right person and winning at love.",
    "Clara Bow": "Compares Swift's fame to Old Hollywood star Clara Bow, examining the cyclical nature of female stardom. It reflects on being replaced by the next young thing and the fleeting nature of celebrity.",
    "The Black Dog": "About discovering an ex has moved on by seeing their location at a pub called The Black Dog. It explores the pain of being replaced and the torture of knowing too much about an ex's new life.",
    "Imgonnagetyouback": "A playful song with double meaning - getting someone back could mean revenge or reconciliation. Swift keeps the intention ambiguous, exploring the thin line between wanting someone back and wanting to get back at them.",
    "The Albatross": "Uses the metaphor of an albatross (a burden or curse) to explore being seen as bad luck or a destructive force in others' lives. It examines reputation and the weight of being blamed for others' downfalls.",
    "Chloe or Sam or Sophia or Marcus": "Explores the fear of being replaceable and interchangeable in a partner's life. Swift questions whether she was truly special or just another name in a long list of people.",
    "How Did It End?": "Examines the public curiosity and gossip surrounding a breakup, with Swift questioning how to explain the end of a relationship. It explores the invasive nature of public interest in private pain.",
    "So High School": "A joyful song about feeling young and giddy in love with Travis Kelce. It celebrates the excitement of new romance that makes you feel like a teenager again, complete with high school imagery.",
    "I Hate It Here": "About escapism and dissatisfaction with reality, using time travel fantasies to cope with present unhappiness. Swift explores retreating into imagination when the real world becomes too difficult.",
    "Thank You Aimee": "Widely interpreted as being about Kim Kardashian (with 'KIM' capitalized in the title), this song thanks a bully for making Swift stronger. It's about finding gratitude for adversity that shaped her resilience.",
    "I Look in People's Windows": "A haunting song about longing and searching for someone in crowds and windows. It captures the ache of missing someone and looking for them everywhere, unable to move on.",
    "The Prophecy": "A plea to fate or destiny, begging for a different outcome in love. Swift questions whether she's cursed to repeat patterns and asks for mercy from whatever force controls her romantic destiny.",
    "Cassandra": "References the Greek prophetess cursed to tell truths no one believes. Swift compares herself to Cassandra, having warned about situations or people but being ignored, only to be proven right later.",
    "Peter": "Uses Peter Pan imagery to explore a relationship with someone who won't grow up. It's about the sadness of loving someone who chooses to remain in Neverland while you have to move forward into adulthood.",
    "The Bolter": "Examines the pattern of running away from relationships when they get too real. Swift explores the fear of commitment and intimacy that causes some people to bolt before they can be hurt.",
    "Robin": "A tender song about protecting innocence and childhood, possibly addressing a younger person. It expresses the desire to shield someone from harsh realities and preserve their pure perspective.",
    "The Manuscript": "Reflects on looking back at a past relationship like reading an old manuscript. Swift examines how we revise and reinterpret our own stories with time and distance, finding new meaning in old chapters."
}

# Personality themes based on actual song meanings
SHOWGIRL_THEMES = {
    "The Fate of Ophelia": {"arch": "Rescued Romantic", "kw": ["loyal", "saved", "transformed", "devoted"]},
    "Elizabeth Taylor": {"arch": "Glamorous Icon", "kw": ["passionate", "legendary", "bold", "timeless"]},
    "Opalite": {"arch": "Radiant Dreamer", "kw": ["shimmering", "evolving", "hopeful", "luminous"]},
    "Father Figure": {"arch": "Steady Protector", "kw": ["nurturing", "reliable", "comforting", "grounded"]},
    "Eldest Daughter": {"arch": "Responsible Leader", "kw": ["dutiful", "strong", "selfless", "capable"]},
    "Ruin the Friendship": {"arch": "Bold Risk-Taker", "kw": ["honest", "brave", "authentic", "daring"]},
    "Actually Romantic": {"arch": "Genuine Believer", "kw": ["sincere", "optimistic", "warm", "trusting"]},
    "Wish List": {"arch": "Hopeful Visionary", "kw": ["aspirational", "vulnerable", "dreaming", "yearning"]},
    "Wood": {"arch": "Natural Soul", "kw": ["grounded", "simple", "authentic", "earthy"]},
    "Cancelled!": {"arch": "Defiant Survivor", "kw": ["resilient", "unbreakable", "independent", "strong-willed"]},
    "Honey": {"arch": "Sweet Healer", "kw": ["genuine", "gentle", "soothing", "authentic"]},
    "The Life of a Showgirl": {"arch": "Complex Performer", "kw": ["charismatic", "multifaceted", "theatrical", "captivating"]}
}

POETS_THEMES = {
    "Fortnight": {"mod": "Forbidden Longing", "kw": ["intense", "conflicted", "haunted", "passionate"]},
    "The Tortured Poets Department": {"mod": "Creative Intensity", "kw": ["artistic", "self-aware", "dramatic", "deep"]},
    "My Boy Only Breaks His Favorite Toys": {"mod": "Pattern Recognition", "kw": ["understanding", "cyclical", "aware", "accepting"]},
    "Down Bad": {"mod": "Devastated Vulnerability", "kw": ["overwhelmed", "lost", "raw", "disoriented"]},
    "So Long, London": {"mod": "Exhausted Acceptance", "kw": ["weary", "letting go", "reflective", "moving on"]},
    "But Daddy I Love Him": {"mod": "Rebellious Choice", "kw": ["defiant", "independent", "determined", "unapologetic"]},
    "Fresh Out the Slammer": {"mod": "Liberated Rush", "kw": ["free", "reckless", "exhilarated", "unleashed"]},
    "Florida!!!": {"mod": "Chaotic Escape", "kw": ["running", "reinventing", "hiding", "wild"]},
    "Guilty as Sin?": {"mod": "Moral Questioning", "kw": ["tempted", "conflicted", "desiring", "guilty"]},
    "Who's Afraid of Little Old Me?": {"mod": "Fierce Reclamation", "kw": ["powerful", "dangerous", "unapologetic", "commanding"]},
    "I Can Fix Him (No Really I Can)": {"mod": "Savior Complex", "kw": ["hopeful", "delusional", "trying", "persistent"]},
    "Loml": {"mod": "Devastating Loss", "kw": ["mourning", "betrayed", "heartbroken", "grieving"]},
    "I Can Do It with a Broken Heart": {"mod": "Performing Resilience", "kw": ["strong", "functioning", "hiding pain", "enduring"]},
    "The Smallest Man Who Ever Lived": {"mod": "Scathing Clarity", "kw": ["angry", "disappointed", "outgrowing", "seeing truth"]},
    "The Alchemy": {"mod": "Winning Chemistry", "kw": ["transformative", "joyful", "victorious", "magical"]},
    "Clara Bow": {"mod": "Cyclical Fame", "kw": ["aware", "replaceable", "observant", "fleeting"]},
    "The Black Dog": {"mod": "Painful Discovery", "kw": ["tortured", "replaced", "knowing too much", "haunted"]},
    "Imgonnagetyouback": {"mod": "Ambiguous Revenge", "kw": ["strategic", "playful", "determined", "plotting"]},
    "The Albatross": {"mod": "Cursed Reputation", "kw": ["burdened", "blamed", "marked", "weighted"]},
    "Chloe or Sam or Sophia or Marcus": {"mod": "Fear of Replacement", "kw": ["insecure", "questioning", "interchangeable", "anxious"]},
    "How Did It End?": {"mod": "Public Scrutiny", "kw": ["examined", "gossiped about", "explaining", "invaded"]},
    "So High School": {"mod": "Giddy Youth", "kw": ["excited", "playful", "young at heart", "joyful"]},
    "I Hate It Here": {"mod": "Escapist Fantasy", "kw": ["dissatisfied", "imaginative", "retreating", "coping"]},
    "Thank You Aimee": {"mod": "Grateful Strength", "kw": ["resilient", "transformed", "stronger", "victorious"]},
    "I Look in People's Windows": {"mod": "Searching Longing", "kw": ["yearning", "looking", "missing", "aching"]},
    "The Prophecy": {"mod": "Pleading Fate", "kw": ["begging", "questioning destiny", "hopeful", "desperate"]},
    "Cassandra": {"mod": "Unheard Truth", "kw": ["ignored", "vindicated", "frustrated", "prophetic"]},
    "Peter": {"mod": "Lost Innocence", "kw": ["tender", "growing up", "choosing maturity", "bittersweet"]},
    "The Bolter": {"mod": "Flight Response", "kw": ["running away", "afraid of intimacy", "escaping", "self-protective"]},
    "Robin": {"mod": "Protective Love", "kw": ["nurturing", "shielding", "gentle", "fierce"]},
    "The Manuscript": {"mod": "Rewritten Narrative", "kw": ["reflective", "reinterpreting", "authoring", "perspective"]},
}

def generate_profile(sg_song, p_song):
    """Generate personality profile for song combination."""
    sg = SHOWGIRL_THEMES[sg_song]
    p = POETS_THEMES[p_song]

    # Create a unique archetype title
    title = f"The {p['mod']} {sg['arch']}"

    # Generate traits that blend both song energies
    traits = [
        f"You carry the {sg['kw'][0]} energy of someone who embodies {sg_song}, while navigating the {p['kw'][0]} reality of {p_song}",
        f"Your {sg['kw'][1]} nature is constantly in dialogue with your {p['kw'][1]} tendencies",
        f"You possess a rare ability to be both {sg['kw'][2]} and {p['kw'][2]} simultaneously",
        f"Others see you as someone who is {sg['kw'][3]} yet deeply {p['kw'][3]}"
    ]

    # Generate strengths based on the positive aspects of both songs
    strengths = [
        f"Your {sg['kw'][0]} approach to life allows you to remain {p['kw'][0]} even in difficult situations",
        f"You have a {sg['kw'][1]} quality that helps you navigate {p['kw'][1]} experiences with grace",
        f"Your capacity to be {sg['kw'][2]} while staying {p['kw'][2]} makes you a powerful force in relationships",
        f"You inspire others through your unique blend of {sg['kw'][3]} wisdom and {p['kw'][3]} authenticity"
    ]

    # Generate challenges that reflect the tension between the two songs
    challenges = [
        f"You may struggle to balance your {sg['kw'][0]} instincts with your {p['kw'][0]} reality",
        f"Your {sg['kw'][1]} nature can sometimes clash with your {p['kw'][1]} experiences",
        f"Learning when to embrace your {sg['kw'][2]} side versus your {p['kw'][2]} side is an ongoing journey",
        f"You might feel torn between being {sg['kw'][3]} and honoring your {p['kw'][3]} truth"
    ]

    # Generate a horoscope-like summary
    summary = (
        f"Born under the cosmic alignment of '{sg_song}' and '{p_song}', you are {title}. "
        f"Your soul carries the essence of someone who is both {sg['kw'][0]} and {p['kw'][0]}, "
        f"creating a complex inner world that few truly understand. "
        f"You were meant to walk the path between {sg['kw'][1]} dreams and {p['kw'][1]} realities, "
        f"teaching others that it's possible to be {sg['kw'][2]} while remaining {p['kw'][2]}. "
        f"Your life's work is to embrace your {sg['kw'][3]} nature without losing your {p['kw'][3]} core. "
        f"In love, you seek someone who appreciates both your light and shadow. "
        f"In work, you thrive when you can express your full complexity. "
        f"Your greatest gift to the world is showing that contradictions can coexist beautifully."
    )

    return {
        "title": title,
        "traits": traits,
        "strengths": strengths,
        "challenges": challenges,
        "summary": summary
    }

# Generate all mashups
mashups = {}
for month in range(1, 13):
    for day in range(1, 32):
        key = f"{month}-{day}"
        sg_song = SHOWGIRL_SONGS[month - 1]
        p_song = POETS_SONGS[day - 1]

        mashups[key] = {
            "month": month,
            "day": day,
            "showgirlSong": sg_song,
            "poetsSong": p_song,
            "songMeanings": {
                "showgirl": SHOWGIRL_MEANINGS[sg_song],
                "poets": POETS_MEANINGS[p_song]
            },
            "personalityProfile": generate_profile(sg_song, p_song)
        }

print(f"Generated {len(mashups)} mashup combinations!")

# Save to JSON
output_file = "src/data/songMashups.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(mashups, f, indent=2, ensure_ascii=False)

print(f"✅ Saved to {output_file}")
print(f"✅ File size: {len(json.dumps(mashups))} characters")
print("✅ Generation complete!")

