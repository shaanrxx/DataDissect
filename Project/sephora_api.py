import requests
import pandas as pd
url = "https://sephora.p.rapidapi.com/products/v2/list"

querystring = {"number":"3","size":"500","country":"GB","language":"en-SG","sort":"price"}

headers = {
	"X-RapidAPI-Key": "9c2ded9108msha55090905dfe96dp152c1ajsnc4c239548328",
	"X-RapidAPI-Host": "sephora.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
print(response.json())
# Create DataFrame from JSON response
df = pd.DataFrame.from_records(response.json()['products'])
df.to_csv('sephora_products.csv', index=False)
# Display first 5 rows of DataFrame
print(df.head())