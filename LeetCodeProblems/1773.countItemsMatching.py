from typing import List



def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    myDict = {'type': 0, 'color': 1, 'name': 2}
    count = 0
    for item in items:
        if item[myDict[ruleKey]] == ruleValue:
            count += 1
    print("my dictionary rule key: ", myDict[ruleValue])
    return count



items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]] 
ruleKey = "color" 
ruleValue = "silver"
print(countMatches(items, ruleKey, ruleValue))
