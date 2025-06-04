#リスト["The","fox","jumped","over","the","fence","."]の文字列を正しい英文になるように連結しよう。単語と単語の間は空白が必要ですが、最後のピリオドの前には不要です。文字列を要素に持つリストを一つに連結するメソッドがあることを忘れずに!

string = ["The","fox","jumped","over","the","fence","."]
string = " ".join(string)
string = string[0:-2] + "."
print(string)
