# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# • Sort the list and find the min and max age
# • Add the min age and the max age again to the list
# • Find the median age (one middle item or two middle items divided by two)
# • Find the average age (sum of all items divided by their number)
# • Find the range of the ages (max minus min)

#creating a list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort() #built-in sort
print(f" Given list: {ages}") #sorted list

print(f"max age: {max(ages)}, min age: {min(ages)}") #min and max age

ages.extend([min(ages),max(ages)]) #add the max and min ages back to the list
print(f"New list: {ages}") #print the list after new additions

#median
middle = int(len(ages)/2) #find middle index in the list
print(middle)
if middle % 2 == 0:    #find if its even
    print(f"The median of ages: {int((ages[middle-1]  + ages[middle] )/ 2)}")

#average age
print(f"The average of ages: {sum(ages)/len(ages)}")

#range
print(f"Range of the ages: {max(ages) - min(ages)}")
