import pandas as pd
from yfinance import Ticker

file_path = "nasdaq-listed.csv"
df = pd.read_csv(file_path)
first_row = df.iloc[:, 0]
ewp = int(input("Enter 0 only EPS Enter 1 for both price and EWS"))

with open("demo.txt", "w") as f:  

    for i in range(len(first_row)):
        k = str(first_row[i])
        fl = {}
        try:
            l = Ticker(k)
            j = l.income_stmt
            
            
            if 'Diluted EPS' in j.index:
                eps = j.loc['Diluted EPS'].head(2)
                
                eps_ea = eps.to_list()
                filtered_eps = [x for x in eps_ea if pd.notna(x)]
                # print(filtered_eps)
                if len(filtered_eps)>1:
                    # print(k,filtered_eps)
                    if filtered_eps[0]>2*filtered_eps[1] and (filtered_eps[0]>0 and filtered_eps[1]>0) and ewp == 0:
                        f.write(f"{k} {filtered_eps}\n")

                        prev_pri = l.history(period='1y').iloc[0]['Close']
                        curr_pri = l.info["previousClose"]
                        x = (curr_pri*100)/prev_pri
                        if x<=40 and ewp==1:
                            f.write(f"{k} {x}\n")
        
        except Exception as e:
            f.write(f"Error fetching data for {k}: {e}\n")
            

