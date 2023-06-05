# m.22/hnd/csc/11503
data = {
    "name": "hopeson",
    "age": 22,
    "city": "warri",
    "school":"petrouleum training institute",
    "arr":[1,2,3,4,5,5,6]
}
del data["arr"]
data["age"] = 23
data["city"]= "new york"
data.update({"gender": "male", "occupation":"software developer"})
print(data)
