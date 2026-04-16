import json
import os


def save_to_csv(records_dict, filename="data/air_quality.csv"):
    if len(records_dict) == 0:
        print("No records to save!")
        return

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        file.write("timestamp,pm25,pm10,no2,so2,co,o3,aqi,category\n")

        for r in records_dict:
            file.write(f"{r['timestamp']},{r['pm25']},{r['pm10']},{r['no2']},{r['so2']},{r['co']},{r['o3']},{r['aqi']},{r['category']}\n")

    print("Data saved successfully in", filename)


def load_from_csv(filename="data/air_quality.csv"):
    records = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for line in lines[1:]:
            data = line.strip().split(",")

            record = {
                "timestamp": data[0],
                "pm25": float(data[1]),
                "pm10": float(data[2]),
                "no2": float(data[3]),
                "so2": float(data[4]),
                "co": float(data[5]),
                "o3": float(data[6]),
                "aqi": float(data[7]),
                "category": data[8]
            }

            records.append(record)

        print("Data loaded successfully from", filename)

    except FileNotFoundError:
        print("CSV file not found!")
    except:
        print("Error while reading CSV file!")

    return records


def save_to_json(records_dict, filename="data/air_quality.json"):
    if len(records_dict) == 0:
        print("No records to save!")
        return

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        json.dump(records_dict, file, indent=4)

    print("Data saved successfully in", filename)


def load_from_json(filename="data/air_quality.json"):
    try:
        with open(filename, "r") as file:
            records = json.load(file)

        print("Data loaded successfully from", filename)
        return records

    except FileNotFoundError:
        print("JSON file not found!")
        return []
    except:
        print("Error in loading JSON file!")
        return []
