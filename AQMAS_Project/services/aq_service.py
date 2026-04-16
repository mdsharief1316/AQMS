from models.pollutant import PollutantRecord
from utils.validators import validate_timestamp, validate_pollutant

records = []


def calculate_aqi(pm25, pm10, no2, so2, co, o3):
    return max(pm25, pm10, no2, so2, co, o3)


def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Very Poor"
    else:
        return "Severe"


def add_record():
    timestamp = input("Enter Timestamp (YYYY-MM-DD HH:MM): ")

    if not validate_timestamp(timestamp):
        print("Invalid timestamp format!")
        return

    try:
        pm25 = float(input("Enter PM2.5 value: "))
        pm10 = float(input("Enter PM10 value: "))
        no2 = float(input("Enter NO2 value: "))
        so2 = float(input("Enter SO2 value: "))
        co = float(input("Enter CO value: "))
        o3 = float(input("Enter O3 value: "))
    except:
        print("Invalid input! Enter only numbers.")
        return

    if (not validate_pollutant(pm25) or not validate_pollutant(pm10) or
            not validate_pollutant(no2) or not validate_pollutant(so2) or
            not validate_pollutant(co) or not validate_pollutant(o3)):
        print("Pollutant values cannot be negative!")
        return

    aqi = calculate_aqi(pm25, pm10, no2, so2, co, o3)
    category = get_aqi_category(aqi)

    record_obj = PollutantRecord(timestamp, pm25, pm10, no2, so2, co, o3, aqi, category)
    records.append(record_obj)

    print("Record Added Successfully!")
    print("AQI =", aqi, "| Category =", category)


def view_records():
    if len(records) == 0:
        print("No records available!")
        return

    print("\n------ AIR QUALITY RECORDS ------")
    print("Timestamp\t\tPM2.5\tPM10\tNO2\tSO2\tCO\tO3\tAQI\tCategory")
    print("-" * 100)

    for r in records:
        print(f"{r.timestamp}\t{r.pm25}\t{r.pm10}\t{r.no2}\t{r.so2}\t{r.co}\t{r.o3}\t{r.aqi}\t{r.category}")


def get_records_as_dict():
    return [r.to_dict() for r in records]


def set_records_from_dict(data_list):
    global records
    records = []

    for d in data_list:
        record_obj = PollutantRecord(
            d["timestamp"], d["pm25"], d["pm10"], d["no2"],
            d["so2"], d["co"], d["o3"], d["aqi"], d["category"]
        )
        records.append(record_obj)


def show_alert():
    if len(records) == 0:
        print("No records available!")
        return

    last_record = records[-1]

    print("\n------ ALERT SYSTEM ------")
    print("Latest AQI =", last_record.aqi)
    print("Category   =", last_record.category)

    if last_record.aqi > 200:
        print("WARNING: Air Quality is Unhealthy! Avoid Outdoor Activities.")
    else:
        print("Air Quality is Safe.")
