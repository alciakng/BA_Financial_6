from datetime import datetime
from matplotlib import ticker
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import squarify  as squarify# 트리맵용
import os

# 모든컬럼 확인 옵션 
pd.set_option('display.max_columns', None) 

df_차주 = pd.read_csv("./dataset/차주정보.csv")
df_기업개요정보 = pd.read_csv("./dataset/기업개요정보.csv")
df_연체정보_신용도판단정보= pd.read_csv("./dataset/연체정보(신용도판단정보).csv")
df_연체정보_공공정보 = pd.read_csv("./dataset/연체정보(공공정보).csv")
df_개인대출정보_금융권 = pd.read_csv("./dataset/개인대출정보(금융권).csv")
df_개인대출정보_대부업권 = pd.read_csv("./dataset/개인대출정보(대부업).csv")
df_신용카드개설정보 = pd.read_csv("./dataset/신용카드개설정보.csv")
df_신용카드이용정보 = pd.read_csv("./dataset/신용카드이용정보.csv")
df_채무보증정보 = pd.read_csv("./dataset/채무보증정보.csv")
df_기업대출정보 = pd.read_csv("./dataset/기업대출정보.csv")
df_기술신용평가정보 = pd.read_csv("./dataset/기술신용평가정보.csv")
df_기업개요정보기술신용대출정보 = pd.read_csv("./dataset/기술신용대출정보.csv")
df_보험계약관계자정보 = pd.read_csv("./dataset/보험계약관계자정보.csv")
df_보험계약정보 = pd.read_csv("./dataset/보험계약정보.csv")
df_보험담보정보 = pd.read_csv("./dataset/보험담보정보.csv")
df_청구사고정보 = pd.read_csv("./dataset/청구사고정보.csv")
df_청구계약정보 = pd.read_csv("./dataset/청구계약정보.csv")
df_청구지급사유정보 = pd.read_csv("./dataset/청구지급사유정보.csv")
df_청구지급상세사유정보 = pd.read_csv("./dataset/청구지급상세사유정보.csv")
df_청구피해자물정보 = pd.read_csv("./dataset/청구피해자물정보.csv")


# 한국표준산업분류(KIC) 10차 코드 
url = 'https://github.com/FinanceData/KSIC/raw/master/KSIC_10.csv.gz'
df_ksic = pd.read_csv(url, dtype='str')
df_ksic['Industy_code'] = df_ksic['Industy_code'].str.pad(width=5, side='right', fillchar='0')
df_ksic['Industy_code'] = df_ksic['Industy_code'].str[:4]
df_ksic.rename(columns={'Industy_code': 'BIZ_TYP_CD'}, inplace=True)
df_ksic.rename(columns={'Industy_name': 'BIZ_TYP_NM'}, inplace=True)
df_ksic.head(100)
df_ksic.info()

############################################################
# Section1. 기업개요정보 파악
#  0. 각 데이터 프레임 결측치 파악
#  1. 차주-기업개요정보 (1:n) 병합처리 
#  2. 개인사업자 필터링, 소상공인 필터링(유의한 변수없음.교수님께 질의필요)
#  3. 연령 구간화 (0 : ~19 1: 19~34 2: 35~50 3: 51~64 4: 65~)
#  4. 한국표준산업분류(KIC) 10차코드로 업종명 매핑(현재 모의데이터 업종코드는 비정상적)
#  5. 시각화
#    - 차주 한명당 업체개수 - 건수 시각화
#    - 업종 - 연령별 건수 막대그래프
#    - 연령대별 업종 분포 시각화 
############################################################

# ------------------------------
# 0. 결측치파악 => 결측치 존재하지 않음 
# ------------------------------
print(df_차주.info())
print(df_기업개요정보.info())

# -----------------------------
# 1. 차주-기업개요정보 (1:n) 병합처리
# -----------------------------
df_차주_기업개요정보 = df_기업개요정보.merge(df_차주, on=['JOIN_SN','JOIN_SN_TYP'], how='left')

# -------------------------------------------------------
# 2. 개인사업자 필터링, 소상공인 필터링(유의한 변수없음.교수님께 질의필요)
# -------------------------------------------------------
df_차주_기업개요정보 = df_차주_기업개요정보[df_차주_기업개요정보["JOIN_SN_TYP"] ==1]
df_차주_기업개요정보.info()

