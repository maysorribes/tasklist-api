# tasklist-api

API REST senzilla per gestionar una llista de tasques, construïda amb Flask i publicada a Docker Hub mitjançant GitHub Actions.

## Ús local

```bash
pip install -r requirements.txt
python app.py
```

## Ús amb Docker

```bash
docker pull <DOCKERHUB_USERNAME>/tasklist-api:latest
docker run -p 5000:5000 <DOCKERHUB_USERNAME>/tasklist-api
```

## Endpoints

| Mètode | Ruta | Descripció |
|--------|------|------------|
| GET | /tasks | Llista totes les tasques |
| POST | /tasks | Crea una nova tasca |
| PUT | /tasks/:id | Actualitza una tasca |
| DELETE | /tasks/:id | Elimina una tasca |
