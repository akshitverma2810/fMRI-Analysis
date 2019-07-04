# -*- coding: utf-8 -*-
import numpy as np
import nilearn.plotting as niplt
from sklearn.decomposition import FastICA
from sklearn.decomposition import fastica
from nilearn.input_data import NiftiMasker
from nilearn.masking import compute_epi_mask
#import dmatrix
import nibabel as nib
from nilearn import image
import matplotlib.pyplot as plt
from scipy.signal import detrend
from sklearn.decomposition import PCA
from nilearn.decomposition import CanICA

import compute_mask as cm



task1='deterministicclassification'
task2='mixedeventrelatedprobe'
task3='probabilisticclassification'

task=task1
#num=[3,4]
num=[3,4,5,6,7,8,9,10,11,12,13,14]
num_comps=10
resources='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Resources/'

#mask=nib.load('C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/mask.nii')


def my_g(x):
#    print(x.shape)
#    print(np.tanh(x).shape)
#    print((1-np.tanh(x)**2).shape)
    
#    print(np.where(x[~np.isfinite(x)]))
#    print(x[np.where(~np.isfinite(x))])
#    x[np.where(~np.isfinite(x))]=0
#    print(np.where(x[~np.isfinite(x)]))
#    alpha = fun_args.get('alpha', 1.0)  # comment it out?
    alpha=1
    x *= alpha
    gx = np.tanh(x)  # apply the tanh inplace
    g_x = np.empty(x.shape[0])
    # XXX compute in chunks to avoid extra allocation
    for i, gx_i in enumerate(gx):  # please don't vectorize.
        g_x[i] = (alpha * (1 - gx_i ** 2)).mean()
    return gx, g_x

#    return np.tanh(x),np.mean(1-np.tanh(x)**2,axis=-1)


for sub in num:
    if sub<10:
        path='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-0'+str(sub)+'/func'
    else:
        path='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-'+str(sub)+'/func'
    
    
    sub_comps1=[]
    sub_comps2=[]
    sub_comps3=[]
    conv_sub_comps=[]
    
    print('RUNNING PILOT '+str(sub)+'......')
    for run in range(1,2):
       
        if sub<10:
               file='/sub-0'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii'
               file_csv='/sub-0'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_events.tsv'
        else:
               file='/sub-'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_bold.nii'
               file_csv='/sub-'+str(sub)+'_task-'+str(task)+'_run-0'+str(run)+'_events.tsv'
               
        img=image.load_img(path+file)
        mask=cm.compute_mask(sub,run)
        masker= NiftiMasker(mask_img=mask,standardize=True,smoothing_fwhm=5)
        
        X=masker.fit_transform(img)

#        ///////////////////////////////////////////////////////////
        print('extracting logcosh....')
        clf1=FastICA(n_components=num_comps,whiten=True, fun='logcosh',max_iter=700,random_state=42)
        X_ica1=clf1.fit_transform(np.transpose(X))
        
        A1=clf1.mixing_
        
        print('extracting tanh.....')
        clf2=FastICA(n_components=num_comps,whiten=True, fun=my_g,max_iter=700,random_state=42)
        X_ica2=clf2.fit_transform(np.transpose(X))
        A2=clf2.mixing_
        
        
        
        corr_matrix=np.empty((num_comps,num_comps))
        for i in range(num_comps):
            ts1=A1[:,i]
            for j in range(num_comps):    
                ts2=A2[:,j]
                corr_matrix[i][j]=np.corrcoef(ts1,ts2)[0][1]
        fig=plt.figure()
        ax1=fig.add_subplot(1,1,1)
        ax1.imshow(corr_matrix,cmap='gray')
        fig.savefig('corr_sub_'+str(sub))
        
        vals=np.where(corr_matrix>=0.7)

        for i in vals[0]:
            ts=A1[:,i]
            plt.plot(np.correlate(ts,ts,mode='full'))
            plt.show()
        
        
        X_ica1=X_ica1[:,vals[0]]
        A1=A1[:,vals[0]]
        
        np.save(resources+'_sub'+str(sub)+'_run'+str(run)+'_fun_logcosh_components',X_ica1)
        np.save(resources+'_sub'+str(sub)+'_run'+str(run)+'_fun_logcosh_mixing',A1)
#      
#        
#        
#        
#
#   
#    ica_sub1=np.array(sub_comps1)
