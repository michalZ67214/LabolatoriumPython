import numpy as np

tablica = np.zeros((3,3))

print(tablica)

tab1 = np.zeros((3,3))
print('\n1)')
tab1[1:3, :2] = 1
print(tab1)

tab2 = np.zeros((3,3))
print('\n2)')
tab2[:, 2:] = 1
print(tab2)

tab3 = np.zeros((3,3))
print('\n3)')
tab3[:2, :] = 1
print(tab3)

tab4 = np.zeros((3,3))
print('\n4)')
tab4[0:2,0] = 1
print(tab4)

tab5 = np.zeros((3,3))
print('\n5)')
tab5[:2, [0, 2]] = 1
print(tab5)