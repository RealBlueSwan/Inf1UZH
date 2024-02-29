#!/usr/bin/env python3

# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    #predef
    hamminglist = []
    
    # is the dataset the same lenght?
    if len(signal_2) == 0  or len(signal_1["data"]) == 0 or len(signal_1["data"]) != len(signal_2) or len(signal_1["times"]) != len(signal_1["data"]):
        raise Warning( "Empty signal on at least one of the sensors")
    
    #are the two compared data equal lenght? if not raise Warning
    for n in range(len(signal_1["data"])):
        #print(signal_1["data"][n], signal_2[n])
        
        if len(signal_1["data"][n]) != len(signal_2[n]):
            raise Warning("Sensor defect detected")

        # test if the two are the same and if not add them to the list huminglist
        if signal_1["data"][n] != signal_2[n]:
            #insert defcalc and 
            hamminglist.append(humming_calc(signal_1["data"][n], signal_2[n]))
            # hamminglist.append((signal_1["data"][n], signal_2[n]))

    return hamminglist

def humming_calc(str1, str2):
    counter = 0
    #make a counter for every letter that is different
    for n in range(len(str1)):
        if str1[n] != str2[n]:
            counter = counter + 1
    return (str1, str2, counter)
    

    


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
