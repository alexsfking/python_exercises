class Time:
    seconds_in_minute = 60
    minutes_in_hour = 60

    def __init__(self,hour:int,minute:int,second:int):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
        
    def __add__(self, other:'Time') -> 'Time':
        second = self.second + other.second
        minute, second = divmod(second, Time.seconds_in_minute)
        minute += self.minute + other.minute
        hour, minute = divmod(minute, Time.minutes_in_hour)
        hour += self.hour + other.hour
        return Time(hour,minute,second)
    
    def __sub__(self, other:'Time') -> 'Time':
        flag = None
        second = (self.second + 60*self.minute + 3600*self.hour) - (other.second + 60*other.minute + 3600*other.hour)
        if(second < 0):
            second = abs(second)
            flag = True
        minute, second = divmod(second, Time.seconds_in_minute)
        hour, minute = divmod(minute, Time.minutes_in_hour)
        if flag:
            return Time(-hour,minute,second)
        return Time(hour,minute,second)
    
    def __mul__(self, multiplier:int) -> 'Time':
        second = self.second + 60*self.minute + 3600*self.hour
        second *= multiplier
        flag = None
        if(second < 0):
            second = abs(second)
            flag = True
        minute, second = divmod(second, Time.seconds_in_minute)
        hour, minute = divmod(minute, Time.minutes_in_hour)
        if flag:
            return Time(-hour,minute,second)
        return Time(hour,minute,second)

time_a = Time(11,40,23)
time_b = Time(1,40,59) 
print(time_a)
print(time_b)
print(time_a + time_b)
print(time_a - time_b)
print(time_b - time_a)
print(time_a * 2)
print((time_a + time_b) * 2)
print((time_b - time_a) * 2)
print((time_a - time_b) * 2)
print((time_a - time_b) * -2)