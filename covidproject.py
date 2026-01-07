# COVID Data Analysis Project
# Libraries used: Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    """
    Creates and returns a DataFrame with dummy COVID-19 data
    for 5 Indian states.
    """
    data = {
        "State": ["Maharashtra", "Kerala", "Karnataka", "Tamil Nadu", "Uttar Pradesh"],
        "Confirmed": [8000000, 6800000, 4100000, 3600000, 2100000],
        "Recovered": [7800000, 6600000, 3950000, 3500000, 2050000],
        "Deaths": [148000, 72000, 40500, 38000, 23500]
    }

    df = pd.DataFrame(data)
    return df

def calculate_rates(df):
    """
    Calculates Recovery Rate and Fatality Rate
    and adds them as new columns.
    """
    df["Recovery Rate (%)"] = (df["Recovered"] / df["Confirmed"]) * 100
    df["Fatality Rate (%)"] = (df["Deaths"] / df["Confirmed"]) * 100
    return df

def generate_bar_chart(df):
    """
    Generates a bar chart for Recovery and Fatality Rates
    and saves it inside the output folder.
    """

    os.makedirs("output", exist_ok=True)


    plt.figure(figsize=(10, 6))

    # Plot bar charts
    plt.bar(df["State"], df["Recovery Rate (%)"], label="Recovery Rate", color="green")
    plt.bar(df["State"], df["Fatality Rate (%)"], label="Fatality Rate", color="red")

    # Chart styling
    plt.title("COVID-19 Recovery and Fatality Rates (India)", fontsize=14)
    plt.xlabel("State")
    plt.ylabel("Rate (%)")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()


    plt.savefig("output/covid_rates.png")
    plt.show()

def main():
    df = load_data()
    df = calculate_rates(df)
    generate_bar_chart(df)


    print("\nFinal COVID-19 Data Analysis:\n")
    print(df)
if __name__ == "__main__":
    main()
