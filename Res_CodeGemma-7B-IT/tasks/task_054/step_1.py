import datetime
import pytz

utc_now = datetime.datetime.now(pytz.utc)
print(utc_now)