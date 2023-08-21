def intToRoman(num: int) -> str:
    if num > 9999  or num <0:
        return ""
    roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
             ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"], 
             ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
             ["","M","MM","MMM", "ĪṼ", "Ṽ", "ṼĪ", "ṼĪĪ", "ṼĪĪĪ", "ĪẌ"]]
    roman_val = ""
    i=0
    while num>0:
        val = num%10
        num = (num-val)/10
        roman_val = roman[i][int(val)]+roman_val
        i += 1
    return roman_val