""" Modello dati per le prenotazioni """
from pydantic import BaseModel
class Prenotazione(BaseModel):
    dataPrenotazione: str
    oraPrenotazione: str
    numPersone: int
    phone: str
    nominativo: str

class PrenotazioneResponse(BaseModel):
    id: str
    dataPrenotazione: str
    oraPrenotazione: str
    numPersone: int
    phone: str
    nominativo: str