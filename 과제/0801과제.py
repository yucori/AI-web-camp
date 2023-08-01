import pandas as pd
csv_data = pd.read_csv('./과제/my_data.csv')
#print("\nCSV 파일로부터 읽은 데이터: \n")
#print(csv_data)

csv_data.rename(columns={csv_data.columns[0]:'indexed'}, inplace=True)
csv_data = csv_data.drop('indexed', axis=1) #2차원 배열에서 axis=0은 행, axis=1은 열을 뜻함
csv_data['name'] = ['앨리스', '밥', '찰리', '제임스', '앨리스', '밥', '찰리', '제임스']
csv_data['salary'] = csv_data['salary'].map('{:,d}'.format)
#print(csv_data)

csv_data.to_csv('./과제/my_data_modified.csv', index=False)