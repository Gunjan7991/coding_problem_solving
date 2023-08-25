def combine (letterList:list)->list:
    defaut = letterList[0]
    if len(letterList)>1:
        for i in range(1, len(letterList)):
            defaut = combineList(defaut, letterList[i])
    return defaut
    
def combineList(l1: list,l2: list)->list:
    combined = []
    for val0 in l1:
        for val1 in l2:
            combined.append(val0+val1)
    return combined

def letterCombinations(digits: str) -> list[str]:
    if digits == "":
        return []
    keypad = {"2":['a','b','c'], "3":['d','e','f'],
        "4":['g','h','i'], "5":['j','k','l'], "6":['m','n','o'],
        "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']
    }
    letterList = []
    for num in digits:
        if int(num) >9 or int(num)<2:
            return []
        letterList.append(keypad[num])
    return combine(letterList)