# -----------
# 3. 연령구간화 
# -----------
bins = [-1, 19, 34, 50, 64, 150]  # 각 구간의 경계값
labels = ["~19","~34","~50","~64","65~"]          # 구간에 매길 값

df_차주_기업개요정보['BTH_SECTION'] = pd.cut(datetime.now().year - df_차주_기업개요정보['BTH_YR'], bins=bins, labels=labels)

df_차주_연령구간화 = df_차주.copy()
df_차주_연령구간화['BTH_SECTION'] = pd.cut(datetime.now().year - df_차주['BTH_YR'], bins=bins, labels=labels)


# ---------------------------------------------------
# 4. 10차 코드로 업종명 매핑 (현재 모의데이터셋 불완전하여 매핑안됨)
# ---------------------------------------------------
#df_차주_기업개요정보['BIZ_TYP_CD'] = df_차주_기업개요정보['BIZ_TYP_CD'].astype(object)
#df_차주_기업개요정보 = df_차주_기업개요정보.merge(df_ksic,on="BIZ_TYP_CD", how='left')

# ---------------------------
# 5. 시각화를 위한 Summary df 생성
# ---------------------------
df_차주_기업개요정보_Summary = df_차주_기업개요정보.groupby('JOIN_SN')['BIZ_SN'].nunique().reset_index(name='BIZ_COUNT')
df_차주_기업개요정보_Summary = df_차주_기업개요정보_Summary.groupby('BIZ_COUNT')["JOIN_SN"].count().reset_index(name='COUNT')

df_차주_기업개요정보_Summary['BIZ_COUNT'] = df_차주_기업개요정보_Summary['BIZ_COUNT'].astype(str)
df_차주_기업개요정보_Summary['BIZ_COUNT'] = df_차주_기업개요정보_Summary['BIZ_COUNT']


df_차주_기업개요정보_Summary.head()

#############################################################################
# Section2. 기업대출 및 연체규모 파악
#  0. 각 데이터 프레임 결측치 파악
#  1. 병합 
#    - 1-1) 금융권+대부업권 대출정보 병합 후 기업대출정보와 동일 컬럼기준으로 병합
#    - 1-2) 차주+대출정보 병합
#    - 1-3) 신용도판단정보+공공정보 연체정보 병합
#    - 1-4) 대출정보+신용카드이용정보 통합 
#    - 1-5) 대출신용카드이용정보 + 연체정보 통합
#    - 1-6) 차주 + 대출신용카드연체정보 통합
#  2. 시각화 
#    - 2-1) 차입자의 대출 보유수 파이플롯 시각화
#    - 2-2) 평균대출금액 박스플롯 시각화, 연령별 금액 히스토그램 시각화
#    - 2-3) 연령구간별 대출금액 분포 트리맵 시각화, 박스플롯 시각화
#    - 2-4) 연령별 연체율 박스플롯시각화 - 평균연체율 표시
#    - 2-5) 연령별 차주의 연체율, 전체 평균연체율 대비 시각화 
#    - 2-6) 차주의 연체금액/대출금액, 연체건수/기관건수=연체율을 비교시각화
############################################################################

################################
# 0. 결측치파악 => 결측치 존재하지 않음 
################################

#대출정보(병합대상)
print(df_개인대출정보_금융권.info())
print(df_개인대출정보_대부업권.info())
print(df_기업대출정보.info())

#연체정보(병합대상)
print(df_연체정보_신용도판단정보.info())
print(df_연체정보_공공정보.info())

print(df_신용카드개설정보.info())

# ==============================
# 1. 병합
# ==============================

# ---------------------------
# 1-1) 금융권+대부업권 대출정보 병합 
# ---------------------------

