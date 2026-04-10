from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
	return {"status": "ok", "output": "Hello world!"}

@app.get("/text/{text}")
def text(text: str):
	return {"status": "ok", "output": str(text)}
