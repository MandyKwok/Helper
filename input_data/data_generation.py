import random
import datetime

def generate_N_random_date(N, start, end):
    """
    This function will return N random datetime objects between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    
    result = []
    for i in range(N):
        random_second = random.randrange(int_delta)
        datetime_object = datetime.datetime.date(start + datetime.timedelta(seconds = random_second))
        result.append(datetime_object)
        
    return result