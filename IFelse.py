import math
import os
import random
import re
import sys

n: int = 20
if n % 2 != 0:
    print("Weird \n")
if n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird \n")
if n % 2 == 0 and 6 <= n <= 20:
    print("Weird \n")
if n % 2 == 0 and n > 20:
    print("Not Weird")
