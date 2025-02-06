import os
from pathlib import Path

from torchvision import datasets,  transforms
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split

NUM_WORKERS = os.cpu_count()

def create_dataloader(
        image_dir: str,
        transform: transforms.Compose,
        batch_size: int,
        num_workers: int=NUM_WORKERS
):
    """Creates training and testing dataloaders"""

    # Use ImageFolder to create datasets
    image_data = datasets.ImageFolder(image_dir, transform=transform)

    # Get class names
    class_names = image_data.classes

    # Train test split
    X_train, X_test = train_test_split(image_data, test_size=0.2, random_state=42)

    # Turn images into data loaders
    train_dataloader = DataLoader(
        X_train,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True
    )
    test_dataloader = DataLoader(
        X_test,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True
    )

    return train_dataloader, test_dataloader, class_names

