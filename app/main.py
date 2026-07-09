from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
  return {"message":"Welcome to Career Graph"}

@app.get("/health")
def health_check():
    return {"status":"Server is running in Okay condition"}



