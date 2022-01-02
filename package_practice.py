# import travel.thailand
# trip_to = travel.thailand.ThilandPackage()
# trip_to.detail()

# from travel.thailand import ThilandPackage
# trip_to = ThilandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *

from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThilandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))