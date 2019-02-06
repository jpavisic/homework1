
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_iris


# In[3]:


# Load the iris dataset using sklearn
iris_dataset=load_iris()


# In[4]:


# Save the sepal and petal measurements in a "data" array and the type of flower in a "label" array.
measurements = iris_dataset['data']
sepal_length = measurements[:,0]
sepal_width = measurements[:,1]
petal_length = measurements[:,2]
petal_width = measurements[:,3]

label = iris_dataset['target']

# Create an array of colors corresponding to the different flower types from the target array.
colors=[]
for l in label:
    if l==0:
        colors.append('blue')
    elif l==1:
        colors.append('red')
    else:
        colors.append('green')


# In[6]:


# Create a pair-plot of the iris dataset similar to Figure 1-3 in IMLP with the diagonals containing histograms
fig, axes = plt.subplots(4,4, figsize=(15,15))
# Generate all pairwise scatter plots
axes[0,1].scatter(sepal_width, sepal_length, c=colors, alpha=0.6)
axes[0,2].scatter(petal_length, sepal_length, c=colors, alpha=0.6)
axes[0,3].scatter(petal_width, sepal_length, c=colors, alpha=0.6)
axes[1,0].scatter(sepal_length, sepal_width, c=colors, alpha=0.6)
axes[1,2].scatter(petal_length, sepal_width, c=colors, alpha=0.6)
axes[1,3].scatter(petal_width, sepal_width, c=colors, alpha=0.6)
axes[2,0].scatter(sepal_length, petal_length, c=colors, alpha=0.6)
axes[2,1].scatter(sepal_width, petal_length, c=colors, alpha=0.6)
axes[2,3].scatter(petal_width, petal_length, c=colors, alpha=0.6)
axes[3,0].scatter(sepal_length, petal_width, c=colors, alpha=0.6)
axes[3,1].scatter(sepal_width, petal_width, c=colors, alpha=0.6)
axes[3,2].scatter(petal_length, petal_width, c=colors, alpha=0.6)

# Generate the histograms along the diagonal
axes[0,0].hist(sepal_length, bins=20, color='blue', ec='black', alpha=0.8)
axes[1,1].hist(sepal_width, bins=20, color='blue', ec='black', alpha=0.8)
axes[2,2].hist(petal_length, bins=20, color='blue', ec='black', alpha=0.8)
axes[3,3].hist(petal_width, bins=20, color='blue', ec='black', alpha=0.8)
axes[0,0].set_ylabel("sepal length (cm)")
axes[1,0].set_ylabel("sepal width (cm)")
axes[2,0].set_ylabel("petal length (cm)")
axes[3,0].set_ylabel("petal width (cm)")
axes[3,0].set_xlabel("sepal length (cm)")
axes[3,1].set_xlabel("sepal width (cm)")
axes[3,2].set_xlabel("petal length (cm)")
axes[3,3].set_xlabel("petal width (cm)")

# Adjust the subplots to similar configuration to the figure
for i in range(0,3):
    for j in range(0,4):
        axes[i,j].set_xticklabels([])
for i in range(0,4):
    for j in range(1,4):
        axes[i,j].set_yticklabels([])
fig.subplots_adjust(hspace=0, wspace=0)

# Add plot title and legend
fig.suptitle("Pair Plot of the Iris Dataset \n Colored by Class Label", fontsize=24)
classes = ['setosa','versicolor','virginica']
class_colors = ['blue','red','green']
leg_key = []
for i in range(0,len(class_colors)):
    leg_key.append(plt.Circle((0,0),0.2, fc=class_colors[i]))
axes[0,2].legend(leg_key,classes,loc=2, title='Legend for Scatter Plot Points')

plt.show()
fig.savefig('task22.png', bbox_inches='tight')

