import pandas as pd

def recommend_crop(temp, humidity, soil_type):
    df = pd.read_csv("crop_data.csv")
    matched = df[
        (df["temperature"] <= temp + 2) &
        (df["temperature"] >= temp - 2) &
        (df["humidity"] <= humidity + 10) &
        (df["humidity"] >= humidity - 10) &
        (df["soil_type"].str.lower() == soil_type.lower())
    ]
    if not matched.empty:
        return matched["crop"].values[0]
    return "No suitable crop found"
