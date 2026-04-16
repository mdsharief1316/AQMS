import numpy as np


def trend_analysis(records_dict):
    if len(records_dict) == 0:
        print("No records available for analysis!")
        return

    pm25_list = np.array([r["pm25"] for r in records_dict])
    pm10_list = np.array([r["pm10"] for r in records_dict])
    no2_list = np.array([r["no2"] for r in records_dict])
    so2_list = np.array([r["so2"] for r in records_dict])
    co_list = np.array([r["co"] for r in records_dict])
    o3_list = np.array([r["o3"] for r in records_dict])
    aqi_list = np.array([r["aqi"] for r in records_dict])

    print("\n------ TREND ANALYSIS REPORT ------")
    print("Average PM2.5 =", np.mean(pm25_list))
    print("Average PM10  =", np.mean(pm10_list))
    print("Average NO2   =", np.mean(no2_list))
    print("Average SO2   =", np.mean(so2_list))
    print("Average CO    =", np.mean(co_list))
    print("Average O3    =", np.mean(o3_list))
    print("Maximum AQI   =", np.max(aqi_list))
    print("Minimum AQI   =", np.min(aqi_list))
