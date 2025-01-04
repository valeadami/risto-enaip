# Restaurant API with FastAPI

Questo progetto implementa un'API REST per la gestione di un ristorante, progettata per l'integrazione con un chatbot Voiceflow.

## Tecnologie Utilizzate

- Python 3.11
- FastAPI
- Uvicorn
- Git per il versioning
- Render per il deployment


## API Endpoints

- `GET /`: Homepage
- `GET /menu`: Restituisce il menu del ristorante
- `GET /bevande`: Restituisce la lista delle bevande disponibili

## Deployment

Il progetto è configurato per il deployment su Render.com. Il deployment viene attivato automaticamente ad ogni push su GitHub.

## Struttura del Progetto

```
resto-ai/
├── venv/
├── main.py           # File principale dell'applicazione
├── requirements.txt  # Dipendenze del progetto
├── .gitignore       # File e cartelle ignorati da git
└── README.md        # Questo file
```

## Note di Sviluppo

- Il progetto è stato sviluppato per scopi educativi
- L'integrazione principale è con un chatbot Voiceflow
- Le risposte API sono strutturate specificamente per l'integrazione con Voiceflow


