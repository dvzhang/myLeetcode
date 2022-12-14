# 1
# select p.firstName, p.lastName, a.city, a.state
# from person p
# left join address a
# on p.personId=a.personId

# 2
# SELECT P.FirstName, P.LastName, A.City, A.State
# FROM Person P
# LEFT JOIN (SELECT DISTINCT PersonId, City, State 
#            FROM Address) A
# on P.PersonId = A.PersonId;


import numpy as np
import pandas as pd

person = pd.DataFrame({"PersonId":[1], "LastName":["wang"], "FirstName":["Allen"]})
address = pd.DataFrame({"PersonId":[1], "AddressId":[2], "City":["NY"]})

ans = person.merge(address, how="left", on="PersonId")[["PersonId", "LastName", "FirstName", "City"]]



print(ans)

