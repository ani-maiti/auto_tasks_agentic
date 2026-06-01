import json

data = {"results":{"sunrise":"3:47:28 AM","sunset":"8:08:59 PM","solar_noon":"11:58:13 AM","day_length":"16:21:31","civil_twilight_begin":"3:04:19 AM","civil_twilight_end":"8:52:07 PM","nautical_twilight_begin":"1:57:43 AM","nautical_twilight_end":"9:58:43 PM","astronomical_twilight_begin":"12:00:01 AM","astronomical_twilight_end":"12:00:01 AM"},"status":"OK","tzid":"UTC"}
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"Sunrise: {sunrise}, Sunset: {sunset}")