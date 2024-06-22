from datetime import *

class To_Do :
    def __init__(self , startdate = date.today() , starttime = datetime.now().strftime("%H:%M") , enddate = date.today() , endtime = datetime.now().strftime("%H:%M") , tle , des) :
        self.start_date = startdate
        self.start_time = starttime
        self.end_date = startdate
        self.end_time = endtime
        self.title = tle
        self.description = des