import pandas as pd
import os

absolute_path = os.path.dirname(__file__)
inc_data = 'georef-belgium-postal-codes.csv'
out_data = 'temp.csv'

temp_data = pd.read_csv(os.path.join(absolute_path, inc_data), sep = ';')


#do stuff
# Maybe try to access it directly from source? 

temp_data.to_csv(os.path.join(absolute_path, out_data), sep = ';', header = True)