from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/health")
async def get_health():
    return {"status": "ok"}

@app.get("/info")
async def get_info():
    return {
	"app": "devops-test",
	"version": "1.0.0",
	"port": 8000
    }

@app.get("/about")
async def get_about():
    return {"message": "This is a DevOps test application"}