df_개인대출정보 = pd.concat([df_개인대출정보_금융권, df_개인대출정보_대부업권], ignore_index=True)
# 구분컬럼추가 
df_개인대출정보["기업개인구분"] = "개인"
df_기업대출정보["기업개인구분"] = "기업"
# 대출과목코드 일원화(1.개인대출상품코드 스트링 붙이기(LN_CD_1+LN_CD_2+LN_CD_3),2.기업대출과목코드를 개인대출코드로 바꿈)
df_개인대출정보["LN_CD_1"] = df_개인대출정보["LN_CD_1"].astype('str')
df_개인대출정보["LN_CD_2"] = df_개인대출정보["LN_CD_2"].astype('str')
df_개인대출정보["LN_CD_3"] = df_개인대출정보["LN_CD_3"].astype('str')
df_개인대출정보["LN_CD"] = df_개인대출정보["LN_CD_1"]+df_개인대출정보["LN_CD_2"]+df_개인대출정보["LN_CD_3"]
df_기업대출정보.rename(columns={'LN_ACCT_CD': 'LN_CD'}, inplace=True)

# 겹치는 컬럼 파악 
common_cols = list(df_개인대출정보.columns.intersection(df_기업대출정보.columns))
# 해당 컬럼기준으로 개인대출정보+기업대출정보 병합 
df_대출정보 = pd.concat([df_개인대출정보[common_cols], df_기업대출정보[common_cols]], ignore_index=True)

print(df_대출정보.info())
# 자료의 범위
print(df_대출정보['YM'].min(),df_대출정보['YM'].max())

# ---------------------------
# 1-2) 차주+대출집계정보 병합
# ---------------------------

# 대출정보_집계
df_대출정보_보유기관_집계 = df_대출정보.groupby(['JOIN_SN','YM'])['COM_SN'].count().reset_index(name='COM_SN_COUNT')
df_대출정보_대출과목_집계 = df_대출정보.groupby(['JOIN_SN','YM'])['LN_CD'].count().reset_index(name='LN_CD_COUNT')

# 차주의 월별 집계치 중 min(), max() 건수를 기준으로 새로운 데이터 프레임 생성 
df_대출정보_보유기관_집계=df_대출정보_보유기관_집계.groupby('JOIN_SN')['COM_SN_COUNT'].agg(최소보유건수='min', 최대보유건수='max').reset_index()
df_대출정보_대출과목_집계=df_대출정보_대출과목_집계.groupby('JOIN_SN')['LN_CD_COUNT'].agg(최소대출건수='min', 최대대출건수='max').reset_index()

# 집계정보통합 
df_대출정보_집계 = pd.merge(df_대출정보_보유기관_집계, df_대출정보_대출과목_집계, on='JOIN_SN', how='inner')
df_대출정보_집계.head(100)

df_차주_기업개요정보.head(100)

# 차주+집계정보 병합
df_차주_대출정보_집계 = df_차주.merge(df_대출정보_집계,on='JOIN_SN',how='left')


df_차주_대출정보_집계[['최소보유건수','최대보유건수','최소대출건수','최대대출건수']] = df_차주_대출정보_집계[['최소보유건수','최대보유건수','최소대출건수','최대대출건수']].fillna(0)
####################차주+대출정보 집계 테이블 완성#######################

# ---------------------------
# 1-3) 신용도판단정보+공공정보 병합 
# ---------------------------

df_연체정보_신용도판단정보["민간공공구분"] = "민간"
df_연체정보_공공정보["민간공공구분"] ="공공"
# 연체정보 통합 
df_연체정보 = pd.concat([df_연체정보_신용도판단정보, df_연체정보_공공정보], ignore_index=True)


df_연체정보.groupby(['JOIN_SN', 'COM_SN'])['RLS_DT'].count().to_csv()

df_연체정보[df_연체정보['JOIN_SN']==8318].to_csv()

# 기관별 마지막월의 연체정보만을 본다(해제된것 포함)
df_연체정보_기관별_최종  = (
    df_연체정보.sort_values(['YM'],ascending=True) 
      .groupby(['JOIN_SN', 'COM_SN'], as_index=False)  # 그룹핑
      .tail(1)  # 각 그룹에서 마지막 row (최신 월)
)

# --------------------------------------------------------------------
# 1-4) 대출정보+신용카드이용정보 통합
# --------------------------------------------------------------------
df_대출정보.info()
df_신용카드이용정보.info()

