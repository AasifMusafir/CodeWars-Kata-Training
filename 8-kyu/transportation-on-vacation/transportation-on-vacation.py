def rental_car_cost(d):
    if d>=1 and d<3:
        d=(d*40)
    elif d>=3 and d<7:
        d=(d*40)-20
    
    else:
        d=(d*40)-50
    
    return d
    # your code