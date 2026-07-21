from data_prep import load_data, DATA_PATH
from elo import build_ratings
from predict import predict_match

TEST_MATCHES = [
    ("Argentina", "France", "draw", True),             # 2022 WC Final (3-3, Argentina won on penalties)
    ("Argentina", "Croatia", "home_win", True),        # 2022 WC Semifinal (3-0)
    ("France", "Morocco", "home_win", True),           # 2022 WC Semifinal (2-0)
    ("Morocco", "Spain", "draw", True),                # 2022 WC Round of 16 (0-0, Morocco won on penalties)
    ("Germany", "Japan", "away_win", True),            # 2022 WC Group Stage (1-2, major upset)
    ("Saudi Arabia", "Argentina", "home_win", True),   # 2022 WC Group Stage (2-1, huge upset)
    ("Brazil", "Croatia", "draw", True),               # 2022 WC Quarterfinal (1-1, Croatia won on penalties)
    ("Spain", "England", "away_win", True),            # Euro 2024 Final (1-2)
    ("England", "Netherlands", "home_win", True),      # Euro 2024 Semifinal (2-1)
    ("Argentina", "Colombia", "home_win", True),       # Copa America 2024 Final (1-0)
]