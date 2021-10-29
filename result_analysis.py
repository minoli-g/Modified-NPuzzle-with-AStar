import statistics
import numpy as np
import math

def paired_t_test(results):

    #results should be a long array containing 2-arrays
    #first element- misplaced, second - manhattan

    n = len(results)

    differences = list(map(lambda x: x[0]-x[1],results))

    mean_diff = statistics.mean(differences)

    standard_deviation = statistics.pstdev(differences)

    standard_error_of_mean_diff = standard_deviation / math.sqrt(n)

    t_value = mean_diff / standard_error_of_mean_diff

    print("Mean of differences: %.3f" % mean_diff)
    print("Standard Deviation: %.3f" % standard_deviation)
    print("Standard Error of Mean Difference: %.3f" % standard_error_of_mean_diff)
    print("T-value: %.3f" % t_value)




results = [[54, 54],
 [73, 49],
 [237, 122],
 [6, 6],
 [25, 18],
 [136, 77],
 [1658, 109],
 [2580, 864],
 [272, 60],
 [84, 24],
 [12, 12],
 [292, 48],
 [125, 40],
 [45, 23],
 [277, 85],
 [1087, 243],
 [12, 9],
 [1823, 221],
 [4571, 491],
 [496, 62],
 [32, 32],
 [42, 30],
 [3702, 731],
 [344, 124],
 [20, 20],
 [928, 99],
 [69, 44],
 [36, 36],
 [21, 21],
 [12, 12],
 [71, 53],
 [226, 80],
 [55, 45],
 [3, 3],
 [10, 10],
 [415, 147],
 [14, 14],
 [15, 15],
 [12, 12],
 [37, 14],
 [24, 24],
 [28, 16],
 [30, 30],
 [178, 42],
 [40, 40],
 [42, 24],
 [10, 10],
 [1388, 387],
 [88, 78],
 [198, 91],
 [54, 16],
 [134, 84],
 [16, 16],
 [50, 45],
 [496, 151],
 [65, 24],
 [66, 30],
 [21, 21],
 [98, 93],
 [24, 24],
 [40, 28],
 [1034, 144],
 [40, 40],
 [24, 24],
 [31, 24],
 [35, 35],
 [59, 35],
 [24, 24],
 [8, 8],
 [227, 142],
 [243, 140],
 [8, 8],
 [15, 15],
 [191, 116],
 [198, 77],
 [30, 30],
 [1961, 231],
 [161, 91],
 [3228, 300],
 [282, 129],
 [18, 18],
 [45, 45],
 [1227, 75],
 [66, 50],
 [30, 30],
 [30, 27],
 [30, 30],
 [9, 9],
 [136, 75],
 [679, 219],
 [445, 138],
 [28, 28],
 [2943, 1076],
 [29593, 3932],
 [30, 30],
 [54, 54],
 [369, 67],
 [21, 21],
 [128, 77],
 [52, 42],
 [65, 65],
 [45, 45],
 [28, 28],
 [24, 24],
 [21, 21],
 [40, 40],
 [18, 18],
 [18, 16],
 [74, 38],
 [49, 49],
 [60, 60],
 [356, 152]]

paired_t_test(results)
