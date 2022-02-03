import numpy as np
from PIL import Image                                                                                
img = Image.open( '/content/sample3.png' )
# for image in path:
  
img = img.convert("L")
data = np.array( img)
#Convert the new npy file to png
np.save( '/content/SAR2SAR-test/test_data/sar4.npy', data)
print(" was saved")
print(data.shape)
