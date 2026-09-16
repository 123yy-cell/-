import torch

def demo_tensor():
    x = torch.arange(1, 6, dtype=torch.float32)
    return x.mean().item()
