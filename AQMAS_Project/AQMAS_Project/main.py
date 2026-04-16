from services.aq_service import (
    add_record,
    view_records,
    get_records_as_dict,
    set_records_from_dict,
    show_alert
)
from storage.file_handler import (
    save_to_csv,
    load_from_csv,
    save_to_json,
    load_from_json
)
from analysis.stats import trend_analysis
from visual.charts import generate_chart


def menu():
    print("\n========== AQMAS MENU ==========")
    print("1. Add Pollutant Record")
    print("2. View Records")
    print("3. Save Data to CSV")
    print("4. Load Data from CSV")
    print("5. Save Data to JSON")
    print("6. Load Data from JSON")
    print("7. Trend Analysis")
    print("8. Generate AQI Chart")
    print("9. Show Alerts")
    print("10. Exit")


while True:
    menu()

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Enter only numbers!")
        continue

    if choice == 1:
        add_record()

    elif choice == 2:
        view_records()

    elif choice == 3:
        save_to_csv(get_records_as_dict())

    elif choice == 4:
        data = load_from_csv()
        set_records_from_dict(data)

    elif choice == 5:
        save_to_json(get_records_as_dict())

    elif choice == 6:
        data = load_from_json()
        set_records_from_dict(data)

    elif choice == 7:
        trend_analysis(get_records_as_dict())

    elif choice == 8:
        generate_chart(get_records_as_dict())

    elif choice == 9:
        show_alert()

    elif choice == 10:
        print("Exiting AQMAS... Thank You!")
        break

    else:
        print("Invalid Choice! Try again.")
