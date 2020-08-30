import pprint
pp = pprint.PrettyPrinter(indent=4)

MyDict=[
    {
        "Name": "Ravi",
        "Age": 25
    },
    {
        "Name": "Raj",
        "Age": 26
    }
]
result= dict()
for x in MyDict:
    print(x["Name"])
    result[x["Name"]]=x

print(result)

result1= {user['Name']:user for user in MyDict if user['Age']>25}
pp.pprint(result1)

"""
load
loads
dump
dumps
"""
