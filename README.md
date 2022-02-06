# SAR2SAR-test

Open a colab notebook:
And run the following commands
```
!git clone https://github.com/aspirin01/SAR2SAR-test.git
```
```
!pip uninstall -y tensorflow
```
```
!pip install tensorflow-gpu==1.13.1
```
```
!python /content/SAR2SAR-test/main.py 
 
```



# For despeckling a different image

```
import numpy as np
from PIL import Image                                         
#Enter image path
img = Image.open( '/content/SAR2SAR-test/test_data/sample.jpg' )
img = img.convert("L")
data = np.array( img)
#Convert the new npy file to png and save it in the directory used for running the despeckling algorithm
np.save( '/content/SAR2SAR-test/test_data/sample5.npy', data)
print(" was saved")
print(data.shape)

```
Use this code.
