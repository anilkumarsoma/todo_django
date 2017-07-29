from datetime import datetime
date_object = datetime.strptime('03/10/2016', '%d/%m/%Y')
past = datetime.now()
remaningdays = date_object - past
print remaningdays.days
