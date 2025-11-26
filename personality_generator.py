#!/usr/bin/env python3
"""
Intelligent personality profile generator for Taylor Swift mashups.
Creates unique, thematic profiles based on song combinations.
"""

# Personality archetypes and themes for each song
SHOWGIRL_THEMES = {
    "The Fate of Ophelia": {"keywords": ["tragic", "dramatic", "fated", "intense"], "archetype": "Tragic"},
    "Elizabeth Taylor": {"keywords": ["glamorous", "passionate", "legendary", "bold"], "archetype": "Glamorous"},
    "Opalite": {"keywords": ["transformative", "mystical", "radiant", "evolving"], "archetype": "Mystical"},
    "Father Figure": {"keywords": ["protective", "stable", "nurturing", "grounded"], "archetype": "Guardian"},
    "Eldest Daughter": {"keywords": ["responsible", "caring", "reliable", "strong"], "archetype": "Caretaker"},
    "Ruin the Friendship": {"keywords": ["brave", "honest", "risk-taking", "authentic"], "archetype": "Brave"},
    "Actually Romantic": {"keywords": ["sincere", "optimistic", "genuine", "warm"], "archetype": "Sincere"},
    "Wish List": {"keywords": ["dreamy", "hopeful", "vulnerable", "aspirational"], "archetype": "Dreamer"},
    "Wood": {"keywords": ["natural", "grounded", "simple", "authentic"], "archetype": "Earthy"},
    "Cancelled!": {"keywords": ["defiant", "resilient", "strong-willed", "independent"], "archetype": "Defiant"},
    "Honey": {"keywords": ["sweet", "healing", "gentle", "comforting"], "archetype": "Healer"},
    "The Life of a Showgirl": {"keywords": ["performative", "charismatic", "complex", "theatrical"], "archetype": "Performer"}
}

POETS_THEMES = {
    "Fortnight": {"keywords": ["fleeting", "bittersweet", "temporary", "intense"], "modifier": "Fleeting"},
    "The Tortured Poets Department": {"keywords": ["artistic", "deep", "creative", "introspective"], "modifier": "Tortured"},
    "My Boy Only Breaks His Favorite Toys": {"keywords": ["self-destructive", "complex", "tragic", "aware"], "modifier": "Complex"},
    "Down Bad": {"keywords": ["vulnerable", "overwhelmed", "raw", "emotional"], "modifier": "Vulnerable"},
    "So Long, London": {"keywords": ["nostalgic", "accepting", "graceful", "moving-on"], "modifier": "Nostalgic"},
    "But Daddy I Love Him": {"keywords": ["rebellious", "defiant", "passionate", "independent"], "modifier": "Rebellious"},
    "Fresh Out the Slammer": {"keywords": ["liberated", "free", "wild", "exhilarated"], "modifier": "Liberated"},
    "Florida!!!": {"keywords": ["escapist", "chaotic", "adventurous", "reinventing"], "modifier": "Escapist"},
    "Guilty as Sin?": {"keywords": ["tempted", "questioning", "provocative", "conflicted"], "modifier": "Tempted"},
    "Who's Afraid of Little Old Me?": {"keywords": ["powerful", "assertive", "fierce", "unapologetic"], "modifier": "Fierce"},
    "I Can Fix Him (No Really I Can)": {"keywords": ["hopeful", "determined", "savior", "optimistic"], "modifier": "Hopeful"},
    "Loml": {"keywords": ["mourning", "deep", "lost", "reflective"], "modifier": "Mourning"},
    "I Can Do It with a Broken Heart": {"keywords": ["resilient", "strong", "performing", "enduring"], "modifier": "Resilient"},
    "The Smallest Man Who Ever Lived": {"keywords": ["outgrowing", "disappointed", "evolved", "clear-sighted"], "modifier": "Evolved"},
    "The Alchemy": {"keywords": ["transformative", "magical", "creative", "synergistic"], "modifier": "Alchemical"},
    "Clara Bow": {"keywords": ["iconic", "aware", "cyclical", "observant"], "modifier": "Iconic"},
    "The Black Dog": {"keywords": ["shadowed", "struggling", "honest", "coping"], "modifier": "Shadowed"},
    "Imgonnagetyouback": {"keywords": ["strategic", "determined", "plotting", "confident"], "modifier": "Strategic"},
    "The Albatross": {"keywords": ["burdened", "literary", "carrying", "marked"], "modifier": "Burdened"},
    "Chloe or Sam or Sophia or Marcus": {"keywords": ["insecure", "questioning", "seeking", "uncertain"], "modifier": "Seeking"},
    "How Did It End?": {"keywords": ["analytical", "retrospective", "understanding", "processing"], "modifier": "Analytical"},
    "So High School": {"keywords": ["youthful", "passionate", "nostalgic", "intense"], "modifier": "Youthful"},
    "I Hate It Here": {"keywords": ["escapist", "imaginative", "dissatisfied", "creative"], "modifier": "Imaginative"},
    "Thank You Aimee": {"keywords": ["grateful", "strong", "transformed", "wise"], "modifier": "Grateful"},
    "I Look in People's Windows": {"keywords": ["longing", "observant", "yearning", "distant"], "modifier": "Longing"},
    "The Prophecy": {"keywords": ["mystical", "questioning", "fated", "seeking"], "modifier": "Prophetic"},
    "Cassandra": {"keywords": ["truth-telling", "unheard", "frustrated", "prescient"], "modifier": "Prophetic"},
    "Peter": {"keywords": ["innocent", "choosing", "growing", "tender"], "modifier": "Tender"},
    "The Bolter": {"keywords": ["fleeing", "afraid", "running", "protective"], "modifier": "Fleeing"},
    "Robin": {"keywords": ["protective", "gentle", "nurturing", "fierce"], "modifier": "Protective"},
    "The Manuscript": {"keywords": ["reflective", "authoring", "perspective", "wise"], "modifier": "Reflective"}
}

