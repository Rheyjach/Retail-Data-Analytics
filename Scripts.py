#modulos utilizados
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#lectura de archivos
#stores=pd.read_csv("stores data-set.csv",sep=",")
#sales=pd.read_excel("sales data-set.xlsx")
#features=pd.read_excel("Features data set.xlsx")


#Limpieza de datos
"""null_stores=stores.isnull().sum()
duplicated_stores=stores.duplicated(subset=["Store"],keep=False).sum()"""


"""sales=sales.drop(columns=["Dept","IsHoliday"],axis=1)
sales['Sales_Week_Date'] = pd.to_datetime(sales['Sales_Week_Date'])
null_sales=sales.isnull().sum()
sales=sales.groupby(["Store","Sales_Week_Date"])["Weekly_Sales"].sum().reset_index()
duplicated_sales=sales.duplicated(subset=["Store","Sales_Week_Date"],keep=False).sum()"""

"""null_features=features.isnull().sum()
features['Sales_Week_Date'] = pd.to_datetime(features['Sales_Week_Date'])
features[['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']]=features[['MarkDown1', 'MarkDown2',
                                                                                       'MarkDown3', 'MarkDown4', 'MarkDown5']].fillna(0)
duplicated_features=features.duplicated(subset=["Store","Sales_Week_Date"],keep=False).sum()"""


#Union de tablas

"""sales_features = pd.merge(sales, features, on=['Store', 'Sales_Week_Date'], how='inner')
final_data = pd.merge(sales_features, stores, on='Store', how='inner')
duplicated_final_datas=final_data.duplicated(subset=['Store', 'Sales_Week_Date'],keep=False).sum()"""

#Tabla final para el analisis
final_data=pd.read_excel("final_data.xlsx")

#Analisis explorativo
"""exploration_final_data=final_data.describe(include=[int,float])
exploration_final_data.to_excel("exploration.xlsx",index=False)"""

#final_data['MarkDown2']=final_data['MarkDown2'].apply(lambda x:0 if x <0 else x)
#final_data['MarkDown3']=final_data['MarkDown3'].apply(lambda x:0 if x <0 else x)


"""plt.figure(figsize=(8, 6))
sns.boxplot(data=final_data[['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']])
plt.title('MarkDowns Distribution')
plt.show()"""

"""final_data['Weekly_Sales'].hist(bins=30)
plt.title('Weekly Sales Distribution')
plt.xlabel('Weekly Sales')
plt.ylabel('Frequency')
plt.show()"""

"""final_data["IsHoliday"]=final_data["IsHoliday"].astype(int)
selectionData=final_data.select_dtypes(include=["int","float"])
Correlation_matrix = selectionData.corr()
CorrelationWeekly_Sales=Correlation_matrix["Weekly_Sales"].reset_index(name="Weekly_Sales")
positive_correlation=CorrelationWeekly_Sales[CorrelationWeekly_Sales["Weekly_Sales"]>0].sort_values(by="Weekly_Sales",ascending=False)
negative_correlation=CorrelationWeekly_Sales[CorrelationWeekly_Sales["Weekly_Sales"]<=0].sort_values(by="Weekly_Sales").reset_index(drop=True)

positive_correlation.to_excel("exploration.xlsx",index=False)"""


#Elaboracion de graficos de tendencias
"""plt.figure(figsize=(12, 8))
sns.heatmap(correlacion_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlación entre variables')
plt.show()"""

# ['Store', 'Sales_Week_Date', 'Weekly_Sales', 'Temperature', 'Fuel_Price',
# 'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI',
# 'Unemployment', 'IsHoliday', 'Store_Type', 'Size']

"""for column in ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment','MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5','Size']:
    plt.figure()
    sns.scatterplot(data=final_data, x=column, y='Weekly_Sales')
    plt.title(f'Relationship between {column} and Weekly Sales', fontsize=18)
    plt.xlabel(column, fontsize=14)  
    plt.ylabel('Weekly Sales', fontsize=14)  
    plt.xticks(fontsize=11)  
    plt.yticks(fontsize=12) 
    plt.show()"""



"""holiday_sales = final_data.groupby('IsHoliday')['Weekly_Sales'].mean()
holiday_sales.plot(kind='bar')
plt.title('Average Sales: Holidays and Non-Holidays')
plt.xlabel('Is it a holiday?')
plt.ylabel('Average Sales')
plt.show()"""

"""sales_by_date = final_data.groupby('Sales_Week_Date')['Weekly_Sales'].sum()
sales_by_date.plot(figsize=(12, 6))
plt.title('Weekly Sales Trend Over Time')
plt.xlabel('Date',fontsize=14)
plt.ylabel('Total Sales',fontsize=14)
plt.xticks(fontsize=11)  
plt.yticks(fontsize=12)
plt.show()"""

"""storeType_Sales=final_data.groupby("Store_Type")["Weekly_Sales"].mean()
storeType_Sales.plot(kind='bar')
plt.title('Average sales: Store type')
plt.xlabel('Store_Type')
plt.ylabel('Average Sales')
plt.show()"""

"""def Capacity_Type(x):
    if x < 80000:
        return 'Small'
    elif x > 160000:
        return 'Large'
    else:
        return 'Medium'


final_data['Capacity_Type']=final_data["Size"].apply(Capacity_Type)
sales_by_Capacity=final_data.groupby("Capacity_Type")["Weekly_Sales"].mean()
sales_by_Capacity.plot(kind='bar')
plt.title('Average sales: Store capacity')
plt.xlabel('Store capacity',fontsize=10)
plt.ylabel('Average Sales',fontsize=10)
plt.xticks(fontsize=7)  
plt.yticks(fontsize=10)
plt.show()"""


isholiday_mardowns=final_data.groupby("IsHoliday")[['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']].mean()
isholiday_mardowns.plot(kind="bar")
plt.title('Average Markdowns: It is a holiday vs It is not a holiday')
plt.xlabel('is it a holiday?')
plt.ylabel('Average Markdowns')
plt.show()





