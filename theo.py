#%%
from math import factorial
def is_wprime(n):
    return n > 1 and bool (n == 2 or (n % 2 and (factorial(n-1) + 1 ) % n ==0))
    if __name__== '__main__':
            c=10000
            print(f"Prime under {c}:",end='\n  ')
            print([n for n in range(c) if is_wprime(n)])
# %%
 print(f"Prime under {10000}:",end='\n  ')
 print([n for n in range(10000) if is_wprime(n)])
