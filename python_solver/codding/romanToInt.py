def romanToInt(s: str) -> int:
    val = 0
    roman = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C":100,
        "XC":90,
        "L":50,
        "XL": 40,
        "X":10,
        "IX":9,
        "V":5,
        "IV":4,
        "I":1
    }
    j = 0
    while j < len(s):
        string = ""
        if (s[j] == "C" or s[j] == "X" or s[j] == "I")  and j+1 != len(s):
            string += s[j]
            if s[j] == "C" and (s[j+1] == "D"  or s[j+1] == "M"):
                string += s[j+1]
                j+=1
            elif s[j] == "X" and (s[j+1] == "L"  or s[j+1] == "C"):
                string += s[j+1]
                j+=1   
            elif s[j] == "I" and (s[j+1] == "V"  or s[j+1] == "X"):
                string += s[j+1]
                j+=1 
            j+=1 
            
        else:
            string += s[j]
            j+=1
        if string in roman:
            val += roman[string]
        else:
            return 0
    return val