st = input("好きな食べ物は？:")
print(st)

strg = open("food.txt","w")
strg.write(st)
strg.close()
