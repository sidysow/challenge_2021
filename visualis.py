
# %%
import numpy as np
import pandas as pd
from pandas import DataFrame
from ipywidgets import interact 
from matplotlib import pyplot as plt
from download import download
from datetime import datetime
import json
from pandas import Series
from ipywidgets import interact
#%%
# PREPARATION DES DONNES

# %%
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json'
path_target = "bike1_traffic.json"
download(url, path_target, replace=False)


#%%

bike1_traffic_df = pd.read_json('bike1_traffic.json', lines=True)



# %%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json'
path_target = "bike2_traffic.json"
download(url, path_target, replace= False)
#%%
bike2_traffic_df = pd.read_json('bike2_traffic.json', lines=True)






#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json'
path_target = "bike3_traffic.json"
download(url, path_target, replace= False)
#%%
bike3_traffic_df = pd.read_json('bike3_traffic.json', lines=True)



#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json'
path_target = "bike4_traffic.json"
download(url, path_target, replace= False)
#%%
bike4_traffic_df = pd.read_json('bike4_traffic.json', lines=True)



#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042635_archive.json'
path_target = "bike5_traffic.json"
download(url, path_target, replace= False)
#%%
bike5_traffic_df = pd.read_json('bike5_traffic.json', lines=True)




#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063161_archive.json'
path_target = "bike6_traffic.json"
download(url, path_target, replace= False)
#%%
bike6_traffic_df = pd.read_json('bike6_traffic.json', lines=True)


#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063162_archive.json'
path_target = "bike7_traffic.json"
download(url, path_target, replace= False)
#%%
bike7_traffic_df = pd.read_json('bike7_traffic.json', lines=True)



#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_XTH19101158_archive.json'
path_target = "bike8_traffic.json"
download(url, path_target, replace= False)
#%%
bike8_traffic_df = pd.read_json('bike8_traffic.json', lines=True)


#%%
url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063163_archive.json'
path_target = "bike9_traffic.json"
download(url, path_target, replace= False)
#%%
bike9_traffic_df = pd.read_json('bike9_traffic.json', lines=True)



#%%

url='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063164_archive.json'
path_target = "bike10_traffic.json"
download(url, path_target, replace= False)
#%%
bike10_traffic_df = pd.read_json('bike10_traffic.json', lines=True)




# %%
data_test_df=bike1_traffic_df.join(bike1_traffic_df['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test_df=data_test_df.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 

data_test_df['start_of_day'] = data_test_df['start_of_day'].str.replace('T',' ')
#%%

time_improved = pd.to_datetime(data_test_df['start_of_day'] ,
                               format='%Y-%m-%d %H:%M:%S')
time_improved                       

data_test_df['start_day'] = time_improved

data_test_df= data_test_df.set_index(['start_day'])

# %%
#                                             Preparing Data 1
#------------------------------------------------------------------------------------------------------------------------

#%%
bike1_traffic_df=bike1_traffic_df.rename(columns = {'intensity': 'celleneuve'})

bike2_traffic_df=bike2_traffic_df.rename(columns = {'intensity': 'barracasa'}) 

bike3_traffic_df=bike3_traffic_df.rename(columns = {'intensity': 'Laverune'}) 

bike4_traffic_df=bike4_traffic_df.rename(columns = {'intensity': 'Lattes 2'}) 

bike5_traffic_df=bike5_traffic_df.rename(columns = {'intensity': 'Lattes 1'}) 

bike6_traffic_df=bike6_traffic_df.rename(columns = {'intensity': 'Vieille poste'}) 

bike7_traffic_df=bike7_traffic_df.rename(columns = {'intensity': 'Gerhardt'})

bike8_traffic_df=bike8_traffic_df.rename(columns = {'intensity': 'Tanneurs'}) 

bike9_traffic_df=bike9_traffic_df.rename(columns = {'intensity': 'Delmas 1'}) 

bike10_traffic_df=bike10_traffic_df.rename(columns = {'intensity': 'Delmas 2'}) 

#%%

#%%

data_reel = pd.DataFrame((bike1_traffic_df['celleneuve'], bike2_traffic_df['barracasa'],bike3_traffic_df['Laverune'],bike4_traffic_df['Lattes 2'],bike5_traffic_df['Lattes 1'],bike6_traffic_df['Vieille poste'],bike7_traffic_df['Gerhardt'],bike8_traffic_df['Tanneurs'],bike9_traffic_df['Delmas 1'],bike10_traffic_df['Delmas 2']))
data_reel=data_reel.T
#%%
data_reel['startday'] = time_improved
#%%
data_reel = data_reel.set_index(['startday'])


#%%

def hist_explore( position ='celleneuve', c='red' ):

  
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    ax.plot(data_reel[position], '-*',color=c)
    #ax.hist(df_titanic['Age'], density=density,
            #bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel('Age')
    plt.ylabel('Number of bike')
    plt.title("courbes")
    plt.tight_layout()
    plt.show()


## todo CORRECT THE DENSITY OPTION.

# %%

interact(hist_explore ,position=['celleneuve','barracasa','Laverune','Lattes 2','Lattes 1','Vieille poste','Gerhardt','Tanneurs','Delmas 1','Delmas 2'] ,c=['red','maroon','blue','purple','lime'])

#%%



















# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
