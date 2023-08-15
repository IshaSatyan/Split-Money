import collections
import math


def find_path(parms):
    print_bill = []
        
    # Get the maximum and minimum values in the `parms` dictionary.
    max_value = max(parms.values())
    min_value = min(parms.values())
    
    # If the maximum and minimum values are not equal, then find the path between them.
    if max_value != min_value:
        # Get the keys of the nodes with the maximum and minimum values.
        max_key = list(parms.keys())[list(parms.values()).index(max_value)]
        min_key = list(parms.keys())[list(parms.values()).index(min_value)]
        
        # Calculate the amount that the two nodes need to pay each other.
        result = max_value + min_value
        result = round(result, 1)
        if result >= 0:
            print(f"{min_key} needs to pay {max_key}: {round(math.fabs(min_value), 2)}")
            parms.pop(max_key)
            parms.pop(min_key)
            parms[max_key] = result
            parms[min_key] = 0
        else:
            print(f"{min_key} needs to pay {max_key}: {round(math.fabs(max_value), 2)}")
            parms.pop(max_key)
            parms.pop(min_key)
            parms[max_key] = 0
            parms[min_key] = result
        find_path(parms)


if __name__ == "__main__":
    parms = {
        "Lakshya": 120.0,
        "Mehul": -40.0,
        "Khush": -90.0,
        "Manish": 10.0,
    }
    find_path(parms)
