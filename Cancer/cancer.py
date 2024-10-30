import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('cancer_dataset.csv')

survival_counts= data['survived'].value_counts()
print(survival_counts)

plt.figure(figsize=(8,8))
plt.pie(survival_counts, labels=['Dead (0)', 'Alive (1)'], autopct='%1.1f%%', startangle=140, colors=['#F10000', '#2eb774'])
plt.title('Kanserden ölenler ve hayatta kalanlar yüzdelik dağılım')
plt.axis('equal')
plt.show()
