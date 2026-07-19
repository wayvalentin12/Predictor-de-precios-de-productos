from fastapi import FastAPI
from proyecto import calcular

app = FastAPI()

@app.post("/calcular")
async def calcularprecios(precios: str, meses_futuros: int):
    resultado = calcular(precios, meses_futuros)
    return {"resultado": resultado}
