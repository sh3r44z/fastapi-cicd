from fastapi import FastAPI 

app = FastAPI(title="FastAPI CI/CD Demo", version = "1.0.0")


@app.get("/")
def root():
    return{"message": "Hello from FastAPI", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return { 
        "app": "fastapi-cicd",
        "version": "1.0.0",
        "description": "A demo APi for CI/CD pipeline practice"
    
    }
