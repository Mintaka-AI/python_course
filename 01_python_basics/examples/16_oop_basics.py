"""Lesson 16: basic classes, inheritance, composition, and properties."""

import math


class Location:
    def __init__(self, room):
        self.room = room


class Sensor:
    def __init__(self, sensor_id, offset_c=0.0):
        self.sensor_id = sensor_id
        self.offset_c = offset_c

    def calibrate(self, raw_c):
        return raw_c + self.offset_c


class LocatedSensor(Sensor):
    def __init__(self, sensor_id, location, offset_c=0.0):
        super().__init__(sensor_id, offset_c)
        self.location = location


class Tank:
    def __init__(self, capacity_l, current_l):
        if not math.isfinite(capacity_l) or capacity_l <= 0:
            raise ValueError("Tank capacity must be a finite number greater than zero.")
        if not math.isfinite(current_l) or not 0 <= current_l <= capacity_l:
            raise ValueError("Tank current volume must be finite and within its capacity.")
        self.capacity_l = capacity_l
        self.current_l = current_l

    @property
    def fill_percent(self):
        return self.current_l / self.capacity_l * 100


sensor = LocatedSensor("B-02", Location("Lab 3"), offset_c=0.2)
tank = Tank(200, 50)

print(f"{sensor.sensor_id} in {sensor.location.room}: {sensor.calibrate(20.0):.1f} °C")
print(f"Tank fill: {tank.fill_percent:.0f}%")
