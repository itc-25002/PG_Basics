import csv


movies = [["トップガン","卒業白書","マイノリティ・リポート"],["タイタニック","レヴェナント","インセプション"],["トレーニング デイ","マイ・ボディガード","フライト"]]
#movies = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("cha.csv","w") as f:
    w = csv.writer(f, delimiter=",", encoding="utf-8")
    for x in movies:
        w.writerow(x)
        
