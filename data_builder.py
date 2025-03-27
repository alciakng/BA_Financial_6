from datetime import datetime
import pandas as pd
import os

class DatasetBuilder:
    def __init__(self,dataset_json):
        
        """
        path_dict: {"차주정보": "차주정보.csv",
                    "기업개요정보": "기업개요정보.csv",
                    "연체정보(신용도판단정보)": "연체정보(신용도판단정보).csv",
                    "연체정보(공공정보)": "연체정보(공공정보).csv",
                    "개인대출정보(금융권)": "개인대출정보(금융권).csv",
                    "개인대출정보(대부업)": "개인대출정보(대부업).csv",
                    "신용카드개설정보": "신용카드개설정보.csv",
                    "신용카드이용정보": "신용카드이용정보.csv",
                    "채무보증정보": "채무보증정보.csv",
                    "기업대출정보": "기업대출정보.csv",
                    "기술신용평가정보": "기술신용평가정보.csv",
                    "기술신용대출정보": "기술신용대출정보.csv",
                    "보험계약관계자정보": "보험계약관계자정보.csv",
                    "보험계약정보": "보험계약정보.csv",
                    "보험담보정보": "보험담보정보.csv",
                    "청구사고정보": "청구사고정보.csv",
                    "청구계약정보": "청구계약정보.csv",
                    "청구지급사유정보": "청구지급사유정보.csv",
                    "청구지급상세사유정보": "청구지급상세사유정보.csv",
                    "청구피해자물정보": "청구피해자물정보.csv"}   
        """
        
        # 기본 데이터셋
        self.dataset_json = dataset_json
        self.df_차주 = None
        self.df_기업개요정보 = None
        self.df_연체정보_신용도판단정보= None
        self.df_연체정보_공공정보 = None
        self.df_개인대출정보_금융권 = None
        self.df_개인대출정보_대부업권 = None
        self.df_신용카드개설정보 = None
        self.df_신용카드이용정보 = None
        self.df_채무보증정보 = None
        self.df_기업대출정보 = None
        self.df_기술신용평가정보 = None
        self.df_기술신용대출정보 = None
        self.df_보험계약관계자정보 = None
        self.df_보험계약정보 = None
        self.df_보험담보정보 = None
        self.df_청구사고정보 = None
        self.df_청구계약정보 = None
        self.df_청구지급사유정보 = None
        self.df_청구지급상세사유정보 = None
        self.df_청구피해자물정보 = None

        # 10차 업종코드
        self.df_ksic = None

        # merge 후 데이터셋
        self.df_차주_기업개요정보_mg = None
        self.df_차주_기업개요정보_집계_mg = None 
        
        self.df_개인대출정보_mg = None
        self.df_대출정보_mg = None
        self.df_차주_기업개요정보_대출정보_집계_mg = None

        self.df_차주_대출_신용카드_연체정보_mg = None
       

    def load_data(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        datset_dir = os.path.join(base_dir, 'dataset')

        self.df_차주 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['차주정보']))  
        self.df_기업개요정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['기업개요정보']))
        self.df_연체정보_신용도판단정보= pd.read_csv(os.path.join(datset_dir, self.dataset_json['연체정보(신용도판단정보)']))
        self.df_연체정보_공공정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['연체정보(공공정보)']))
        self.df_개인대출정보_금융권 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['개인대출정보(금융권)']))
        self.df_개인대출정보_대부업권 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['개인대출정보(대부업)']))
        self.df_신용카드개설정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['신용카드개설정보']))
        self.df_신용카드이용정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['신용카드이용정보']))
        self.df_채무보증정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['채무보증정보']))
        self.df_기업대출정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['기업대출정보']))
        self.df_기술신용평가정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['기술신용평가정보']))
        self.df_기술신용대출정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['기술신용대출정보']))
        self.df_보험계약관계자정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['보험계약관계자정보']))
        self.df_보험계약정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['보험계약정보']))
        self.df_보험담보정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['보험담보정보']))
        self.df_청구사고정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['청구사고정보']))
        self.df_청구계약정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['청구계약정보']))
        self.df_청구지급사유정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['청구지급사유정보']))
        self.df_청구지급상세사유정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['청구지급상세사유정보']))
        self.df_청구피해자물정보 = pd.read_csv(os.path.join(datset_dir, self.dataset_json['청구피해자물정보']))

    ############################################################
    #  함수 : 표준산업분류(KIC) 10차코드 Load 
    ############################################################
    def load_kic(self):
        # 한국표준산업분류(KIC) 10차 코드 
        url = 'https://github.com/FinanceData/KSIC/raw/master/KSIC_10.csv.gz'
        self.df_ksic = pd.read_csv(url, dtype='str')
        self.df_ksic['Industy_code'] = self.df_ksic['Industy_code'].str.pad(width=5, side='right', fillchar='0')
        self.df_ksic['Industy_code'] = self.df_ksic['Industy_code'].str[:4]
        self.df_ksic.rename(columns={'Industy_code': 'BIZ_TYP_CD'}, inplace=True)
        self.df_ksic.rename(columns={'Industy_name': 'BIZ_TYP_NM'}, inplace=True)
        self.df_ksic.head(100)
        self.df_ksic.info()


    ############################################################
    #  함수 : 차주정보 merge - merge_borrower
    #  0. 각 데이터 프레임 결측치 파악
    #  1. 차주-기업개요정보 (1:n) 병합처리 
    #  2. 개인사업자 필터링, 소상공인 필터링(유의한 변수없음.교수님께 질의필요)
    #  3. 연령 구간화 (0 : ~19 1: 19~34 2: 35~50 3: 51~64 4: 65~)
    #  4. 한국표준산업분류(KIC) 10차코드로 업종명 매핑(현재 모의데이터 업종코드는 비정상적)
    ############################################################

    def merge_borrower(self):
        # ------------------------------
        # 0. 결측치파악 => 결측치 존재하지 않음 
        # ------------------------------
        print(self.df_차주.info())
        print(self.df_기업개요정보.info())

        # -----------------------------
        # 1. 차주-기업개요정보 (1:n) 병합처리
        # -----------------------------
        self.df_차주_기업개요정보_mg = self.df_기업개요정보.merge(self.df_차주, on=['JOIN_SN','JOIN_SN_TYP'], how='left')

        # -------------------------------------------------------
        # 2. 개인사업자 필터링, 소상공인 필터링(유의한 변수없음.교수님께 질의필요)
        # -------------------------------------------------------
        self.df_차주_기업개요정보_mg = self.df_차주_기업개요정보_mg[self.df_차주_기업개요정보_mg["JOIN_SN_TYP"] ==1]
        self.df_차주_기업개요정보_mg.info()

        # -----------
        # 3. 연령구간화 
        # -----------
        bins = [-1, 19, 34, 50, 64, 150]  # 각 구간의 경계값
        labels = ["~19","~34","~50","~64","65~"]          # 구간에 매길 값

        self.df_차주_기업개요정보_mg['BTH_SECTION'] = pd.cut(datetime.now().year - self.df_차주_기업개요정보_mg['BTH_YR'], bins=bins, labels=labels)

        # ---------------------------------------------------
        # 4. 10차 코드로 업종명 매핑 (현재 모의데이터셋 불완전하여 매핑안됨)
        # ---------------------------------------------------
        #self.df_차주_기업개요정보_mg['BIZ_TYP_CD'] = self.df_차주_기업개요정보_mg['BIZ_TYP_CD'].astype(object)
        #self.df_차주_기업개요정보_mg = self.df_차주_기업개요정보_mg.merge(self.df_ksic,on="BIZ_TYP_CD", how='left')

        # ---------------------------
        # 5. 시각화를 위한 Summary df 생성
        # ---------------------------
        self.df_차주_기업개요정보_집계_mg  = self.df_차주_기업개요정보_mg.groupby('JOIN_SN')['BIZ_SN'].nunique().reset_index(name='BIZ_COUNT')
        self.df_차주_기업개요정보_집계_mg  = self.df_차주_기업개요정보_집계_mg.groupby('BIZ_COUNT')["JOIN_SN"].count().reset_index(name='COUNT')

        self.df_차주_기업개요정보_집계_mg['BIZ_COUNT'] = self.df_차주_기업개요정보_집계_mg['BIZ_COUNT'].astype(str)

        self.df_차주_기업개요정보_집계_mg.info()

        print("======df_차주_기업개요정보_집계_mg=======")
        print(self.df_차주_기업개요정보_집계_mg.head(100))
        print("====================================")


    ############################################################
    #  함수 : 금융권+대부업권 대출정보 병합
    #  1. 금융권+대부업권 대출정보 병합 
    #  2. 차주+대출집계정보 병합
    #  3. 신용도판단정보+공공정보 병합 
    #  4. 대출정보+신용카드이용정보 통합
    #  5. 대출신용카드이용정보 + 연체정보 통합
    #  6. 차주 + 대출신용카드연체정보 통합
    ############################################################
    def merge_loan_credit(self):
        # ---------------------------
        # 1) 금융권+대부업권 대출정보 병합 
        # ---------------------------
        self.df_개인대출정보_mg = pd.concat([self.df_개인대출정보_금융권, self.df_개인대출정보_대부업권], ignore_index=True)
        # 구분컬럼추가 
        self.df_개인대출정보_mg["기업개인구분"] = "개인"
        self.df_기업대출정보["기업개인구분"] = "기업"
        # 대출과목코드 일원화(1.개인대출상품코드 스트링 붙이기(LN_CD_1+LN_CD_2+LN_CD_3),2.기업대출과목코드를 개인대출코드로 바꿈)
        self.df_개인대출정보_mg["LN_CD_1"] = self.df_개인대출정보_mg["LN_CD_1"].astype('str')
        self.df_개인대출정보_mg["LN_CD_2"] = self.df_개인대출정보_mg["LN_CD_2"].astype('str')
        self.df_개인대출정보_mg["LN_CD_3"] = self.df_개인대출정보_mg["LN_CD_3"].astype('str')
        self.df_개인대출정보_mg["LN_CD"] = self.df_개인대출정보_mg["LN_CD_1"]+self.df_개인대출정보_mg["LN_CD_2"]+self.df_개인대출정보_mg["LN_CD_3"]
        self.df_기업대출정보.rename(columns={'LN_ACCT_CD': 'LN_CD'}, inplace=True)

        # 겹치는 컬럼 파악 
        common_cols = list(self.df_개인대출정보_mg.columns.intersection(self.df_기업대출정보.columns))
        # 해당 컬럼기준으로 개인대출정보+기업대출정보 병합 
        self.df_대출정보_mg = pd.concat([self.df_개인대출정보_mg[common_cols], self.df_기업대출정보[common_cols]], ignore_index=True)

        print(self.df_대출정보_mg.info())
        # 자료의 범위
        print(self.df_대출정보_mg['YM'].min(),self.df_대출정보_mg['YM'].max())

        # ---------------------------
        # 2. 차주+대출집계정보 병합
        # ---------------------------
        # 대출정보_집계
        df_대출정보_보유기관_집계 = self.df_대출정보_mg.groupby(['JOIN_SN','YM'])['COM_SN'].count().reset_index(name='COM_SN_COUNT')
        df_대출정보_대출과목_집계 = self.df_대출정보_mg.groupby(['JOIN_SN','YM'])['LN_CD'].count().reset_index(name='LN_CD_COUNT')

        # 차주의 월별 집계치 중 min(), max() 건수를 기준으로 새로운 데이터 프레임 생성 
        df_대출정보_보유기관_집계=df_대출정보_보유기관_집계.groupby('JOIN_SN')['COM_SN_COUNT'].agg(최소보유건수='min', 최대보유건수='max').reset_index()
        df_대출정보_대출과목_집계=df_대출정보_대출과목_집계.groupby('JOIN_SN')['LN_CD_COUNT'].agg(최소대출건수='min', 최대대출건수='max').reset_index()

        # 집계정보통합 
        df_대출정보_집계 = pd.merge(df_대출정보_보유기관_집계, df_대출정보_대출과목_집계, on='JOIN_SN', how='inner')
        
        print("=========df_대출정보_집계_mg==========")
        print(df_대출정보_집계.head(100))
        print("===================================")

        # 차주+집계정보 병합
        self.df_차주_기업개요정보_대출정보_집계_mg  = self.df_차주_기업개요정보_mg.merge(df_대출정보_집계,on='JOIN_SN',how='left')
        print(self.df_차주_기업개요정보_대출정보_집계_mg.info())
   
        self.df_차주_기업개요정보_대출정보_집계_mg[['최소보유건수','최대보유건수','최소대출건수','최대대출건수']] = self.df_차주_기업개요정보_대출정보_집계_mg[['최소보유건수','최대보유건수','최소대출건수','최대대출건수']].fillna(0)
        # ---------------------------
        # 3. 신용도판단정보+공공정보 병합 
        # ---------------------------
        self.df_연체정보_신용도판단정보["민간공공구분"] = "민간"
        self.df_연체정보_공공정보["민간공공구분"] ="공공"
        # 연체정보 통합 
        df_연체정보 = pd.concat([self.df_연체정보_신용도판단정보, self.df_연체정보_공공정보], ignore_index=True)
        df_연체정보.groupby(['JOIN_SN', 'COM_SN'])['RLS_DT'].count().to_csv()
        df_연체정보[df_연체정보['JOIN_SN']==8318].to_csv()

        # 기관별 마지막월의 연체정보만을 본다(해제된것 포함)
        df_연체정보_기관별_최종  = (
            df_연체정보.sort_values(['YM'],ascending=True) 
            .groupby(['JOIN_SN', 'COM_SN'], as_index=False)  # 그룹핑
            .tail(1)  # 각 그룹에서 마지막 row (최신 월)
        )

        # --------------------------------------------------------------------
        # 4. 대출정보+신용카드이용정보 통합
        # --------------------------------------------------------------------
        self.df_대출정보_mg.info()
        self.df_신용카드이용정보.info()

        # 대출정보와 신용카드 이용정보의 금액을 같은이름으로 통일 
        df_대출정보_AMT= self.df_대출정보_mg.rename(columns={'LN_AMT': 'AMT'})
        df_신용카드이용정보_AMT= self.df_신용카드이용정보.copy()
        df_신용카드이용정보_AMT['AMT'] = self.df_신용카드이용정보['CD_USG_AMT']+ self.df_신용카드이용정보['CD_CA_AMT'] # 신용카드 이용금액+신용카드론 이용금액 합산

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
        # 5. 대출신용카드이용정보 + 연체정보 통합
        # --------------------------------------------------------------------
        df_대출_신용카드_병합_기관별_최종.info()
        df_연체정보_기관별_최종.info()

        df_연체정보_기관별_최종[['JOIN_SN','JOIN_SN_TYP','COM_SN','DLQ_RGST_AMT','DLQ_AMT']]


        df_대출_신용카드_연체정보 = pd.merge(df_대출_신용카드_병합_기관별_최종,df_연체정보_기관별_최종[['JOIN_SN','JOIN_SN_TYP','COM_SN','DLQ_RGST_AMT','DLQ_AMT']],on=['JOIN_SN','JOIN_SN_TYP','COM_SN'],how='left')

        df_대출_신용카드_연체정보.info() 

        # --------------------------------------------------------------------
        # 6. 차주 + 대출신용카드연체정보 통합
        # --------------------------------------------------------------------
        self.df_차주_대출_신용카드_연체정보_mg = pd.merge(self.df_차주_기업개요정보_mg, df_대출_신용카드_연체정보,on=['JOIN_SN','JOIN_SN_TYP'],how='left')
        self.df_차주_대출_신용카드_연체정보_mg.info()

        self.df_차주_대출_신용카드_연체정보_mg[['YM','SCTR_CD','COM_SN','IS_ME','AMT','DLQ_RGST_AMT','DLQ_AMT']] = self.df_차주_대출_신용카드_연체정보_mg[['YM','SCTR_CD','COM_SN','IS_ME','AMT','DLQ_RGST_AMT','DLQ_AMT']].fillna(0)
        self.df_차주_대출_신용카드_연체정보_mg['대출신용카드구분'].fillna('미보유',inplace=True)
        
        print("======df_차주_대출_신용카드_연체정보_mg=======")
        print(self.df_차주_대출_신용카드_연체정보_mg.head(100))
        print("=======================================")


  