""" This program calculates the distance between two near cities """

def sqrt(n):
    """ i'll use square root at the end on the  pythagorean theorem """
    epsilon = 0.0001
    b = 2

    p = (b + n/b)/2
    while abs(n - p**2) > epsilon:
        b = p
        p = (b + n/b)/2

    return p

def convert_latitude(lat):
    
    degrees = 0
    minutes = 0
    seconds = 0
    
    south = False
    """this will ensure that if they're on opposite hemispheres then
    their respectives latitudes and longitudes will
    not be subtracted, but added """

    assert len(lat) < 10 and len(lat) > 7, "Invalid input"

    if lat[0] == "-":
        south = True
        
    
    if south == False:
        degrees = float(lat[:2])
        minutes = float(lat[3:5])
        seconds = float(lat[6:])
        minutes += seconds/60
        degrees += minutes/60
        
    else:
        degrees = float(lat[:3])
        minutes = float(lat[4:6])
        minutes = float(lat[7:])
        
        minutes += seconds/60
        degrees -= minutes/60

    alpha = (abs(degrees) * 3.14159265359)/180
    latitude = alpha * 6371
    
    return latitude

def convert_longitude(long):

    degrees = 0
    minutes = 0
    seconds = 0
    
    stop = 0
    west = False

    if long[0] == "-":
        west = True
    
    for i in range(len(long)):
        
        if long[i] == " ":
            degrees = float(long[:i])
            stop = i + 1
            
            break

    for i in range(stop, len(long)):
        
        if long[i] == " ":
            minutes = float(long[stop:i])
            stop = i + 1
            
            seconds = float(long[stop:])
            break
    
    

    if west == False:
        minutes += seconds/60
        degrees += minutes/60

    else:
        minutes += seconds/60
        degrees -= minutes/60

    alpha = (abs(degrees) * 3.14159265359)/180
    longitude = alpha * 6371

    return longitude
    


class localization:
    def __init__(self, latitude, longitude):
        
        self.latitude = convert_latitude(latitude)
        self.longitude = convert_longitude(longitude)
    

    def __add__(self, other):
        distance_x = abs(self.latitude - other.latitude)
        distance_y = abs(self.longitude - other.longitude)
        """ the difference between their latitudes """
        
        distance = distance_x**2 + distance_y**2
        distance = sqrt(distance)

        return ("the distance is of {} km".format(round(distance, 4)))



sao_paulo = localization("-23 32 56", "-46 38 20")
rio_de_janeiro = localization("-22 54 13", "-43 12 35")
    
distance = sao_paulo + rio_de_janeiro
print("Between Sao Paulo and Rio de Janeiro", distance)


