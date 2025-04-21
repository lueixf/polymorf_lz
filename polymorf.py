import pandas as pd

class Time:
    def __init__(self):
        self.df = pd.read_csv('var11.csv')

        self.df['Время оплаты'] = self.df['Время оплаты'].str.strip()
        self.df['Время оплаты'] = pd.to_datetime(self.df['Время оплаты'], format='%H:%M:%S', errors='coerce')
        self.df['Время оплаты'] = self.df['Время оплаты'].dt.time

        
    def divide(self):
        normal = self.df[self.df['Время оплаты'].apply(self.is_normal_time)]
        suspicious = self.df[self.df['Время оплаты'].apply(self.is_suspicious_time)]
    

        print(f"Нормальные транзакции: {len(normal)}")
        print(f"Подозрительные транзакции: {len(suspicious)}")
        
        normal.to_csv('normal_transactions.csv', index=False)
        suspicious.to_csv('suspicious_transactions.csv', index=False)

    def is_normal_time(self, time):
        start_time = pd.to_datetime('09:00:00', format='%H:%M:%S').time()
        end_time = pd.to_datetime('23:00:00', format='%H:%M:%S').time()
        return start_time <= time <= end_time

    def is_suspicious_time(self, time):
        return not self.is_normal_time(time)
    
    def __invert__(self):
        self.df_no_duplicates = self.df.drop_duplicates()
        self.a = len(self.df)
        self.b = len(self.df_no_duplicates)
        self.duplicates = self.a - self.b
        print("Кол-во дубликатов - ",self.duplicates )
        self.df_no_duplicates.to_csv('df_no_duplicates.csv', index=False) 

    def __del__(self):
        print('All')

def main():
    t = Time()
    t.divide()
    ~t

if __name__ == "__main__":
    main()