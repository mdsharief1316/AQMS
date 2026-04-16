class PollutantRecord:
    def __init__(self, timestamp, pm25, pm10, no2, so2, co, o3, aqi, category):
        self.timestamp = timestamp
        self.pm25 = pm25
        self.pm10 = pm10
        self.no2 = no2
        self.so2 = so2
        self.co = co
        self.o3 = o3
        self.aqi = aqi
        self.category = category

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "pm25": self.pm25,
            "pm10": self.pm10,
            "no2": self.no2,
            "so2": self.so2,
            "co": self.co,
            "o3": self.o3,
            "aqi": self.aqi,
            "category": self.category
        }
