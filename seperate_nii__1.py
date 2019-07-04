# -*- coding: utf-8 -*-
import os
import nilearn as nil
from nilearn import image
import nibabel as nib

task1='deterministicclassification'
task2='mixedeventrelatedprobe'
task3='probabilisticclassification'

task=task1
#num=[5,6,7,8,9,10,11,12,13,14,15,16,17]

num=[4]
resources='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Resources/'








for sub in num:
    if sub<10:
        path='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-0'+str(sub)+'/func'
    else:
        path='C/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-'+str(sub)+'/func'
    
   
    
    print('RUNNING PILOT '+str(sub)+'......')
    
    
    
    for run in range(1,2):
       
        out='/'+task+'_run_'+str(run)+'/'
        os.makedirs(path+'/'+task+'_run_'+str(run))
        
        if sub<10:
               file='/sub-0'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii.gz'
               file_csv='/sub-0'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_events.tsv'
        else:
               file='/sub-'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii.gz'
               file_csv='/sub-'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_events.tsv'
               
        img=nib.load(path+file)
        print(img.shape)
        for i in range(img.shape[-1]):
            fl=nil.image.index_img(img,i)
            nib.save(fl,path+out+str(i+1))
            