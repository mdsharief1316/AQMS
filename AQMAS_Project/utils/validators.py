from datetime import datetime


def validate_timestamp(timestamp):
    try:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
        return True
    except:
        return False


def validate_pollutant(value):
    return value >= 0
