import pandas as pd
class Time:
    def __init__(self):
        self.df = pd.read_csv('var11.csv')
       

    def divide(self):
        print (self.df.between_time('9:00', '23:00'))
        print(self.df.between_time('23:00', '9:00'))
        

    def __del__(self):
        print('All')

t = Time()
t.divide()