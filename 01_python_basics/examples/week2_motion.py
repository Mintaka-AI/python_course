"""Week 2 practice: speed, time, and distance."""

distance_m = 240
time_s = 12
speed_m_s = distance_m / time_s

new_time_s = 15
new_distance_m = speed_m_s * new_time_s

print(f"Speed: {speed_m_s:.1f} m/s")
print(f"Distance in {new_time_s} s: {new_distance_m:.1f} m")
