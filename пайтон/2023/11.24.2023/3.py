import math
x1_coordinate_algebra_10klass_gdz=input("x1 оордината ")
y1_absis_piska_jopa=input("y1 координата абцис ")
x2_coordinate_algebra_10klass_gdz=input("x2 оордината ")
y2_absis_piska_jopa=input("y2 координата абцис ")
try:
    x1_coordinate_algebra_10klass_gdz=float(x1_coordinate_algebra_10klass_gdz)
    y1_absis_piska_jopa=float(y1_absis_piska_jopa)
    x2_coordinate_algebra_10klass_gdz=float(x2_coordinate_algebra_10klass_gdz)
    y2_absis_piska_jopa=float(y2_absis_piska_jopa)
except ValueError:
    exit()
rasstoyanie=math.sqrt((x2_coordinate_algebra_10klass_gdz-x1_coordinate_algebra_10klass_gdz)**2+(y2_absis_piska_jopa-y1_absis_piska_jopa)**2)
print(rasstoyanie)