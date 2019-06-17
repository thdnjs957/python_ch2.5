def func1(a):
    x = 10
    return a + x # 지역변수에 없으면 바로 global에서 찾는다, 오류 없다

def func2(a):
    return a + x

def fun3(a):
    global g
    g = 3
    return a + g

x = 1

# (L)GB , local 함수 내부
print(func1(5))

# L(G)B
print(func2(10))
print(fun3(10))
# print(g) global에 없어서 에러 , global g 라고 하면 자리 차지함

# LG(B)
print(dir('___builtins___'))
