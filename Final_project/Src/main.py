from fastapi import FastAPI
import uvicorn
import socket

app = FastAPI()

@app.get("/")
def read_root():
    pod_name = socket.gethostname()
    pod_ip = socket.gethostbyname(pod_name)

    return {
        "status": "ok",
        "message": "Server is running",
        "pod_name": pod_name,
        "pod_ip": pod_ip
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)