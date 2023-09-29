# Kakao Arena : brunch article recommendation
late submission임을 밝힘  
1위 성적 밝히기  
1위 성적 넘기기 (어떻게든)  
유명 알고리즘들 사용 (시간 우위)  

```bash
$> tree -d
.
├── res
│   ├── contents
│   ├── predict
│   ├── read
│   ├── magazine.json
│   ├── metadata.json
│   └── users.json
└── tmp
```

## result  

## run  

## evaluate 
train 데이터와 test 데이터를 나누기 위해 아래와 같이 실행합니다.(,dev를 test로 바꾸기)   
```bash
$> python database.py groupby 2018100100 2019022200 ./tmp/ ./tmp/train
$> python database.py groupby 2019022200 2019030100 ./tmp/ ./tmp/dev
```

```bash
$> python evaluate.py run ./tmp/dev.users.recommend ./tmp/dev --topn=100
```
