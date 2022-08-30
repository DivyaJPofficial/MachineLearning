# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# • Find the length of the set it_companies
# • Add 'Twitter' to it_companies
# • Insert multiple IT companies at once to the set it_companies
# • Remove one of the companies from the set it_companies
# • What is the difference between remove and discard
# • Join A and B
# • Find A intersection B
# • Is A subset of B
# • Are A and B disjoint sets
# • Join A with B and B with A
# • What is the symmetric difference between A and B
# • Delete the sets completely
# • Convert the ages to a set and compare the length of the list and the set.



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(f"length of IT compaines: {len(it_companies)}")

#add twitter
it_companies.add('Twitter')
print(f"add Twitter: {it_companies}")

#multiple IT companies
it_companies.update(['TCS', 'accenture', 'Honeywell'])
print(f"updated IT companies:{it_companies}")

#remove
it_companies.remove('accenture')
print(f"remove a company:{it_companies}")

#discard
it_companies.discard('TCS')
print(f"discard a company:{it_companies}")

#remove() raises key error if element is not found whereas
#discard doesn't raise an error


#join A and B
print(f"join A AND B:{A | B}")

#intersection of A and B
print(f"intersection A AND B:{A & B}")

#subset
print(f"if A is subset of B:{A.issubset(B)}")

#Are A and B disjoint sets
print(f"if disjoint set:{A.isdisjoint(B)}") #disjoint means no elements in common

# • Join A with B and B with A
A.update(B)
print(A)

B.update(A)
print(B)

#symmetric difference
print(f"symmetric difference:{A.symmetric_difference(B)}")

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f"symmetric difference of initial set: a  {A.symmetric_difference(B)}")


#delete set
A.clear()
B.clear()

#Convert the ages to a set and compare the length of the list and the set.
print(f"The length of the list age:{len(age)}")

age = set(age)
print(f"The length of the set age:{len(age)}")


