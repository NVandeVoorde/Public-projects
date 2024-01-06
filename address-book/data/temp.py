import pandas as pd

temp_data = pd.read_csv('C:/Users/vandevnj/Documents/Personal/Projecten/Public-projects/address-book/data/georef-belgium-postal-codes.csv', sep = ';')


#do stuff
# Maybe try to access it directly from source? 

temp_data.to_csv('data/temp.csv', sep = ';', header = True)