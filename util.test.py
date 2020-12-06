from util import shouldGoOutside
from datetime import datetime

assert(shouldGoOutside(100) == True)
assert(shouldGoOutside(-100) == False)

assert(shouldGoOutside(50, datetime(2020, 6, 1)) == False)
assert(shouldGoOutside(50, datetime(2020, 8, 1)) == False)
assert(shouldGoOutside(50, datetime(2020, 10, 1)) == False)
assert(shouldGoOutside(50, datetime(2020, 11, 1)) == True)
assert(shouldGoOutside(50, datetime(2020, 12, 1)) == True)

print("Tests pass")