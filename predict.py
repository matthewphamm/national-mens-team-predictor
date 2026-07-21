from elo import expected_score, build_ratings, HOME_ADVANTAGE
from data_prep import load_data, DATA_PATH

# Tunable constants for draw probability 
DRAW_MAX = 0.34             # highest possible draw probability, for two evenly matched teams
DRAW_MIN = 0.05             # lowest possible draw probability, for very mismatched teams
DRAW_SENSITIVITY = 0.0015   # how fast draw probability shrinks as rating gap grows

def estimate_draw_probability(rating_diff: float) -> float:
    rating_diff = abs(rating_diff)

    draw_prob = DRAW_MAX - DRAW_SENSITIVITY * rating_diff

    results = max(DRAW_MIN, min(DRAW_MAX, draw_prob))
    return results

def predict_match(rating_home: float, rating_away: float,
                  is_neutral: bool) -> dict[str, float]:
    if is_neutral is True:
        effective_rating_home = rating_home
    else:
        effective_rating_home = rating_home + HOME_ADVANTAGE
    
    expected_home = expected_score(effective_rating_home, rating_away)

    rating_diff = effective_rating_home - rating_away

    draw_prob = estimate_draw_probability(rating_diff)

    prob_home_win = expected_home - 0.5 * draw_prob
    prob_away_win = 1 - prob_home_win - draw_prob
    
    results = {
        "Home_win": prob_home_win,
        "Draw": draw_prob,
        "Away_win": prob_away_win
    }

    return results

if __name__ == "__main__":
    # Implement a user interface where it asks the user what two teams

    df = load_data(DATA_PATH)
    ratings = build_ratings(df)

    while True:
        team_a = input("Enter a National Team: ")
        team_b = input("Enter a Different National Team: ")

        if not (team_a and team_b):
            print("Please Enter Valid Teams.")
        else:
            formatted_input_a = team_a[0].upper() + team_a[1:].lower()
            formatted_input_b = team_b[0].upper() + team_b[1:].lower()
            break

    rating_a = ratings.get(formatted_input_a)
    rating_b = ratings.get(formatted_input_b)

    print(f"{formatted_input_a} rating: {rating_a:.1f}")
    print(f"{formatted_input_b} rating: {rating_b:.1f}")

    # Simulate a neutral-venue matchup (e.g. a World Cup game)
    result = predict_match(rating_a, rating_b, is_neutral=True)

    print(f"\n{formatted_input_a} vs {formatted_input_b} (neutral venue):")
    print(f"  {formatted_input_a} win: {result['Home_win']:.1%}")
    print(f"  Draw:          {result['Draw']:.1%}")
    print(f"  {formatted_input_b} win: {result['Away_win']:.1%}")