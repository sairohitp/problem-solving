def timeConversion(s):
    new_s = s
    if "PM" in new_s and "12" in new_s[0:2]:
        return s[:-2]
    if "AM" in new_s and "12" in new_s[0:2]:
        new_s = new_s.replace(new_s[0:2], "00")
        return new_s[:-2]
    if "PM" in new_s:
        time = str(int(s[0:2]) + 12)
        new_s = new_s.replace(str(new_s[0:2]),time)
        return new_s[:-2]      
    else:
        return s[:-2]

timeConversion()