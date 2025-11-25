 
print("Hello, World!")
 
import torch
print(torch.__version__) 
print(torch.cuda.is_available())  # 应该返回 True
print(torch.cuda.device_count())  # 应该返回 1（如果你只有一块 GPU）
print(torch.cuda.get_device_name(0))  # 应该返回你的 GPU 名称
 