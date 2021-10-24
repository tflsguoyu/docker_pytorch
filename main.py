# Instead of using sudo systemctl start docker use: sudo /etc/init.d/docker start , as of right now we do not have systemd in WSL 2.
# sudo docker run --gpus all -it --rm -v `pwd`/:/gytest/ nvcr.io/nvidia/pytorch:21.08-py3
import torch

print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
