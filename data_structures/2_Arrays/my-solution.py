# Question 1
list = {'January': 2200, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190}

# 1. In Feb, how many dollars you spent extra compare to January?
print(list['February']-list['January'])
# 2. Find out your total expense in first quarter (first three months) of the year.
print(list['January']+list['February']+list['March'])
# 3. Find out if you spent exactly 2000 dollars in any month
for i in list:
    if list[i] == 2000:
        print(i)
else: print('No such month')
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
list['June'] = 1980
print(list)
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
# based on this
list['April'] = list['April'] - 200
print(list['April'])

# Question 2
heros=['spider man','thor','hulk','iron man','captain america']

#     1. Length of the list
print(len(heros))
#     2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
#     3. You realize that you need to add 'black panther' after 'hulk',
#        so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)
#    5. Sort the heros list in alphabetical order
heros.sort()
print(heros)

# Question 3
max = int(input("Enter the upper limit: "))
list = []
for i in range(max//2):
    list.append(2*i+1)
print(list)
