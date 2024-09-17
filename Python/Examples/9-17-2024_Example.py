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
        
    
main()