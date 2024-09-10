

from datetime import datetime

def DayNumberToDate(daynum):
# initializing day number
    day_num=str(daynum)
    # print day number
    #print("The day number : " + str(day_num))
    
    # adjusting day num
    day_num.rjust(3 + len(day_num), '0')   
    # Initialize year
    year = "2022" 
    # converting to date
    res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y")
    # printing result
    print("Resolved date : " + str(res))