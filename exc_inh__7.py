import nilearn as nil 
import nilearn.plotting as niplt
import nibabel as nib
import os
import numpy as np

path_session1='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/run1/'

path_session2='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/run2/'

path_exc1='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/excitory_run1/'
path_exc2='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/excitory_run2/'

path_inh1='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/inhibitory_run1/'
path_inh2='C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/Program/Activation_Images/best_images/inhibitory_run2/'





anat=nil.image.load_img('C:/Neuroscience/Neuroscience_Summer_Project/ds002_R2.0.5/sub-05/anat/sub-05_inplaneT2.nii')

files_session1=os.listdir(path_session1)
files_session2=os.listdir(path_session2)


for fl in files_session1:
    img=nil.image.load_img(path_session1+fl)
    img_data=img.get_data()
    
    thresh_max=np.max(img_data)
    thresh_min=(np.min(img_data))
    
    img_data_exc=((img_data*(img_data>0))/thresh_max)*5
    
    img_data_inh=((img_data*(img_data<0))/thresh_min)*5
    
    #######################
    img_data_exc=(img_data_exc*(img_data_exc>=2))
    
    img_data_inh=(img_data_inh*(img_data_inh>=2))
    
    #######################
    
    img_exc=nil.image.new_img_like(img,img_data_exc)
    
    img_inh=nil.image.new_img_like(img,img_data_inh)
    
    nib.save(img_exc,path_exc1+fl)
    
    nib.save(img_inh,path_inh1+fl)
    
    
#    
#for fl in files_session2:
#    img=nil.image.load_img(path_session2+fl)
#    img_data=img.get_data()
#    
#    thresh_max=np.max(img_data)
#    thresh_min=(np.min(img_data))
#    
#    img_data_exc=((img_data*(img_data>0))/thresh_max)*5
#    
#    img_data_inh=((img_data*(img_data<0))/thresh_min)*5
#    
#    #######################
#    img_data_exc=(img_data_exc*(img_data_exc>=2))
#    
#    img_data_inh=(img_data_inh*(img_data_inh>=2))
#    
#    #######################
#    
#    img_exc=nil.image.new_img_like(img,img_data_exc)
#    
#    img_inh=nil.image.new_img_like(img,img_data_inh)
#    
#    nib.save(img_exc,path_exc2+fl)
#    
#    nib.save(img_inh,path_inh2+fl)

    





#image_prob_session1=nil.image.concat_imgs([path_exc1+fl for fl in files_session1])
#image_prob_session2=nil.image.concat_imgs([path_session2+fl for fl in files_session2])












#thresh1=np.max(image_prob_session1.get_data())
#thresh2=np.max(image_prob_session2.get_data())



#image_prob_session1_thresh=image_prob_session1.get_data()*(image_prob_session1.get_data()>thresh1)
#image_prob_session2_thresh=image_prob_session2.get_data()*(image_prob_session2.get_data()>thresh2)

#image_prob_session1=nil.image.new_img_like(image_prob_session1,image_prob_session1_thresh)
#image_prob_session2=nil.image.new_img_like(image_prob_session2,image_prob_session2_thresh)


#
#prob_map_session1=niplt.plot_prob_atlas(image_prob_session1,anat_img=anat, display_mode='z', cut_coords=12)
#
#prob_map_session2=niplt.plot_prob_atlas(image_prob_session2,anat_img=anat, display_mode='z', cut_coords=12)
#
#prob_map_session1.savefig('session1_map')
#prob_map_session2.savefig('session2_map')











