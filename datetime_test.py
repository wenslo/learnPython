import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)

print(dt)
print(dt.timestamp())
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a,%b %d %H %M'))
now = datetime.now()
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(hours=19, days=2))
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
print('------------------------------------------------------------------------------------------------')
print(re.match(r'^(\w{3})(\+|-\d{1,2})(\:)(\d{1,2})', 'UTC-09:00'))
print(re.match(r'^(\w{3})((\+|-)\d{1,2})(\:)(\d{1,2})', 'UTC+7:00'))


def to_timestamp(dt_str, tz_str):
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    regular = re.match(r'^(\w{3})((\+|-)\d{1,2})(\:)(\d{1,2})', tz_str)
    hours = float(regular.group(2))
    tz_info = timezone(timedelta(hours=hours))
    time = time.replace(tzinfo=tz_info)
    result = time.astimezone(timezone(timedelta(hours=hours)))
    print(result.timestamp())
    return result.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
