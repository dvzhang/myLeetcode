# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
#   RETURN (
#       # Write your MySQL query statement below.
#       select distinct a.salary from
#       (select salary,
#       dense_rank() over (order by salary desc) rank_s
#       from employee) a
#       where rank_s=N
#   );
# END


import numpy as np
import pandas as pd

person = pd.DataFrame({"PersonId":[1,2,3], "salary":[100, 200, 300]})

def getN(table, n):
    ans = sorted(table["salary"].unique(), reverse=True)
    if len(ans) < n:
        return np.nan
    else:
        return ans[n-1]
    
print(getN(person, 4))

