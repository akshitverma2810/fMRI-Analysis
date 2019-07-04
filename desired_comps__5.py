# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt




path_res='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Results/'

path_output='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Results/'
run=1

comp_maps=np.load(path_res+'component_maps_run'+str(run)+'.npy')
cor_val=np.load(path_res+'corresponding_correlation_run'+str(run)+'.npy')

comp_time_series=np.load(path_res+'highly_correlated_components_run'+str(run)+'.npy')


best_results_ts=[]
best_results_comp=[]
patients=[]

for i in range(cor_val.shape[0]):
    comp_ts=comp_time_series[i][0][:]
    patient=cor_val[i][0]
    
    comp=comp_maps[i][0][:]
    
    
    plt.plot(comp_ts)
    comp_ts=comp_ts-np.mean(comp_ts)
    norm=np.sum(comp_ts**2)
    auto_corr=np.correlate(comp_ts,comp_ts,mode='full')/norm
    
    plt.show()
    plt.plot(auto_corr)
    plt.show()
    print('Patient='+str(patient))
    select=input(' Enter 1 to select : ')
    
    if select=='1':
        best_results_ts.append(comp_ts)
        best_results_comp.append(comp)
        patients.append(patient)
    

best_results_ts=np.array(best_results_ts)    
best_results_comp=np.array(best_results_comp)

patients_array=np.array(patients)

np.save(path_output+'timeseries_run'+str(run)+'.npy',best_results_ts);
np.save(path_output+'comp_series_run'+str(run)+'.npy',best_results_comp);
np.save(path_output+'patient_run'+str(run)+'.npy',patients_array);


        
        
        
        
        
        
    