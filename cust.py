import mysql.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
pd.options.plotting.backend = "plotly"


cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='customer')

print(cnx)
db_cursor = cnx.cursor()
db_cursor.execute('''select p.product,c.CustomerName,o.no_of_units,s.value from products p inner join orderedunits o on p.ID=o.unit_id INNER join salesorders s on s.ID=o.order_id INNER JOIN customer c on s.customer_id=c.ID where p.Product='Electric Motor' or p.Product='Tyre';''')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)
df.columns= ["product", "customer_name","no_of_units","values"]
print(df)

#Bar Graph for Customer with the Product Value
fig = px.bar(df, x="customer_name", y="values", height=600, width=600)
fig.show()

# #Bar Graph for Customer with the no of units of a product
# fig2 = px.bar(df, x="customer_name", y="no_of_units", height=600, width=600)
# fig2.show()
#
# # Bar Graph for value with the no of units of a product
# fig3 = px.bar(df, x="value", y="no_of_units", height=600, width=600)
# fig3.show()

cnx.close()
