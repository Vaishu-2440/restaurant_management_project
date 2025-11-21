from datetime import datetime, time
def is_restaurant_open() :
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    if current_day < 5 :
        opening_time = time(9, 0)
        closing_time = time(22, 0)
    
    else :
        opening_time = time(10, 0)
        closing_time = time(23, 0)
        
    return opeming_time  <= current_time <= closing_time