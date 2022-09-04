# select max(a.salary) SecondHighestSalary
# from
# (select distinct salary
# from Employee
# order by salary desc
# limit 1 offset 1) a



import numpy as np
import pandas as pd

person = pd.DataFrame({"PersonId":[1,2,3], "salary":[100, 200, 300]})


ans = sorted(person["salary"].unique(), reverse=True)

if len(ans) < 2:
    print(np.nan)
else:
    print(ans[1])
