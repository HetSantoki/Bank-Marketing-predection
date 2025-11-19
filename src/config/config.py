'''
author : Santoki Het
github : @SantokiHet
organization : L.J University
'''

from gpu_config.check import GPU_Config

# Dataset configurations
DATASET = {
    "path": "D:\GitProject\Bank-Marketing-Campaign-main\Bank-Marketing-Campaign-main\data\Bank.csv",
    "train_split": 0.8,
    "validation_split": 0.1,
    "test_split": 0.1,
    "batch_size": 32,
    "shuffle": True,
}

# Model configurations
MODEL = {
    "type": "ANN",
    "layers": 5,
    "activation": "relu",
    "dropout_rate": 0.5,
    "input_dim": 38,
    "output_classes": 2,
}

# Training configurations
TRAINING = {
    "epochs": 100,
    "learning_rate": 0.001,
    "optimizer": "Adam",
    "loss_function": "binary_crossentropy",
    "metrics": ["accuracy"],
}

# Hardware configurations
HARDWARE = {
    "use_gpu": GPU_Config.check_gpu_configration(),
    "device": "cuda:0",
}

# Experiment details
EXPERIMENT = {
    "name": "Bank-Marketing-Campaign",
    "description": "Understand customer behavior and preferences",
    "seed": 42,
}

#Model Details
MODEL_DETAILS = {
    "trained_model":"D:\GitProject\Bank-Marketing-Campaign-main\Bank-Marketing-Campaign-main\saved_model\model.h5",
    "preprocessed_pipeline":"D:\GitProject\Bank-Marketing-Campaign-main\Bank-Marketing-Campaign-main\saved_model\preprocessing_pipeline.pkl"
}
