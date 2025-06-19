import csv

movies = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("ch.csv","w") as f:
    w = csv.writer(f, delimiter=",")
    for x in movies:
        w.writerow(x)
        