# 대출정보와 신용카드 이용정보의 금액을 같은이름으로 통일 
df_대출정보_AMT= df_대출정보.rename(columns={'LN_AMT': 'AMT'})
df_신용카드이용정보_AMT= df_신용카드이용정보.copy()
df_신용카드이용정보_AMT['AMT'] = df_신용카드이용정보['CD_USG_AMT']+ df_신용카드이용정보['CD_CA_AMT'] # 신용카드 이용금액+신용카드론 이용금액 합산

# 구분컬럼 생성 
df_대출정보_AMT['대출신용카드구분'] = '대출'
df_신용카드이용정보_AMT['대출신용카드구분'] = '신용'

# 겹치는 컬럼 파악 
common_cols = list(df_대출정보_AMT.columns.intersection(df_신용카드이용정보_AMT.columns))

# 해당 컬럼기준으로 대출정보+신용카드 이용정보 병합 
df_대출_신용카드_병합 = pd.concat([df_대출정보_AMT[common_cols], df_신용카드이용정보_AMT[common_cols]], ignore_index=True)

# 기관별 마지막 월을 기준으로 차주의 대출,신용카드 금액만을 남긴다.
df_대출_신용카드_병합_기관별_최종  = (
    df_대출_신용카드_병합.sort_values(['YM'],ascending=True)  # 월 오름차순 정렬
      .groupby(['JOIN_SN', 'COM_SN', '대출신용카드구분'], as_index=False)  # 그룹핑
      .tail(1)  # 각 그룹에서 마지막 row (최신 월)
)


# --------------------------------------------------------------------
# 1-5) 대출신용카드이용정보 + 연체정보 통합
# --------------------------------------------------------------------
df_대출_신용카드_병합_기관별_최종.info()
df_연체정보_기관별_최종.info()

df_연체정보_기관별_최종[['JOIN_SN','JOIN_SN_TYP','COM_SN','DLQ_RGST_AMT','DLQ_AMT']]


df_대출_신용카드_연체정보 = pd.merge(df_대출_신용카드_병합_기관별_최종,df_연체정보_기관별_최종[['JOIN_SN','JOIN_SN_TYP','COM_SN','DLQ_RGST_AMT','DLQ_AMT']],on=['JOIN_SN','JOIN_SN_TYP','COM_SN'],how='left')

df_대출_신용카드_연체정보.info() 
# --------------------------------------------------------------------
# 1-6) 차주 + 대출신용카드연체정보 통합
# --------------------------------------------------------------------
df_차주_대출_신용카드_연체정보 = pd.merge(df_차주, df_대출_신용카드_연체정보,on=['JOIN_SN','JOIN_SN_TYP'],how='left')
df_차주_대출_신용카드_연체정보.info()


df_차주_대출_신용카드_연체정보[['YM','SCTR_CD','COM_SN','IS_ME','AMT','DLQ_RGST_AMT','DLQ_AMT']] = df_차주_대출_신용카드_연체정보[['YM','SCTR_CD','COM_SN','IS_ME','AMT','DLQ_RGST_AMT','DLQ_AMT']].fillna(0)

df_차주_대출_신용카드_연체정보['대출신용카드구분'].fillna('미보유',inplace=True)

# ==============================
# 2. 시각화 
# ==============================

# 2-1) 차입자의 대출 보유수 파이플롯 시각화
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot()

df_차주_기업개요정보_Summary.info()
ax.pie(df_차주_기업개요정보_Summary['COUNT'],
    labels=df_차주_기업개요정보_Summary['BIZ_COUNT'],
    startangle=0,
    counterclock=False,
    autopct=lambda p :'{:.1f}%'.format(p))

plt.legend(title='Number of businesses operating by person')
plt.show()

# 2-2) 평균대출금액 박스플롯 시각화, 연령별 금액 히스토그램 시각화
df_차주_대출_신용카드_연체정보.info()
df_차주_대출_신용카드_연체정보_소액 = df_차주_대출_신용카드_연체정보[(df_차주_대출_신용카드_연체정보['AMT'] <= 50000) & (df_차주_대출_신용카드_연체정보['대출신용카드구분']=='대출')]
df_차주_대출_신용카드_연체정보_그외 = df_차주_대출_신용카드_연체정보[(df_차주_대출_신용카드_연체정보['AMT'] > 50000) & (df_차주_대출_신용카드_연체정보['대출신용카드구분']=='대출')]

