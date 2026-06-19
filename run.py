import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.main.server.server:app",
                reload=True,
                host="0.0.0.0",
                port=3001)