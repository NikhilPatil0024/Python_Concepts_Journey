"""datetime, timezone-aware now."""
from datetime import datetime, timezone, timedelta
now_utc = datetime.now(timezone.utc)
ist = timezone(timedelta(hours=5, minutes=30))
print(now_utc.astimezone(ist).strftime("%Y-%m-%d %H:%M:%S %Z"))
