
import nilearn.plotting as niplt
import numpy as np
from nilearn.masking import unmask
import nibabel as nib
from nilearn import image
import matplotlib.pyplot as plt
from nilearn import image
import os



path_exc1='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/excitory_run1/'
path_inh1='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/inhibitory_run1/'

path_exc2='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/excitory_run2/'
path_inh2='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/inhibitory_run2/'

path_result='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Results/'

path_output='C:\\Neuroscience\\Neuroscience_Summer_Project\\ds002_R2.0.5\\Program\\Activation_Images\\best_images\\stat_map_images\\threshold'

sub=14
run=1
patients_array=np.load(path_result+'patient_run'+str(run)+'.npy')


patient=0;
count=0
thresh=2.5
for i in range(patients_array.shape[0]):
    
    if(patient!=patients_array[i]):
        count=1;
    else:
        count+=1;        
    
    patient=patients_array[i]
    sub=patient+3
    
    sub=int(sub)
    
    if sub<10:
        path_anat='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-0'+str(sub)+'/anat/'
    else:
        path_anat='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-'+str(sub)+'/anat/'
    
    anat_file='rmprage_defaced.nii'
    anat_img=image.load_img(path_anat+anat_file)
    
    file_bold='Patient '+str(sub)+'.0'+' comp_no '+str(count)+'.nii'
    img=image.load_img(path_exc1+file_bold)
#    img=image.load_img(path_inh1+file_bold)
    print(img.shape)
    print(anat_img.shape)
    stat_name='Patient_'+str(sub)+'comp_no_'+str(count)
#    stat_plot=niplt.plot_stat_map(img,bg_img=anat_img,display_mode='z',cut_coords=[-22,-18,-14,-10-6,-2,2,6,10,14,18,22],threshold=thresh,title=stat_name)
    stat_plot=niplt.plot_stat_map(img,bg_img=anat_img,display_mode='z',axes=(20,20,0.5,0.5),cut_coords=[-22,-16,-10,0,6,10],threshold=thresh)
    
   
    
#    if i>40:
#        break
    
#    stat_plot.savefig(path_output+'_inh'+str(thresh)+"\\"+stat_name)
#    stat_plot.savefig(path_output+str(thresh)+"\\"+stat_name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















