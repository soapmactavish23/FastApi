import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/saudar/{nome}")
async def saudar(nome: str):
    return {"message": f"Olá, {nome}"}

if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0",
                port=3001)