def create_personality_title(showgirl_song, poets_song):
    """Generate a unique personality title from song combination."""
    sg_theme = SHOWGIRL_THEMES[showgirl_song]
    p_theme = POETS_THEMES[poets_song]
    
    archetype = sg_theme["archetype"]
    modifier = p_theme["modifier"]
    
    return f"The {modifier} {archetype}"

def create_traits(showgirl_song, poets_song):
    """Generate personality traits based on song themes."""
    sg_keywords = SHOWGIRL_THEMES[showgirl_song]["keywords"]
    p_keywords = POETS_THEMES[poets_song]["keywords"]
    
    # Combine keywords to create unique traits
    traits = [
        f"{p_keywords[0].capitalize()} yet {sg_keywords[0]}",
        f"Naturally {sg_keywords[1]} with a {p_keywords[1]} edge",
        f"Balances {sg_keywords[2]} tendencies with {p_keywords[2]} awareness",
        f"Embodies both {p_keywords[3]} and {sg_keywords[3]} qualities"
    ]
    
    return traits

def create_strengths(showgirl_song, poets_song):
    """Generate strengths based on positive aspects of both songs."""
    sg_keywords = SHOWGIRL_THEMES[showgirl_song]["keywords"]
    p_keywords = POETS_THEMES[poets_song]["keywords"]
    
    strengths = [
        f"Ability to be {sg_keywords[0]} while remaining {p_keywords[0]}",
        f"Natural {sg_keywords[1]} that inspires others",
        f"Deep capacity for {p_keywords[2]} connection"
    ]
    
    return strengths

def create_challenges(showgirl_song, poets_song):
    """Generate challenges based on potential conflicts in song themes."""
    sg_keywords = SHOWGIRL_THEMES[showgirl_song]["keywords"]
    p_keywords = POETS_THEMES[poets_song]["keywords"]
    
    challenges = [
        f"May struggle with being too {sg_keywords[0]}",
        f"Can become overwhelmed by {p_keywords[1]} feelings",
        f"Balancing {sg_keywords[2]} nature with {p_keywords[3]} reality"
    ]
    
    return challenges

def create_summary(showgirl_song, poets_song, title):
    """Generate a horoscope-like summary."""
    sg_theme = SHOWGIRL_THEMES[showgirl_song]
    p_theme = POETS_THEMES[poets_song]
    
    summary = (
        f"You embody the essence of {showgirl_song.lower()} meeting {poets_song.lower()}, "
        f"creating a unique blend of {sg_theme['keywords'][0]} and {p_theme['keywords'][0]} energy. "
        f"Your {sg_theme['keywords'][1]} nature is tempered by your {p_theme['keywords'][1]} awareness, "
        f"making you someone who understands both the light and shadow of human experience. "
        f"You were born to embrace your {sg_theme['keywords'][2]} spirit while honoring your {p_theme['keywords'][2]} truth."
    )
    
    return summary

def generate_profile(showgirl_song, poets_song):
    """Generate complete personality profile."""
    title = create_personality_title(showgirl_song, poets_song)
    traits = create_traits(showgirl_song, poets_song)
    strengths = create_strengths(showgirl_song, poets_song)
    challenges = create_challenges(showgirl_song, poets_song)
    summary = create_summary(showgirl_song, poets_song, title)
    
    return {
        "title": title,
        "traits": traits,
        "strengths": strengths,
        "challenges": challenges,
        "summary": summary
    }

if __name__ == "__main__":
    # Test with a few combinations
    test_combos = [
        ("The Fate of Ophelia", "Fortnight"),
        ("Actually Romantic", "The Alchemy"),
        ("The Life of a Showgirl", "I Look in People's Windows")
    ]
    
    for sg, p in test_combos:
        profile = generate_profile(sg, p)
        print(f"\n{sg} + {p}")
        print(f"Title: {profile['title']}")
        print(f"Summary: {profile['summary']}")

