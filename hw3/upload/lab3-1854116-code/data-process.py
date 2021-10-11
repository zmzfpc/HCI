# %%
import pandas as pd
import numpy as np
# %%
# Data Preprocess
df=pd.read_csv("./dataset/google-play-store-apps/googleplaystore.csv")
for i in df:
    print(df[i].value_counts())
df.replace("NaN",np.nan,inplace=True)
df.isnull().sum()

# %%
df.dropna(inplace=True)

# %%
out=pd.DataFrame(df,columns=["App","Category","Rating","Reviews","Size","Installs","Price","ContentRating"])
out.to_csv("preprocess.csv",index=None)
# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#matplotlib画图中中文显示会有问题，需要这两行设置默认字体
df=pd.read_csv("./dataset/google-play-store-apps/googleplaystore.csv")
df.drop_duplicates(subset='App', inplace=True)#去重
df = df[df['AndroidVer'] != np.nan]#去除掉空值
df = df[df['AndroidVer'] != 'NaN']#去除掉空值
df = df[df['Installs'] != 'Free']#去除掉串列明显写错的sample
df = df[df['Installs'] != 'Paid']#去除掉串列明显写错的sample
print('Number of apps in the dataset : ' , len(df))
df['Installs']= df['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
df['Installs']= df['Installs'].apply(lambda
x: x.replace(',', '') if ',' in str(x) else x)
df['Installs']= df['Installs'].apply(lambda x: int(x))
df['Size'] = df['Size'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: str(x).replace(',', '') if 'M' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
df['Size'] = df['Size'].apply(lambda x: float(x))
df['Installs']=df['Installs'].apply(lambda x: float(x))
df['Price'] = df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
df['Price'] = df['Price'].apply(lambda x: float(x))
df['Reviews']= df['Reviews'].apply(lambda
x: int(x))
# %%
plt.figure(figsize=(15,10))
g=sns.countplot(x="Category",data=df, palette = "Set1")
g.set_xticklabels(g.get_xticklabels(), rotation=90, ha="right")
plt.savefig('CountApps.png', dpi=1000)
plt.show()
# %%
x = df['Rating'].dropna()
y = df['Size'].dropna()
z = df['Installs'][df.Installs!=0].dropna()
p = df['Reviews'][df.Reviews!=0].dropna()
t = df['Type'].dropna()
price = df['Price']
p= sns.pairplot(pd.DataFrame(list(zip(x, y, np.log(z), np.log10(p), t, price)),
columns=['Rating','Size', 'Installs', 'Reviews', 'Type', 'Price']), hue='Type', palette="Set2")
plt.savefig('relation.png', dpi=300)
plt.show()
# %%
plt.figure(figsize=(10,10))
sns.boxplot(x="Type", y="Rating", hue="ContentRating", data=df, palette="PRGn")
plt.savefig('box.png', dpi=600)
plt.show()
# %%
subset_df= df[df.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE','LIFESTYLE','BUSINESS'])]
sns.set_style('darkgrid')
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
p = sns.stripplot(x="Price", y="Category", data=subset_df, jitter=True, linewidth=1)
#title = ax.set_title('不同类别的App的价格趋势',size = 25)
plt.savefig('不同类别的App的价格趋势.png', dpi=300)
plt.show()
# %%
df[['Category', 'App']][df.Price > 200]
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
subset_df_price= subset_df[subset_df.Price<100]
p = sns.stripplot(x="Price", y="Category", data=subset_df_price, jitter=True, linewidth=1)
plt.savefig('Price.png', dpi=300)
plt.show()
# %%
