# Kakao Arena : brunch article recommendation
문제 정의:  
해당 대회는 과거 데이터를 이용해서 미래의 유저에게 article을 추천하는 문제입니다.  

솔루션:  
이런 데이터의 형태는 한 유저가 article을 열람한 로그 형태, 즉 sequence 데이터라고 볼 수 있습니다.    
이런 sequence 형태의 데이터에서 가장 최근의 행동도 중요하긴 하지만,   
전체의 맥락을 파악하는 것 역시 중요한 요소입니다.   
따라서 attention을 기반으로 전체 맥락을 고려하는 transformer 기반의 모델이 적합하다고 생각해  
SASRec(Self Attentive Sequential Recommendation) 모델을 사용했습니다.  

## data setting 
먼저 res 아래에 Kakao Arena : brunch article recommendation의 데이터를 넣습니다.  

## run  
### df.txt 생성  
먼저 SASRec을 위한 sequential 데이터를 만들기 위해 create_dataset.py를 실행합니다.  
```
python create_dataset.py
```
SASRec에서는 오직 유저의 article 열람 로그만을 사용하기 때문에,  
다른 딥러닝 모델보다 요구되는 데이터의 양이 적어 효율적입니다.  

### 학습 및 추론
그 후 main.py를 실행하여 SASRec의 학습 및 추론을 진행합니다.  
해당 코드의 예시는 아래와 같습니다:   
```
python main.py --dataset=df --train_dir=default
```
--device=cuda로 인수를 설정하면 GPU를 이용해 학습 및 추론 속도를 가속화시킬 수 있습니다.  
또한 학습 및 추론의 결과는 'df_default' 폴더 내부에 저장되며,  
학습된 모델로 추론만 진행을 원하실 경우에는 --inference_only=True로 인수를 설정하시기 바랍니다.  

## result  
|Dataset|NDCG@100|
|---|---|
|Valid|0.84125|
|Test|0.84924|

## hyperparameter setting
hyperparameter를 조절하여 다양한 실험을 진행하기 위해서 configure.py의 내부 값을 변경해주시기 바랍니다.  
result에 해당하는 결과를 얻기 위해 사용한 hyperparameter는 다음과 같습니다:  
|Hyperparameter|Value|
|---|---|
|batch_size|128|
|lr|0.001|
|maxlen|200|
|hidden_units|50|
|num_blocks|2|
|num_epochs|10|
|num_heads|1|
|dropout_rate|0.2|
|l2_emb|0.0|

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
