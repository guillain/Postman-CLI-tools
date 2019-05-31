# Postman-CLI-tools
Extract Postman configuration and save it locally under JSON format.

## Prerequisite
- Python 3.x and packages: `pip install -r requirements.txt` (if you use .env file)
- Environment variable: 
  - By shell: `postman_api_key=xxxxxxxxx`
  - By .env file: `cp sample.env .env`
  
## Execution
`python main.py`

## Trace
```
$ python main.py
workspaces listing...
workspaces dumping...
-  84f1dbac-aa50-4dda-ab46-d77b46095eec LBL
collections listing...
collections dumping...
-  00002fdf-c204-45b6-bd17-c648bc740027 BO-Elastic-ML
-  003700eb-a7bb-4fdf-8f51-443e630171d4 BO-LBL-ELK
-  005b3900-d322-4b72-8102-74c2a1d0ca51 BO-Postman
-  00350d4d-0055-4668-ab41-faa08c1ff300 BO-Elastic
-  004ddaf3-4400-449f-9d83-7cc1984e0005 BO-Elastic-Watcher
-  00aa9e88-b624-0076-a570-d8d47a00e354 LBL ELK
-  0011c89f-e2c6-4c00-9f5d-7bfa00fde985 BO-API-GW
-  00421bf4-9ea3-4583-001c-46007812c041 BO-OpenWeather
environments listing...
environments dumping...
-  001d306d-c82c-4d3f-8000-00d38c4bf1e2 BO-Postman
-  00836c23-9dbb-497c-9c00-0042d0920f52 BO-Elastic-OVH
-  006978ac-5338-47f3-00e3-12002eac223b BO-OpenWeather
-  0029173a-4756-4700-8d46-72fa000baf4f BO-Elastic-AWS
-  003bcea0-76d7-0073-94b2-d7c403000f3c LBL
-  00628877-a700-43e5-8908-8402a9ae00c7 BO-API-GW-localhost
-  007a8cb4-00b0-4f7d-988c-cd44a228d000 BO-API-GW AWS Dev
-  002eb400-45f7-4f97-93b6-779dc92bc717 BO-API-GW
-  007e00cc-21fa-4233-8cd6-3aa9d5691ced BO-API-App
-  00005f5e-113c-4a85-aa75-378bed37e0d5 BO-API-GW localhost
$
```
