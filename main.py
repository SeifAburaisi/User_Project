import fastapi

app = fastapi.FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/health')
def read_health():
    return {'Status': 'Healthy'}