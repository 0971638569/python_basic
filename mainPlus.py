import mathPlus
import mathPlus as ma
from mathPlus import _sum
from mathPlus import sum as su
import os, sys

# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
lib_path = os.path.abspath(os.path.join('modules'))

# thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)

from mathModules import mul

a = ma.sum(1, 2, '3')
b = su('1', 2, 1)
c = mathPlus.sum('1', 5, '2')
d = _sum(2, 3, 4)
e = mul(1, 2, 0)

print(a)
print(b)
print(c)
print(d)
print(e)