# import os
# import requests
import zipfile
from pathlib import Path

# Setup path to data folder
data_path = Path("data")
image_path = data_path / "foods"

# If the image folder doesn't exist, download it and prepare it
if image_path.is_dir():
    print(f"{image_path} directory already exists")
else:
    print(f"Did not find {image_path} directory, creating one...")
    image_path.mkdir(parents=True, exist_ok=True)

# Download food dataset
# with open(data_path / "food.zip", "wb") as f:
#     print("Downloading food data...")
#     request = requests.get("https://storage.googleapis.com/kaggle-data-sets/1864/33884/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250206T044226Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0d0e3d30f66ed4c1deb7b9aaf67cb310111f7adb59890db6e6430b4b44114ab8778c878c87469b47fb0c1098f8079124352a3f8faaf2f882ff74e98bb1c723d256277be7b68dd7f6bf613fba5588daa3732667ba3db3a1b2c27ea240b54e328a840f334ca1985c7a55fd91f8bb05893000c40eeab33770cf24b880deca03d4f00cc1f24daeda7b7a9eb82a091ef5f4913158386449f2b29016e6499887963f6dc25a32ed33c455a35d2378d025841a309f019d651a5d0c5b0b479c39d9fc17217835b1c383a2ab16c78d100546573ef36f7fd4bb96ae66542ff1d715e28f29c82bca165e1e15e1ad3bbd7e1a0e229e39bb84dbbda41c127a156829107bd81c66")
#     f.write(request.content)

# Unzip food data
with zipfile.ZipFile("food.zip", "r") as zipref:
    print("Unzippping ...")
    zipref.extractall(image_path)

# Remove zip file
# os.remove(data_path /"food.zip")