import datetime
from astral import sun

today = datetime.date.today()
location = "New York"

sunrise = sun(location, today).sunrise
sunset = sun(location, today).sunset

print("Today's sunrise in New York is:", sunrise)
print("Today's sunset in New York is:", sunset)