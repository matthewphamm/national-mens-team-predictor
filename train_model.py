import pandas as pd
from sklearn.linear_model import PoissonRegressor # type: ignore
from data_prep import load_data, DATA_PATH
from train_data import build_training_df

def train_goal_models(training_df: pd.DataFrame) -> tuple[PoissonRegressor, PoissonRegressor]:
    pass

