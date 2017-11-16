a = int(input("how many B bacterias are there? "))
b = int(input("how nuch time in minutes will we wait? "))

c = a * 2**(b/2)
print("After {0} minutes, we would have {1} bacterias".format(b, c))
