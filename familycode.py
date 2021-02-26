# code here
import json

#other code
#Make a Dictionary of you, your siblings, parents, and grandparents.  Have at least 4 attributes per person.
fm1 = { "name":"Lola", "age":16, "sport":"soccer", "color":"pink", "notatrisk":True}
fm2 = { "name":"Sophie", "age":16, "sport":"soccer", "color":"purple", "sibling":True, "notatrisk":True}
fm3 = { "name":"Alex", "age":25, "sport":"basketball", "color":"blue", "sibling":True, "notatrisk":True}
fm4 = { "name":"Michael", "age":23, "sport":"wrestling", "color":"blue", "sibling":True}
fm5 = { "name":"Nelly", "age":47, "sport":"yoga", "color":"red", "parent":True}
fm6 = { "name":"Anatoly", "age":54, "sport":"biking", "color":"purple", "parent":True}

#Turn the dictionaries into a list.
list_of_bulkinfamily_members = [fm1, fm2, fm3, fm4, fm5, fm6]
print("List Of Family Members")
print(type(list_of_bulkinfamily_members))
print(list_of_bulkinfamily_members)
print()
for family_member in list_of_bulkinfamily_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['sport'] + ", " + family_member['color'])
print()
#Turn the list into a dictionary called 'family'
family = {'bulkinfamily_members': list_of_bulkinfamily_members}
#Print members to run/console
print("Dictionary Of Family Members")
print(type(family))
print(family)
bulkinfamily_members = family['bulkinfamily_members']
print()
for bulkinfamily_member in bulkinfamily_members:
    print(bulkinfamily_member['name'] + ", " + str(bulkinfamily_member['age']) + ", " + bulkinfamily_member['sport'] + ", " + bulkinfamily_member['color'])
print()
#Turn the dictionary into a JSON file
json_bulkinfamily_members = json.dumps(family)
#Print the JSON file to the run/console window, inserting a character or emoji in between each item in the JSON.
print("JSON Family Members")
print(type(json_bulkinfamily_members))
print(json_bulkinfamily_members)
x = json.loads(json_bulkinfamily_members)
family_members = x['bulkinfamily_members']
print()
for family_member in bulkinfamily_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['sport'] + ", " + family_member['color'])
    print(':)')
print()
#Return JSON file to a dictionary with key "family"- my key is bulkinfamily_members
print("Return JSON File To A Dictionary - Key is bulkinfamily_members")
print(json_bulkinfamily_members)
#Using program logic, make new dictionaries from "family" key/values, creating "parents" and "siblings" key with logically corresponding lists as values.
dictfamilymembers = json.loads(json_bulkinfamily_members)
listfamilymembers = dictfamilymembers['bulkinfamily_members']
parents = []
siblings = []
me = []
for member in listfamilymembers:
    if "parent" in member:
        parents.append(member)
    elif "sibling" in member:
        siblings.append(member)
    else:
        me.append(member)
#Print members to run/console in fashion that highlights
print()
print("Organized Members")
print()
print("Parents")
print(parents)
print()
for member in parents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()
print("Siblings")
print(siblings)
print()
for member in siblings:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()
print("Me")
print(me)
print()
for member in me:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()
