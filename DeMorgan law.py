a = bool(int(input('Enter value for A (0 for False, 1 for True): ')))
b = bool(int(input('Enter value for B (0 for False, 1 for True): ')))

lhs_1 = not (a and b)
rhs_1 = (not a) or (not b)

lhs_2 = not (a or b)
rhs_2 = (not a) and (not b)

print('-----------------------------')

print('LHS_1 (not (A and B)) :', lhs_1)
print('RHS_1 ((not A) or (not B)) :', rhs_1)

print('LHS_2 (not (A or B)) :', lhs_2)
print('RHS_2 ((not A) and (not B)) :', rhs_2)

print('-----------------------------')

if (lhs_1 == rhs_1) and (lhs_2 == rhs_2):
    print('De Morgan\'s First Law is verified: not (A and B) = (not A) or (not B)')
    print('De Morgan\'s Second Law is verified: not (A or B) = (not A) and (not B)')
else:
    print('De Morgan\'s Laws are not verified.')
