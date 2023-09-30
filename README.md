# Kakao Arena : brunch article recommendation
late submission임을 밝힘  
1위 성적 밝히기  
1위 성적 넘기기 (어떻게든)  
유명 알고리즘들 사용 (시간 우위)  

```
├── res
│   ├── /contents
│   ├── /predict
│   ├── /read
│   ├── magazine.json
│   ├── metadata.json
│   └── users.json
└── tmp
```

## result  
sequential-rec : collaborative filtering  
cold start 문제 해결  
content-based filtering?  
ensemble  

## run  

## evaluate 
```bash
$> python evaluate.py run ./tmp/dev.users.recommend ./tmp/dev --topn=100
```
