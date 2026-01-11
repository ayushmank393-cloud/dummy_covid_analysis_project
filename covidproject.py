import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
   
   data = {
    "State": ["Maharashtra", "Kerala", "Karnataka", "Tamil Nadu", "Uttar Pradesh"],
    "Confirmed": [8200000, 7000000, 4350000, 3800000, 2500000],
    "Recovered": [8000000, 6850000, 4200000, 3700000, 2400000],
    "Deaths": [150500, 75000, 42000, 39500, 26000]
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

