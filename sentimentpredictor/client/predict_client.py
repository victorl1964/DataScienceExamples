import json
import requests
import pandas as pd
"""Setting the headers to send and accept json responses """
header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
"""Reading test batch """
x_test = pd.read_csv('comments.csv',encoding="utf-8-sig")
"""Converting Pandas Dataframe to json"""
x_test = x_test.to_json(orient='records')
#print(x_test)
resp = requests.post("http://127.0.0.1:5000/sentimentpredictor/predictmany", data = json.dumps(x_test),headers= header)

print(resp.status_code)
print(resp.json())
