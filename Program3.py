# Create a tuple containing names of your sisters and your brothers (imaginary siblings are
# fine)
# • Join brothers and sisters tuples and assign it to siblings
# • How many siblings do you have? 
# • Modify the siblings tuple and add the name of your father and mother and assign it to
# family_members


#sister and brother tuple
sister = ('Priyanka', 'Bhargavi', 'Vani', 'Ramya', 'Sireesha')
brother = ('Charan', 'Praneeth', 'Pranav', 'Eshwar', 'Meena')

#join
siblings = sister + brother

#count of siblings
print(f"Number of siblings: {len(siblings)}")

#modify tuple with father and mother
temp = list(siblings)
temp.extend(['Raju','Rani'])
family_members = tuple(temp)
print(f"family members are:{family_members}")

