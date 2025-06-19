colors = ["purple","orange","green"]
guess = input("何色でしょうか？(入力よろしく):")

if guess in colors:
    print("正解！")
else:
    print("残念。違います。")
