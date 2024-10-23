p = bool(int(input('Enter value for P:')))
q = bool(int(input('Enter value for Q:')))
r = bool(int(input('Enter value for R:')))

lhs_1 = p or (q and r)
rhs_1 = (p or q) and (p or r)

print('LHS_1 :',lhs_1)
print('RHS_1 :',rhs_1)

lhs_2 = p and (q or r)
rhs_2 = (p and q) or (p and r)

print('LHS_2 :',lhs_2)
print('RHS_2 :',rhs_2)

print('-------------------')
if (lhs_1 == rhs_1) and (lhs_2 == rhs_2):
    print('P or (Q and R) = (P or Q) and (P or R)')
    print('P and (Q or R) = (P and Q) or (P and R)')
    print('Distributive law is verified')
