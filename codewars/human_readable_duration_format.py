'''
Your task in order to complete this Kata is to write a function which formats a
duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns
"now". Otherwise, the duration is expressed as a combination of years, days,
hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules The resulting expression is made of components like 4 seconds, 1
year, etc. In general, a positive integer and one of the valid units of time,
separated by a space. The unit of time is used in plural if the integer is
greater than 1.

The components are separated by a comma and a space (", "). Except the last
component, which is separated by " and ", just like it would be written in
English.

A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1
minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function
should not return 61 seconds, but 1 minute and 1 second instead. Formally, the
duration specified by of a component must not be greater than any valid more
significant unit of time.
'''

def calculate(seconds:int,divisor:int)->tuple[int,int]:
    quotient,remainder=divmod(seconds,divisor)
    if(quotient!=0):
        return quotient,remainder
    return 0,seconds       

def output(output_list:list,value:int,unit:str)->list[str]:
    if(value):
        output_list.append(str(value))
        if(value==1):
            output_list.append(unit +',')
        else:
            output_list.append(unit +'s,')
    return output_list

def format_duration(seconds):
    seconds_in_minute=60
    seconds_in_hour=seconds_in_minute*60
    seconds_in_day=seconds_in_hour*24
    seconds_in_year=seconds_in_day*365

    years,seconds=calculate(seconds,seconds_in_year)
    days,seconds=calculate(seconds,seconds_in_day)
    hours,seconds=calculate(seconds,seconds_in_hour)
    minutes,seconds=calculate(seconds,seconds_in_minute)

    out=[] # start building the output
    out=output(out,years,"year")
    out=output(out,days,"day")
    out=output(out,hours,"hour")
    out=output(out,minutes,"minute")
    out=output(out,seconds,"second")

    # remove the last ','
    for i in range(len(out)-1,-1,-1):
        if(out[i].find(',')!=-1):
            out[i]=out[i].replace(',','',1)
            break

    # set the next last ',' to ' and'
    for i in range(len(out)-1,-1,-1):
        if(out[i].find(',')!=-1):
            out[i]=out[i].replace(',',' and',1)
            break
    if(len(out)==0):
        return('now')
    return(" ".join(out))
    

tests=[1,62,120,3600,3662]
for test in tests:
    print(format_duration(test))