import numpy as np
marks=np.array([85,70,59,30])
for mark in marks:
    if mark>=80:
        print(f"{mark} Grade A")
    elif mark>=60 and mark<80:
        print(f"{mark} Grade B")
    elif mark>=40 and mark<60:
        print(f"{mark} Grade C")
    else:
        print(f"{mark} fail vais muji")
        
