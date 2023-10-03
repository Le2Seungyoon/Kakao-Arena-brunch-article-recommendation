# Kakao Arena : brunch article recommendation
EDA의 결과는 ... 
그러므로 ... 


## data setting 
먼저 res 아래에 Kakao Arena : brunch article recommendation의 데이터를 넣습니다.  


## run  
먼저 df.txt 생성  
```
python create_dataset.py
```

그후 main.py 실행 예시는 다음과 같음:  
```
python main.py --dataset=df --train_dir=default
```

## result  
결과를 NDCG으로 ...
상세한 로그는 참고 바람!  

## citation
해당 repository에서 사용된 데이터는 [Kakao](https://www.kakaocorp.com)에서 주최한 Kakao Arena에서 사용된 데이터이며,   
모델인 SASRec의 경우 아래의 논문을 참고했습니다.  
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
