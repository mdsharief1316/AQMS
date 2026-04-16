import matplotlib.pyplot as plt


def generate_chart(records_dict):
    if len(records_dict) == 0:
        print("No records available to plot!")
        return

    timestamps = [r["timestamp"] for r in records_dict]
    aqi_values = [r["aqi"] for r in records_dict]

    plt.plot(timestamps, aqi_values, marker="o")
    plt.xticks(rotation=45)
    plt.title("AQI Trend Chart")
    plt.xlabel("Timestamp")
    plt.ylabel("AQI Value")
    plt.grid(True)
    plt.show()
