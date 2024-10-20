# take marks as input from user
print('Enter marks Obtained in 4 Subjects: ')
Math = int(input('Math :'))
English = int(input('English :'))
Biology = int(input('Biology :'))
Chemistry = int(input('Chemistry :'))

# Let's calculate the percentage of marks 
sum = Math+English+Biology+Chemistry
print('sum of Math,English,Biology and Chemistry')

perc = (sum/400)*100

print(end='Percentage Mark = ')
print(perc)