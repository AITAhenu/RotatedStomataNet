__version__ = '0.4.2'
git_version = 'efb0b265ce62bb9205ba93701628c4b57012001c'
from torchvision import _C
if hasattr(_C, 'CUDA_VERSION'):
    cuda = _C.CUDA_VERSION
