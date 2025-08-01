from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import random
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict():
    prediction = random.choice(["Safe (2x-5x)", "Danger (1.01x-1.5x)", "Lucky (10x+)"])
    return {"prediction": prediction}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(image)

    # Dummy logic based on OCR text (you can improve this later)
    if "1.01" in text:
        result = "Danger (likely to crash)"
    elif "10" in text or "15" in text:
        result = "Lucky (10x+)"
    else:
        result = "Safe (2x-5x)"

    return {"ocr_text": text, "prediction": result}