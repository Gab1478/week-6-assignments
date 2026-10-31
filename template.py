"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. 
import pandas as pd
people = pd.read_csv("people.csv")
print(people)


# ================================================================= PROCESS
# 2.
people["percent"]=(people["value"] / people["limit"]) * 100
print(people)

# ================================================================== OUTPUT
# 3. 
import pandas as pd
people = pd.read_csv("people.csv")

people["percent"] = (people["value"] / people["limit"]) * 100
print(people)


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
