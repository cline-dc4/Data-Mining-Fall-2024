"""
@author: DC Cline
""" 

def main():
    d = dict()
    d["Ant"] = 3
    d["Banana"] = 6
    d["Dog"] = 3
    
    #Information about dictionary
    print("Length:", len(d))
    print("Value for Dog:", d["Dog"])
    for key in d.keys():
        print(key, ":", d[key])
        
    #changing our data
    d["Dog"] = -10
    d["Corban"] = 6
    print("After change")
    for key in d.keys():
        print(key, ":", d[key])
        
    #Dictionary: Value is an array
    dictWithArray = dict()
    dictWithArray["A"] = ["Array", "Apple", "Ant"]
    dictWithArray["E"] = ["Elephant", "Extravagant", "Elegant", "Extracurricular"]
    for k in dictWithArray.keys():
        print(k, ":")
        value = dictWithArray[k]
        for i in range(len(value)):
            print(value[i])
            
    #nested dictionary
    students = {1326: {"year": 3, "gpa": 3.9, "python": 2},
                2435: {"year": 4, "gpa": 3.2, "python": 5}}
    
    avg = 0
    for k in students.keys():
        row = students[k]
        avg += row["gpa"]
    avg = avg/len(students)
    print("Average GPA:", avg)
main()