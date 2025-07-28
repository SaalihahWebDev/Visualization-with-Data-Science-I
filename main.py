import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
rooms_counts=["1 rooms","2 rooms","3 rooms","4 rooms","5 rooms"]
house_amounts=[5,15,25,20,10]
fig,axes=plt.subplots(1,2,figsize=(12,5))
sns.barplot(x=rooms_counts,y=house_amounts,ax=axes[0])
axes[0].set_title("Bar Plot:Rooms vs Houses")
axes[0].set_xlabel("Number of Rooms")
axes[0].set_ylabel("Number of Houses")
axes[1].plot(rooms_counts,house_amounts,marker="o",linestyle="-",color="green")
axes[1].set_xlabel("Number of Rooms")
axes[1].set_ylabel("Number of Houses")
plt.tight_layout()
plt.show()