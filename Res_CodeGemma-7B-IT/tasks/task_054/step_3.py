from datetime import datetime
from pytz import utc

utc_now = datetime.now(utc)
print(utc_now.isoformat())
```
execution trace:
stdout:
2026-05-31T03:39:40.570241+00:00


stderr:


return code: 0