from fastapi import FastAPI, File, UploadFile
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import io

app = FastAPI()

# Загрузка модели DETR
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")

@app.post("/detect-objects")
async def detect_objects(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    
    outputs = model(**inputs)
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes)[0]

    detected_objects = [
        {
            "label": model.config.id2label[label.item()],
            "score": round(score.item(), 3),
            "box": [round(i, 2) for i in box.tolist()]
        }
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"])
        if score.item() > 0.7  # фильтр по score > 0.7
    ]

    return {"detected_objects": detected_objects}
