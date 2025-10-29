# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 16:52:18 2025

@author: Carlos Gil
"""

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Load a NIfTI file

nifti_img = nib.load('sub-01_task-rest_bold.nii')
datos= nifti_img.get_fdata()

print(datos.shape)

vol50= datos[:, :, :, 50]

print(vol50.shape)

x_voxel, y_voxel, z_voxel= 10, 20, 20

if (x_voxel >= datos.shape[0] or
    y_voxel >= datos.shape[1] or
    z_voxel >= datos.shape[2]):
    print("Error: coordenadas fuera de la imagen")

valor_voxel= datos[x_voxel, y_voxel, z_voxel]
print(f"El valor del voxel en las coordenadas({x_voxel}, {y_voxel}, {z_voxel}, es: {valor_voxel}" )

plt.imshow(valor_voxel)
plt.show()

def grafvistas(vol, pos):
    x_voxel, y_voxel, z_voxel = pos
    axial= vol[x_voxel,:, :]
    coronal= vol[:, y_voxel,:]
    sagital= vol[:, :, z_voxel]
    

print(grafvistas.shape)
plt.show()


    