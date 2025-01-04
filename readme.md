# Restaurant API with FastAPI

Questo progetto implementa un'API REST per la gestione di un ristorante, progettata per l'integrazione con un chatbot Voiceflow.

## Tecnologie Utilizzate

- Python 3.11
- FastAPI
- Uvicorn
- Git per il versioning
- Render per il deployment


## API Endpoints pubblici

### Gestione Prenotazioni
- `GET /`: Homepage
- `GET /menu`: Restituisce il menu del ristorante
- `GET /bevande`: Restituisce la lista delle bevande disponibili
- `POST /v1/prenotazioni`: Crea una nuova prenotazione
  ```json
  {
    "dataPrenotazione": "2024-01-20",
    "oraPrenotazione": "19:30",
    "numPersone": 4,
    "phone": "1234567890",
    "nominativo": "Mario Rossi"
  }
  ```

- `GET /v1/prenotazioni`: Recupera tutte le prenotazioni
- `GET /v1/prenotazioni/{id}`: Recupera una prenotazione specifica
- `PUT /v1/prenotazioni/{id}`: Modifica una prenotazione esistente
  ```json
  {
    "dataPrenotazione": "2024-01-21",
    "oraPrenotazione": "20:30",
    "numPersone": 6,
    "phone": "1234567890",
    "nominativo": "Mario Rossi"
  }
  ```

### Formato Risposte

Esempio di risposta per una prenotazione creata:
```json
{
  "success": true,
  "message": "Prenotazione aggiunta con successo",
  "prenotazioni": {
    "id": "RES-1234567890",
    "dataPrenotazione": "2024-01-20",
    "oraPrenotazione": "19:30",
    "numPersone": 4,
    "phone": "1234567890",
    "nominativo": "Mario Rossi"
  },
  "status": 200
}

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


