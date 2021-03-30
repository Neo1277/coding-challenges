import math
def phoneCall(min1, min2_10, min11, s):
    result = s - min1
    min1_time = 0
    time_min2_10 = 0
    time_min11 = 0
    if result < 0:
        result1 = 0
        return result1
    else:
        min1_time = 1
        
        result_test = result
        for cont in range(0, 10):
            time_min2_10 = cont
            result = result_test - (min2_10 * cont)
            if result < 0:
                cont -= 1
                time_min2_10 = cont
                result = result_test - (min2_10 * cont)
                break
        print(time_min2_10)
        if result >= 1:
            time_min11 = result / min11
            result = result - time_min11
            if result < 0:
                result = result + time_min11
                time_min11 = 0
        print(time_min11)
        result1 = math.floor(min1_time + time_min2_10 + time_min11)
    return result1

print(phoneCall(1, 2, 1, 6))