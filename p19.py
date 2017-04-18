#Easy but too boring, just Skip
#Idea below:

def classify(year):
    pass

def countDays():
    days=0 
    for year in range(1901,2000):
        if classify(year)==0:
            days+=366
            pass
        else:
            days+=365
            pass
    
days_count=countDays()
sundays=days//7+days%7  #?
