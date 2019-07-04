import os
import nilearn as nil
import nibabel as nib
from nilearn import image



num=[3,4]
#num=[5,6,7,8,9,10,11,12,13,14]
task='deterministicclassification' 

run=1



for sub in num:
    print(sub)
    if sub<10:
        path_r='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-0'+str(sub)+'/func/deterministicclassification_run_'+str(run)+'/'
        file_output=file='sub-0'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii'  
        path_func='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-0'+str(sub)+'/func/'
    else:
        path_r='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-'+str(sub)+'/func/deterministicclassification_run_'+str(run)+'/'
        file_output=file='sub-'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii'  
        path_func='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-'+str(sub)+'/func/'
    
    slices=[]
    
        
    for i in range(1,181):
        file_name_input='r'+str(i)+'.nii'
        
        img=nib.load(path_r+file_name_input)
        slices.append(img)
        print(img.affine)
    
    bold_img=image.concat_imgs(slices)
    nib.save(bold_img,path_func+file_output)   
    
    
    
    
    
    
    
    
    
    
    