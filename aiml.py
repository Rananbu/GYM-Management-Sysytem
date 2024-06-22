import os
swipath = 'C:\\Program Files\\swipl\\bin'
os.environ['PATH'] = swipath + os.pathsep + os.environ['PATH']
from pyswip import Prolog

prolog = Prolog()
prolog.consult('http://localhost:9999')  # Replace 9999 with the port you're using

for solution in prolog.query("father(bob, Child)"):
    print(solution["Child"])
