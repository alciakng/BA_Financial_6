import json
import pandas as pd
import os 

from data_builder import DatasetBuilder
from data_visualizer import DataVisualizer

# 현재 파이썬 파일 기준으로 경로 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(base_dir, 'dataset.json')

# dataset.json 
with open(dataset_path, 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# 데이터셋 빌더 초기화
builder = DatasetBuilder(dataset)
# 시각화클래스 초기화 
visualizer = DataVisualizer()


# 표준업종 10차코드 로드 
builder.load_kic()
# 데이터 로드 
builder.load_data()
# 차주정보병합
builder.merge_borrower()
# 대출정보 및 시각화 병합
builder.merge_loan_credit()

# 시각화1 - 차주 한명당 업체개수


# 시각화2 - 차입자의 대출 보유수 파이플롯 시각화


# 시각화3 - 평균대출금액 박스플롯 시각화, 연령별 금액 히스토그램 시각화


# 시각화4 - 연령구간별 대출금액 분포 트리맵 시각화, 박스플롯 시각화


# 시각화5 - 연령별 연체율 박스플롯시각화 - 평균연체율 표시


# 시각화6 - 연령별 차주의 연체율, 전체 평균연체율 대비 시각화 


# 시각화7 차주의 연체금액/대출금액, 연체건수/기관건수=연체율을 비교시각화