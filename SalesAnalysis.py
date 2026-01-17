import numpy as np

# Rows = Days, Columns = Products
sales= np.array([
        [200,150,300],
        [220,180,310],
        [210,170,290],
        [230,160,320]
        ])
print("sales Data:\n",sales)

#Total sales per product
product_sales=np.sum(sales,axis=0)
print("Total sales per product:",product_sales)

#Average sales per day
daily_avg=np.mean(sales,axis=1)
print("Average sales per day:",daily_avg)

#overall total sales
print("Overall Sales: ",np.sum(sales))