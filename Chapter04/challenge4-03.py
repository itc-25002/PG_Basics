#3つの必須引数と2つのオプション引数がある関数を書け
def add_mult(a,b,c,x=100,z=1000):
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)
