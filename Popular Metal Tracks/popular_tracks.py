import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('ClassicMetal.csv')

popular_tracks= data.sort_values(by='Popularity', ascending=False).head(10)


plt.figure(figsize=[10,6])

plt.bar(popular_tracks['Track'], popular_tracks['Popularity'], color="darkblue")
plt.xlabel('Tracks')
plt.ylabel('Popularity')
plt.title('Most popular metal tracks')

plt.xticks(rotation= 45, ha="right")
plt.tight_layout()
plt.show()
