# Streaming températures

## 
## Comment lancer l'application

Modifier le fichier db_aws.py et renseigner les constantes suivantes :
- ENTRY_POINT
- API_PATH
- ID_STATION

```bash
cd ../..
python3 -m venv myvenv
source myvenv/bin/activate
```

```bash

pip install -r apps/dash-tp-iot/requirements.txt
```
Lancer l'application:

```bash
python apps/dash-tp-iot/app.py
```
Ouvrir un navigateur sur http://127.0.0.1:8050

