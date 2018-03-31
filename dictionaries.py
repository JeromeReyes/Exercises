# Jerome C. Reyes BSCpE
print(" ")
print("PERIODIC TABLE")
print(" ")
elements = {
            "B - Boron" : "NONMETALS",
            "C - Carbon" : "NONMETALS",
            "N - Nitrogen" : "NONMETALS",
            "O - Oxygen" : "NONMETALS",
            "F - Florine" : "NONMETALS",
            "SI - Silicon" : "NONMETALS",
            "P - Phosphorus" : "NONMETALS",
            "S - Sulfur" : "NONMETALS",
            "CL - Chlorine" : "NONMETALS",
            "AS - Arsenic" : "NONMETALS",
            "SE - Seienium" : "NONMETALS",
            "BR - Bromine" : "NONMETALS",
            "TE - Tellurium" : "NONMETALS",
            "I - Iodine" : "NONMETALS",
            "AL - Astatine" : "NONMETALS"
    }

for key, val in elements.items():
    print(key, "===", val)

#add in dictionary
elements["HE - Helium"] = "NOBLE GASES"
elements["NE - Neon"] = "NOBLE GASES"
elements["AR - Argon"] = "NOBLE GASES"
elements["KR - Krypton"] = "NOBLE GASES"
elements["XE - Xenon"] = "NOBLE GASES"
elements["RN - Radon"] = "NOBLE GASES"

print("-"*10)

for key, value in sorted(elements.items()):     #SORT
    print(key, "===", value)