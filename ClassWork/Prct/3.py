# --- Task Three ---
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "->", end=" ")
    result = leap_year(yr)
if result == testresults[i]:
    print("OK")
else:
    print("Failed")
