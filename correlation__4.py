# -*- coding: utf-8 -*-

import numpy as np
#import nitime
from sklearn.preprocessing import scale
from sklearn.decomposition  import PCA
from scipy import signal
from scipy.stats import spearmanr

task1='deterministicclassification'
task2='mixedeventrelatedprobe'
task3='probabilisticclassification'

task=[task1,task2,task3]

task=task1
num=[3,4]
num=[3,4,5,6,7,8,9,10,11,12,13,14]

R_thresh=0.6
func='logcosh'
run=1;
num_comps=10
comps=[]
mixing=[]
result_path='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Results/'
for sub in num:
    path='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Resources/'
    
    components_name='_sub'+str(sub)+'_run'+str(run)+'_fun_'+func+'_components.npy'
    mixing_name='_sub'+str(sub)+'_run'+str(run)+'_fun_'+func+'_mixing.npy'
    
    components=np.load(path+components_name)
    mixing_matrix=np.load(path+mixing_name)
    print(components.shape)
    print(mixing_matrix.shape)
    
    comps.append(components)
    mixing.append(mixing_matrix)

    
corr_values_marix0=np.zeros((len(num),len(num),num_comps,num_comps))
new_cov_matrix=np.zeros((len(num)*num_comps,len(num)*num_comps))

for l in range(0,len(num)): 
    print('CORRELATION OF SUBJ '+str(l)+' WITH REST')
    for k in range(0,len(num)):
        print('CORRELATION OF SUBJ '+str(l)+' WITH SUBJ '+str(k))    
        for i in range(num_comps):
            t1=signal.detrend(mixing[l][:,i])
            for j in range(num_comps):
                t2=signal.detrend(mixing[k][:,j])
                corr_values_marix0[l][k][i,j]=np.corrcoef(t1,t2)[0,1]
#                corr_values_marix0[l][k][i,j]=spearmanr(t1,t2)[0]
                
        new_cov_matrix[l*num_comps:(l+1)*num_comps,k*num_comps:(k+1)*num_comps]=corr_values_marix0[l][k]      
        
     
                
        
print(np.where(corr_values_marix0>R_thresh))        
print(corr_values_marix0[np.where(corr_values_marix0>R_thresh)])
np.save(result_path+'CORRELATION_MATRIX_run'+str(run)+'.npy',new_cov_matrix)

high_corr_pairs=[]
voxel_pairs=[]
#vals=np.where(np.logical_and((corr_values_marix0>R_thresh),(corr_values_marix0!=1.0)))
vals=np.where((corr_values_marix0>=R_thresh))
corr_value=[]
for i in range(len(vals[0])):
    sub=vals[0][i]
    sub_comp=vals[1][i]
#    if (sub!=sub_comp):    
    corr_value.append([sub,sub_comp,corr_values_marix0[sub][sub_comp][vals[2][i]][vals[3][i]]])
    voxel_pairs.append([comps[sub][:,vals[2][i]], comps[sub_comp][:,vals[3][i]]])
    high_corr_pairs.append([mixing[sub][:,vals[2][i]], mixing[sub_comp][:,vals[3][i]]])
    
highly_correlated_components=np.array(high_corr_pairs)      
corresponding_correlation=np.array(corr_value)
component_maps=np.array(voxel_pairs)

np.save(result_path+'highly_correlated_components_run'+str(run),highly_correlated_components)
np.save(result_path+'corresponding_correlation_run'+str(run),corresponding_correlation)  
np.save(result_path+'component_maps_run'+str(run),voxel_pairs)        
        
        
                

        
        
    
   
    
    