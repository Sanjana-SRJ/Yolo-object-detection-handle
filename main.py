from fastapi import FastAPI, Request, HTTPException
import uvicorn
import cv2
import base64
# from final_code import object_detection

app = FastAPI()

def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/hello")
def read_hello():
    return {"Hello": "Hello"}

@app.post("/predict")
def predict_endpoint():
    print("Received a POST request to /predict")
    return {"Hi myself Shubham soni"}

@app.post("/prediction")
async def predict_endpoint(request: Request):
    try:
        input_data = await request.json()
        if "img" not in input_data:
            raise HTTPException(status_code=400, detail="Image data is required")
        
        img_from_request = input_data["img"]
        # test_model_output = object_detection(img_from_request)
        
        return {"status_code": 200, "status": "success", "response": img_from_request}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)