from datetime import datetime
from fastapi import FastAPI,  HTTPException
from models.prenotazione import Prenotazione, PrenotazioneResponse

#FastAPI è un framework web moderno e veloce per costruire API con Python 3.6+ basato su standard Python type hints.
app = FastAPI()
# Modello dati per le prenotazioni
prenotazioni = []
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/menu")
async def get_menu():
    menu = {
        "menu": [
            "Grilled Chicken",
            "Hamburger",
            "Sandwich",
            "Focaccia"
        ]
    }
    return {"answers": menu}

# Endpoint per le bevande
@app.get("/v1/bevande")
async def get_bevande():
    bevande = {
        "beverages": [
            "Light Beer",
            "Dark Beer",
            "Special Beer",
            "Coca Cola",
            "Still Water"
        ]
    }
    return {"answers": bevande}
@app.post("/v1/prenotazioni", response_model=PrenotazioneResponse)
async def add_prenotazione(prenotazione: Prenotazione):
    id_prenotazione = f"RES-{int(datetime.now().timestamp() * 1000)}"
    new_prenotazione = PrenotazioneResponse(
        id=id_prenotazione,
        **prenotazione.dict()
    )
    prenotazioni.append(new_prenotazione)
    return new_prenotazione

# Endpoint per ottenere tutte le prenotazioni
@app.get("/v1/prenotazioni")
async def get_prenotazioni():
    return {
        "success": True,
        "message": "Prenotazioni recuperate con successo" if prenotazioni else "Nessuna prenotazione trovata",
        "prenotazioni": prenotazioni,
        "status": 200
    }
@app.get("/v1/prenotazioni/{id}")
async def get_prenotazione(id: str):
    prenotazione = next((p for p in prenotazioni if p.id == id), None)
    if not prenotazione:
        raise HTTPException(status_code=404, detail=f"Prenotazione con ID {id} non trovata")
    return {
        "success": True,
        "message": "Prenotazione trovata",
        "prenotazioni": prenotazione
    }

# Endpoint per modificare una prenotazione
@app.put("/v1/prenotazioni/{id}")
async def update_prenotazione(id: str, prenotazione: Prenotazione):
    index = next((i for i, p in enumerate(prenotazioni) if p.id == id), -1)
    if index == -1:
        raise HTTPException(status_code=404, detail=f"Prenotazione con ID {id} non trovata")
    
    updated_prenotazione = PrenotazioneResponse(
        id=id,
        **prenotazione.dict()
    )
    prenotazioni[index] = updated_prenotazione
    return {
        "success": True,
        "message": "Prenotazione aggiornata con successo",
        "data": updated_prenotazione
    }
