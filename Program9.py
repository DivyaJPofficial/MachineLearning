# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

#list of students weights
in_lbs =  [150, 155, 145, 148, 120, 130, 100]

in_kgs = []
#converting weight to kgs
for x in in_lbs:
    in_kgs.append(round(x * 0.45359237,2))

print(f"weight in kgs: {in_kgs}")
