
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


# Read in the dataset and create a color array based on the value in the drive train column.
mpg = pd.read_csv("mpg.csv", index_col=0)
colors=[]
for l in mpg.drv:
    if l=='f':
        colors.append('gold')
    elif l=='r':
        colors.append('skyblue')
    else:
        colors.append('black')


# In[17]:


fig, ax = plt.subplots(2,2, figsize=(15,15))
#Fig 18.1: Standard scatter plot of city fuel economy vs engine displacement
ax[0,0].scatter(mpg.displ, mpg.cty, c=colors)
ax[0,0].set_xlabel('displacement(l)')
ax[0,0].set_ylabel('fuel economy (mpg)')
ax[0,0].set_title('Fig 18.1: City fuel economy vs engine displacement')
classes = ['FWD','RWD','4WD']
class_colors = ['gold','skyblue','black']
leg_key = []
for i in range(0,len(class_colors)):
    leg_key.append(plt.Circle((0,0),0.2, fc=class_colors[i]))
ax[0,0].legend(leg_key,classes,loc=1, title='drive train')

#Fig 18.2 Scatter plot of city fuel economy vs engine displacement with partially transparent points
ax[0,1].scatter(mpg.displ, mpg.cty, c=colors, alpha=0.4)
ax[0,1].set_xlabel('displacement(l)')
ax[0,1].set_ylabel('fuel economy (mpg)')
ax[0,1].set_title('Fig 18.2: City fuel economy vs engine displacement \n Using partially transparent points')
ax[0,1].legend(leg_key,classes,loc=1, title='drive train')

#Fig 18.3 Scatter plot of city fuel economy vs engine displacement with small jitter on x-axis
#Add random amount of jitter along the displacement x-axis to the dataset based on the spread of the data
stdev1 = 0.01*(max(mpg.displ)-min(mpg.displ))
displ_jitter1 = mpg.displ + np.random.randn(len(mpg.displ))*stdev1
# plot the new displacement with jitter
ax[1,0].scatter(displ_jitter1, mpg.cty, c=colors, alpha=0.4)
ax[1,0].set_xlabel('displacement(l)')
ax[1,0].set_ylabel('fuel economy (mpg)')
ax[1,0].set_title('Fig 18.3: City fuel economy vs engine displacement \n Using small amount of jitter')
ax[1,0].legend(leg_key,classes,loc=1, title='drive train')

#Fig 18.4 Scatter plot of city fuel economy vs engine displacement with too much jitter on x-axis
#Add larger random amount of jitter along the displacement x-axis to the dataset based on the spread of the data
stdev2 = 0.08*(max(mpg.displ)-min(mpg.displ))
displ_jitter2 = mpg.displ + np.random.randn(len(mpg.displ))*stdev2
# plot the new displacement with jitter
ax[1,1].scatter(displ_jitter2, mpg.cty, c=colors, alpha=0.4)
ax[1,1].set_xlabel('displacement(l)')
ax[1,1].set_ylabel('fuel economy (mpg)')
ax[1,1].set_title('Fig 18.4: City fuel economy vs engine displacement \n Using too much jitter')
ax[1,1].legend(leg_key,classes,loc=1, title='drive train')

plt.show()
fig.savefig('task23.png', bbox_inches='tight')

