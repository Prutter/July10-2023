def getHighestSalary(list):
	max = 0
	result={}
	for emp in list:
		if emp["salary"] > max :
			max = emp["salary"]
			result = emp
	return result 

list = [
    {
        "name" : "kashish 1",
        "salary" : 10000
    },
    {
        "name" : "kashish 3",
        "salary" : 30000
    },
    {
        "name" : "kashish 2",
        "salary" : 20000
    }
]

print(getHighestSalary(list))