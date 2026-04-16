# AQMS – Air Quality Monitoring System

## Project Overview

The **Air Quality Monitoring System (AQMS)** is a Python-based application developed to monitor, store, analyze, and visualize air pollution data.

This project demonstrates:

* Modular programming
* Data analysis
* File handling
* Data visualization

---

## Features

* Add and store air quality data records
* Validate pollutant inputs
* Calculate Air Quality Index (AQI)
* Store and retrieve data using CSV files
* Perform statistical analysis using NumPy
* Generate visual charts using Matplotlib
* Organized modular project architecture

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* CSV File Handling

---

## Project Structure

```
AQMAS_Project/
│
├── main.py                     # Entry point and menu control
│
├── models/
│   ├── __init__.py
│   └── pollutant.py
│
├── services/
│   ├── __init__.py
│   └── aq_service.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
├── storage/
│   ├── __init__.py
│   └── file_handler.py
│
├── analysis/
│   ├── __init__.py
│   └── stats.py
│
├── visual/
│   ├── __init__.py
│   └── charts.py
│
└── data/
    └── air_quality.csv
```

---

## How to Run the Project

1. Clone the repository
2. Navigate to the project directory
3. Run the program

```
python main.py
```

---

## Future Improvements

* Integration with real-time air quality sensors
* Web dashboard for visualization
* Machine learning based AQI prediction

---

## Authors

* Mohammad Sharief
* Aakash
* Nazeer
* Yaswanth
