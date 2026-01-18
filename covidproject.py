import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data():
    """
    Loads COVID-19 data with varied values
    for better visualization.
    """
    data = {
        "State": [
            "Maharashtra",
            "Kerala",
            "Karnataka",
            "Tamil Nadu",
            "Uttar Pradesh",
            "Delhi",
            "West Bengal"
        ],
        "Confirmed": [8200000, 7000000, 5200000, 4600000, 3500000, 2000000, 1800000],
        "Recovered": [7800000, 6500000, 4900000, 4200000, 3100000, 1750000, 1600000],
        "Deaths": [150500, 98000, 65000, 72000, 48000, 42000, 35000]
    }

    return pd.DataFrame(data)


def calculate_rates(df):
    """
    Calculates Recovery Rate and Fatality Rate
    """
    df["Recovery Rate (%)"] = (df["Recovered"] / df["Confirmed"]) * 100
    df["Fatality Rate (%)"] = (df["Deaths"] / df["Confirmed"]) * 100
    return df


def generate_bar_chart(df):
    """
    Generates a bar chart with value labels
    """
    os.makedirs("output", exist_ok=True)

    plt.figure(figsize=(11, 6))

    x = range(len(df["State"]))

    # Bars
    recovery_bars = plt.bar(
        x,
        df["Recovery Rate (%)"],
        width=0.4,
        label="Recovery Rate (%)",
        color="green"
    )

    fatality_bars = plt.bar(
        [i + 0.4 for i in x],
        df["Fatality Rate (%)"],
        width=0.4,
        label="Fatality Rate (%)",
        color="red"
    )

    # Add value labels on bars
    for bar in recovery_bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.3,
            f"{height:.1f}%",
            ha="center",
            fontsize=9
        )

    for bar in fatality_bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            f"{height:.2f}%",
            ha="center",
            fontsize=9
        )

    # Chart styling
    plt.title("COVID-19 Recovery vs Fatality Rates (India)", fontsize=14)
    plt.xlabel("State")
    plt.ylabel("Rate (%)")
    plt.xticks([i + 0.2 for i in x], df["State"], rotation=30)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
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
