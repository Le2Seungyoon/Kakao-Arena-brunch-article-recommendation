# Kakao Arena : brunch article recommendation
late submission임을 밝힘  
1위 성적 밝히기?   
1위 성적 넘기기 (어떻게든)  
데이터 경로를 res 아래에 넣기

## result  
sequential-rec : collaborative filtering   

## run  
```
python create_dataset.py
```

## evaluate 
```
python evaluate.py run ./tmp/dev.users.recommend ./tmp/dev --topn=100
```
## to - do  
ensemble
cold-start

## citation
```
@inproceedings{kang2018self,
  title={Self-attentive sequential recommendation},
  author={Kang, Wang-Cheng and McAuley, Julian},
  booktitle={2018 IEEE International Conference on Data Mining (ICDM)},
  pages={197--206},
  year={2018},
  organization={IEEE}
}
```
