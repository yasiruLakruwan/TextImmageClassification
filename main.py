

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from tensorflow.keras.models import load_model
from utils.preprocessor import preprocess_image

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and class labels
model = load_model("models/text_classifier1.h5")
class_labels = ['form', 'invoice', 'note']

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    # Read image bytes
    file_bytes = await file.read()

    try:
        img = preprocess_image(file_bytes)
        predictions = model.predict(img)
        predicted_class = class_labels[np.argmax(predictions)]

        return {"prediction": predicted_class}
    except Exception as e:
        return {"error": str(e)}
