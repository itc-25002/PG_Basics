#文字列をfloat型に変換して戻り値とする関数を書け。起こり得る例外をキャッチする例外処理を書こう
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)
