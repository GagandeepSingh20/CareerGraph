from fastapi import FastAPI

app = FastAPI(
    title="CareerGraph API",
    description="A candidate-job matching backend built with FastAPI.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to CareerGraph API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}