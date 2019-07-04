
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
import nilearn.plotting as niplt
from nilearn.masking import unmask
import compute_mask as cm

import nilearn as nil

run=1
func='logcosh'
path_result='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Results/'

path_output='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/'+'run'+str(run)+'/'   

#for sub in range(5,18):
#    path='/windows/ML/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Resources/'
#    
#    components_name='_sub'+str(sub)+'_run'+str(run)+'_fun_'+func+'_components.npy'
#    mixing_name='_sub'+str(sub)+'_run'+str(run)+'_fun_'+func+'_mixing.npy'
#    
#    components=np.load(path+components_name)
#    mixing_matrix=np.load(path+mixing_name)
#    print(components.shape)
#    print(mixing_matrix.shape)
#    
#    fig, axes=plt.subplots(5,4)
#    count=0
#    for  i in range(5):
#        for j in range(4):
#            axes[i,j].plot(mixing_matrix[:,count])
#            count+=1;
#    fig.savefig(path_result+'sub '+str(sub)+' ICA')
#    fig.clear()        
 
 
#mask=nib.load('C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/mask.nii')

#affine=mask.affine

patients_array=np.load(path_result+'patient_run'+str(run)+'.npy')
timeseries=np.load(path_result+'timeseries_run'+str(run)+'.npy')
comp_series=np.load(path_result+'comp_series_run'+str(run)+'.npy')

patient=0;
count=0
for i in range(comp_series.shape[0]):
    
    if(patient!=patients_array[i]):
        count=1;
    else:
        count+=1;    
        
    
    patient=patients_array[i]
    mask=cm.compute_mask(int(patient+3),run)
    img=unmask(comp_series[i],mask_img=mask)
#    nib.save(img,path_output+ 'Patient ' + str(patient+3)+' comp_no '+str(count)+'.nii')
    
    



