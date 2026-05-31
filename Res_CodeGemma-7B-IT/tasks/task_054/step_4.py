from datetime import datetime
from pytz import utc

utc_now = datetime.now(utc)
print(utc_now.strftime("%Y-%m-%dT%H:%M:%S.%f%z"))
```
execution trace:
stdout:
2026-05-31T03:43:27.555448+00:00


stderr:


return code: 0