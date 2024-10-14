#!/usr/bin/env python3

def hamming_dist(signal_1, signal_2):
    result = []

    # Check if either signal is empty
    if not signal_1["times"] or not signal_1["data"] or not signal_2:
        return "Empty signal on at least one of the sensors"

    # Check if the lengths of times, data, and signal_2 are equal
    if len(signal_1["times"]) != len(signal_1["data"]) or len(signal_1["data"]) != len(signal_2):
        return "Empty signal on at least one of the sensors"
    
    # Iterate through the data
    for i in range(len(signal_1["data"])):
        counter = 0
        if len(signal_1["data"][i]) != len(signal_2[i]):
            return "Sensor defect detected"
        # Calculate Hamming distance
        for k in range(len(signal_2[i])):
            if signal_1["data"][i][k] != signal_2[i][k]:
                counter += 1
        if counter != 0:
            result.append((signal_1["data"][i], signal_2[i], counter))
    
    return result

# Example signals
signal_sensor_1 = {"times": [0, 1, 2], "data": ["00110101", "01010101", "10001110"]}
signal_sensor_2 = ("00110101", "01010101", "10001110")
print(hamming_dist(signal_sensor_1, signal_sensor_2))