import torch
import matplotlib.pyplot as plt
from skimage import data,filters,io,color
from skimage.restoration import inpaint
import numpy as np

img_ori = io.imread('/home/zhuzhu/Desktop/webwxgeticon.jpeg')

mask = np.zeros(img_ori.shape[:-1],dtype=np.int)
mask[120:180, 100:350] = 1
mask[560:700, 200:300] = 1
mask[300:500, 800:890] = 1

img_defect = img_ori.copy()
index = (np.array([1,2]),np.array([2,2]))

img_defect[np.where(mask)] = 1
img_result = inpaint.inpaint_biharmonic(img_defect,mask,multichannel=True)

fig,ax = plt.subplots(2,2)

ax[0][0].set_title('original image')
ax[0][0].imshow(img_ori)

ax[0][1].set_title('mask')
ax[0][1].imshow(mask,cmap=plt.cm.gray)

ax[1][0].set_title('defected image')
ax[1][0].imshow(img_defect)

ax[1][1].set_title('inpainted image')
ax[1][1].imshow(img_result)

for i in range(2):
    for j in range(2):
        ax[i][j].axis('off')
plt.show()
