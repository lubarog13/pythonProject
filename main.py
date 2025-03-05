# This is a sample Python script.

from bisectiondraw import bisectionsearch2slides
from bisectionsearch import bsearch
from drawplot import gs2slides
from goldensearch import gsearch
from newton import nsearch
from newtondraw import newtondrawfig
from steepestsearch import sdsearch
from steepestDraw import *
from gradientsearch import grsearch
from secantdraw import secantsearchsecants
from secantsearch import ssearch
from newtonsearch import *
import numpy as np
from newtonDraw import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def iter(x):
    if x == None:
        return
    print(x[0])
    if x[1] != None:
        iter(x[1])


def prepend(x, list):
    return x, list


def reverse(list):
    if list == None:
        return
    i, link = list
    new_list = (i, None)
    while link:
        i, link = link
        new_list = (i, new_list)
    return new_list


def binary_search(x, key, start, end):
    if start > end:
        return -start - 1
    middle = (start + end) // 2
    if x[middle] == key:
        return middle
    elif x[middle] > key:
        end = middle - 1
        return binary_search(x, key, start, end)
    else:
        start = middle + 1
        return binary_search(x, key, start, end)


def sort(x):
    i = 0
    start = 0
    while i < len(x):
        end = i
        key = x[i]
        new = binary_search(x, key, start, end)
        if new != i:
            if new < 0:
                new = 0
            swap(x, i, new)
        i += 1
    return x


def swap(x, old, new):
    if not x:
        return None
    element = x.pop(old)
    x.insert(new, element)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


import re


def solve1(passwords):
    number_list = list(map(lambda x : str(x), range(0, 10)))
    lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    def contain(str, arr):
        for x in arr:
            if str.find(x)!=-1:
                return True
        return False
    pass_list = list(filter(lambda x: (len(x) >= 6 and contain(x, number_list) and contain(x, lowercase_alphabet) and contain(x, uppercase_alphabet)), passwords.split(";")))
    print(pass_list)
    return ",".join(pass_list)


def solve():
    return list(map(lambda x: int(x) ** 2, input().split(" ")))


def solve(cities):
    try:
        regs = list(map(lambda y: y.split(','), cities.split(";")))
        return ";".join(list(map(lambda x: ",".join(x), list(zip(regs[0], regs[1], regs[2])))))
    except:
        return ""


def find(tree, key):
    if tree.get("key") == key:
        return tree
    if key > tree.get("key"):
        if tree.get("right", None) is None:
            return None
        else:
            return find(tree.get("right"), key)
    else:
        if tree.get("left", None) is None:
            return None
        else:
            return find(tree.get("left"), key)


def dfs(tree):
    if tree.get("left") is not None:
        dfs(tree.get("left"))
    print(tree.get("key"))
    if tree.get("right") is not None:
        dfs(tree.get("right"))


def bfs(tree):
    if tree:
        a = [tree]
        while len(a) > 0:
            b = a.pop(0)
            print(b['key'])
            if 'left' in b:
                a.append(b['left'])
            if 'right' in b:
                a.append(b['right'])


class Student:
    marks = []


Alex, Mary = Student(), Student()
Alex.marks.append(5)
Mary.marks = [].append(5)


class A():
    def __init__(self, values):
        self.values = values


class B(A):
    def __len__(self):
        return len(self.values)

def solve(ln):
    d = {}
    arr = ln.split('\n').lower()
    for x in arr:
        d.update({x: d.get(x, 0) + 1})
    print(d)


def solve():
    x, y = list(map(lambda k: int(k), input().split(' ')))
    return [x + y, x - y, x * y]


import math

class Shape:

    def area(self):
        pass

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


import math

class Rectangle(Shape):  # наследуется от Shape
    a = 5  # первая сторона
    b = 10  # вторая сторона
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

    def __str__(self):
        return str(self.area()) + ", " + "Rectangle"
    pass

class Ellipse(Shape):  # наследуется от Shape
    radius = 5  # первый радиус
    second_radius = 10  # второй радиус
    def __init__(self, radius, second_radius):
        self.radius = radius
        self.second_radius = second_radius
    def area(self):
        return math.floor(math.pi * self.radius * self.second_radius)

    def __str__(self):
        return str(self.area()) + ", " + "Ellipse"

class Square(Shape):  # наследуется от Shape
    a = 5  # сторона квадрата
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a*self.a

    def __str__(self):
        return str(self.area()) + ", " + "Square"

class ShapeList(list):
    def append(self, __object):
        if isinstance(__object, Shape):
          super().append(__object)

    def __str__(self):
        s = ""
        for i in range(0, len(self) ):
            s += str(self.__getitem__(i))+"\n"
        return s

def sort1(list):
    return sorted(list, key=lambda x: x[2])

def find(ufs, key):
    if key not in ufs:
        return key
    return find(ufs, ufs[key])

def mst(list):
    list = sort1(list)
    result = []
    ufs = {}
    for r in list:
        if find(ufs, r[0])!=find(ufs, r[1]):
            result.append(r)
            ufs.update({find(ufs, r[0]): find(ufs, r[1])})
    return result
# Press the green button in the gutter to run the script.
def main():
    # print("Find:")
    # interval = [-2, 10]
    # tol = 1e-10
    # [xmin, f, neval, coords] = bsearch(interval,tol)
    # print([xmin, f, neval])
    # bisectionsearch2slides(interval, coords)

    # print("Find:")
    # interval = [-2, 7]  # for drawing
    # tol = 0.01
    # [xmin, f, neval, coords] = nsearch(tol, 1.3)
    # print([xmin, f, neval])
    # newtondrawfig(interval, coords)

    # print("Find:")
    # interval = [-2, 5]
    # tol = 1e-6
    # [xmin, f, neval, coords] = ssearch(interval,tol)
    # print([xmin, f, neval])
    # secantsearchsecants(coords, interval)

    # x0 = np.array([0, 1])
    # tol = 1e-3
    # [xmin, f, neval, coords] = grsearch(x0, tol)
    # print(xmin, f, neval)
    # gradientdrawing(coords, len(coords))

    # print("Himmelblau function:")
    # x0 = np.array([[1.3], [2.0]])
    # tol = 1e-3
    # [xmin, f, neval, coords] = sdsearch(fH, dfH, x0, tol)  # h - функция Химмельблау
    # print(xmin, f, neval)
    # draw(coords, len(coords), "h", fH)
    #
    # print("Rosenbrock function:")
    # x0 = np.array([[1.0], [-2.0]])
    # tol = 1e-7
    # [xmin, f, neval, coords] = sdsearch(fR, dfR, x0, tol)  # r - функция Розенброка
    # print(xmin, f, neval)
    # draw(coords, len(coords), "r", fR)

    print("Himmelblau function:")
    x0 = np.array([[-2.0], [-2.0]])
    tol = 1e-3
    [xmin, f, neval, coords] = nsearch(fH, dfH, x0, tol)  # h - функция Химмельблау
    print(xmin, f, neval)
    draw(coords, len(coords), "h", fH)

    print("Rosenbrock function:")
    x0 = np.array([[-1.0], [-1.0]])
    tol = 1e-9
    [xmin, f, neval, coords] = nsearch(fR, dfR, x0, tol)  # r - функция Розенброка
    print(xmin, f, neval)
    draw(coords, len(coords), "r", fR)


if __name__ == '__main__':
    main()