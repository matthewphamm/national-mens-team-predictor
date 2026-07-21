from data_prep import load_data, DATA_PATH
from elo import expected_score, update_ratings, STARTING_RATING
from predict import predict_match

SCORING_START_YEAR = 1950

def get_actual_result(home_score: int, away_score: int) -> str:
    if home_score > away_score:
        return "home_win"
    elif home_score < away_score:
        return "away_win"
    else:
        return "draw"


def run_backtest(df) -> None:
    ratings: dict[str, float] = {}
    correct = 0
    scored = 0

    for row in df.itertuples():
        rating_home = ratings.get(row.home_team, STARTING_RATING)
        rating_away = ratings.get(row.away_team, STARTING_RATING)

        # TODO: only run the "predict and score" steps if row.date.year >= SCORING_START_YEAR
        #   1. call predict_match(rating_home, rating_away, row.neutral)
        #   2. figure out actual_result as one of "home_win"/"draw"/"away_win"
        #      from row.home_score and row.away_score
        #      (hint: you've written similar comparison logic before, in actual_score)
        #   3. predicted_result = the outcome with the highest probability
        #      (hint: max(result, key=result.get), same as validate.py)
        #   4. increment `scored`, and increment `correct` if predicted_result == actual_result

        if (row.date.year >= SCORING_START_YEAR):
            result = predict_match(rating_home, rating_away, row.neutral)
            predicted_result = max(result, key=result.get)
            actual_result = get_actual_result(row.home_score, row.away_score)

            scored += 1
            if predicted_result == actual_result:
                correct += 1

        # This part ALWAYS runs, regardless of scoring window --
        # ratings must keep updating on every match, warm-up or not:
        new_rating_home, new_rating_away = update_ratings(
            rating_home, rating_away,
            row.home_score, row.away_score,
            row.neutral
        )
        ratings[row.home_team] = new_rating_home
        ratings[row.away_team] = new_rating_away

    print(f"Matches scored (from {SCORING_START_YEAR} onward): {scored}")
    print(f"Correct top-pick predictions: {correct}")
    print(f"Accuracy: {correct/scored:.1%}")


if __name__ == "__main__":
    df = load_data(DATA_PATH)
    run_backtest(df)