# from datetime import datetime

# days = ['Mon', 'The', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# print(datetime.now().month)

# datetime.now().strftime

import time

print(time.strftime('%c', time.localtime(time.time())))