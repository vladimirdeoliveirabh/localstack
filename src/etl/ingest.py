import requestes
import json
from datetime import datetime
import os

api_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"raw_data_{timestamp}.json"
    filepath = os.path.join("data", "bronze", filename)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Dados raw salvos em {filepath}")
else:
    print(f"Erro ao consultar a API: {response.status_code}")
