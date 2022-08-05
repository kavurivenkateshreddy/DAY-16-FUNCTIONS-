# def greet():
#  print('Hello')
# greet()         # Hello

# def greet(n):
#     print('Hello '+n)
# greet('HD')     # Hello HD
# greet('PY')     # Hello PY

# def greet(*names):
#     print('Hey',names[3])
# greet('Python','Programming','Core','Functions')  # Hey Functions

# def details(n,a):
#     print('Hey '+n + '! Your Age is '+str(a))
# details('hd',25)                                    # Hey hd! Your Age is 25
# details(n='HD',a=26)                                # Hey HD! Your Age is 26
# details(a=26,n='HD')                                # Hey HD! Your Age is 26

# def details(n,a):
#     print('Hey '+n + '! Your Age is '+str(a))
# n=input('Enter your Name: ')                  # KVR
# a=input('Enter your Age: ')                   # 25
# details(n,a)                                          # Hey KVR! Your Age is 25

# def r(x,y):
#     return x*y
# print(r(5,6))                                         # 30

def z(p,q):
    return p*q,p+q; 
p=int(input())                                  # 10
q=int(input())                                  # 20
print(z(p,q))                                           # (200, 30)