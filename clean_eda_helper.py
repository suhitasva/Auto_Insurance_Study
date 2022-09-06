import pandas as pd
import numpy as np

def na_replace(df):

    # Replacing age_category NA values with most common values:

    df['age_category'].replace(np.nan,df['age_category'].mode()[0],inplace = True)

    # Replacing credit_score and traffic_index NA values:

    df["traffic_index"] = df.groupby("area")["traffic_index"]\
    .apply(lambda x: x.replace(np.nan,x.median()))

    df["credit_score"] = df.groupby("age_category")["credit_score"]\
    .apply(lambda x: x.replace(np.nan,x.median()))