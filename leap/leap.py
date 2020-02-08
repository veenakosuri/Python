import logging

#Set Logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('leap.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Custom Exception class
class LeapError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def leap_year(year):
    '''Function takes year as input and returns boolean value to say it is a leap year or not '''

    logger.debug("leap_year invoked with year [" + str(year) + "]")

    #Check if it is a valid year value
    try:
        val = int(year)
        if (val < 0):
            raise LeapError("Invalid number, year should be greater than 0")
        elif val > 9999:
            raise LeapError("Invalid number, year should be a 4-digit positive number")
    except ValueError:
        logger.error("Invalid number, year should be a 4-digit positive number")
        raise ValueError
    except Exception as e:
        logger.error(e)
        raise
    finally:
        pass
    
    # A leap year is exactly divisible by 4 except for centuary years (years ending with 00)
    # The century year is a leap year only if it is perfectly divisible by 400
    isLeap = False
    if year%4 == 0:
        if  year%100 == 0:
            if year%400 == 0:                
                isLeap = True
        else:            
            isLeap = True

    return isLeap