# 5천만원 이하 소액 
plt.figure(figsize=(8,5))
plt.ticklabel_format(style='plain', axis='y')
plt.xlabel('Group of Age')
plt.ylabel('Amount')
plt.title('Distribution of loan amount by age group(Sole Proprietorship)')
ax = sns.boxplot(x="BTH_SECTION",y="AMT", data=df_차주_대출_신용카드_연체정보_소액, palette='Set2')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.tight_layout()
plt.show()

# 5천만원 초과 그외 
plt.figure(figsize=(8,5))
plt.ticklabel_format(style='plain', axis='y')
plt.xlabel('Group of Age')
plt.ylabel('Amount')
plt.title('Distribution of loan amount by age group(Sole Proprietorship)')
ax = sns.boxplot(x="BTH_SECTION",y="AMT", data=df_차주_대출_신용카드_연체정보_그외, palette='Set2')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.tight_layout()
plt.show()


"""
df_34 = df_차주_대출_신용카드_연체정보_그외[df_차주_대출_신용카드_연체정보_그외['BTH_SECTION'] == "~34"]
df_34 = df_34[['AMT']]
df_50 = df_차주_대출_신용카드_연체정보_그외[df_차주_대출_신용카드_연체정보_그외['BTH_SECTION'] == "~50"]
df_50 = df_34[['AMT']]
df_64 = df_차주_대출_신용카드_연체정보_그외[df_차주_대출_신용카드_연체정보_그외['BTH_SECTION'] == "~64"]
df_64 = df_34[['AMT']]

df_34.head(100)

plt.hist(df_34, color='red', alpah =0.2, bins = 10000000, label ='~34', density=True)
plt.hist(df_50, color='orange', alpah = 0.2, bins = 100000, label ='~50', density=True)
plt.hist(df_64, color='yellow', alpah = 0.2, bins = 100000, label ='~64', density=True)

plt.legend()
plt.show()"
"""

# 2-3) 연령구간별 대출과목 분포 트리맵 시각화


df_개인대출정보_최종  = (
    df_개인대출정보.sort_values(['YM'],ascending=True) 
      .groupby(['JOIN_SN', 'LN_CD_1','LN_CD_2','LN_CD_3'], as_index=False)  # 그룹핑
      .tail(1)  # 각 그룹에서 마지막 row (최신 월)
)

df_개인대출정보_최종.info()
df_차주.info()

df_차주_개인대출정보 = df_차주_연령구간화.merge(df_개인대출정보_최종,on=['JOIN_SN','JOIN_SN_TYP'], how='left')


#그룹화해서 대출금액 합계 계산
df_차주_개인대출정보_집계 = df_차주_개인대출정보.groupby(['BTH_SECTION', 'LN_CD_2'])['LN_AMT'].sum().reset_index()

df_차주_개인대출정보_집계 = df_차주_개인대출정보_집계[df_차주_개인대출정보_집계['LN_AMT'] >0]

# 트리맵용 label + size 구성
df_차주_개인대출정보_집계['label'] = df_차주_개인대출정보_집계['BTH_SECTION'].astype(str) + '\n' + df_차주_개인대출정보_집계['LN_CD_2'] + '\n' + df_차주_개인대출정보_집계['LN_AMT'].astype(str)
labels = df_차주_개인대출정보_집계['label']
sizes = df_차주_개인대출정보_집계['LN_AMT']
colors = sns.color_palette('pastel', len(sizes))


# 트리맵 그리기
plt.figure(figsize=(10, 6))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.axis('off')
plt.title('연령별 · 대출과목별 대출금액 트리맵')
plt.tight_layout()
plt.show()



# 2-4) 연령별 연체율 박스플롯시각화 - 평균연체율 표시



# 2-5) 연령별 차주의 연체율, 전체 평균연체율 대비 시각화
df_차주_대출_신용카드_연체정보_그외.info()


# 2-6) 차주의 연체금액/대출금액, 연체건수/기관건수=연체율을 비교시각화


