import torch
from modules.model_builder import FoodDetection
import torchvision.transforms as transforms
from PIL import Image
import io

# Load model
model = FoodDetection(input_shape=3,
    hidden_units=10,
    output_shape=33)

PATH = "models/food_detection_model.pth"
model.load_state_dict(torch.load(PATH))

model.eval()

def transform_image(img):
    # Create transforms
    data_transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
    ])
    image = Image.open(io.BytesIO(img)).convert("RGB")
    return data_transform(image).unsqueeze(0)


def get_prediction(image_tensor):
    test_pred_logits = model(image_tensor)
    test_pred_labels = test_pred_logits.argmax(dim=1)
    return test_pred_labels