import os
import pandas as pd
import tqdm

# 경로는 ./res로 설정되어 있습니다. 필요시 data_path를 수정하시기 바랍니다.
data_path = './res'

# read에서 데이터를 불러와 dataframe 형태로 구축
def iterate_data_files(from_dtm, to_dtm):
    from_dtm, to_dtm = map(str, [from_dtm, to_dtm])
    read_root = os.path.join(data_path, 'read')
    for fname in os.listdir(read_root):
        if len(fname) != len('2018100100_2018100103'):
            continue
        if from_dtm != 'None' and from_dtm > fname:
            continue
        if to_dtm != 'None' and fname > to_dtm:
            continue
        path = os.path.join(read_root, fname)
        yield path, fname
        
data = [];
 
files = sorted([path for path, _ in iterate_data_files('2018100100', '2019030100')])
 
for path in tqdm.tqdm(files, mininterval=1):
    for line in open(path):
        tokens = line.strip().split()
        read_datetime = path[7:17]
        user_id = tokens[0]
        reads = tokens[1:]
        for item in reads:
            data.append([read_datetime, user_id, item])

read_df = pd.DataFrame(data)
read_df.columns = ['date', 'user_id', 'article_id']
read_df = read_df[['user_id', 'article_id', 'date']]
df = read_df.copy()

# 독립된 user, article id 값들을 각각 수치화
user_set, article_set = set(df['user_id'].unique()), set(df['article_id'].unique())

user_map = dict()
article_map = dict()

for u, user in enumerate(user_set):
    user_map[user] = u+1
for i, item in enumerate(article_set):
    article_map[item] = i+1
    
df["user_id"] = df["user_id"].apply(lambda x: user_map[x])
df["article_id"] = df["article_id"].apply(lambda x: article_map[x])
df = df.sort_values(by=["user_id", "date"])
df.drop(columns=["date"], inplace=True)

# SASRec에서 요구하는 형태로 변환하여 저장
df.to_csv(os.path.join(data_path, 'df.txt'), sep=" ", header=None, index=False)

