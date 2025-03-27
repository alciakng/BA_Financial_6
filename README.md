# 📊 BA_Finance_6

- 금융 데이터 기반 분석 프로젝트입니다.  
- 차주, 대출, 신용카드, 연체정보 등의 다양한 데이터셋을 통합하고 시각화하여 인사이트를 도출합니다.
- 소상공인 금융포용정책(정책자금, 새출발기금) 이후 연체율을 예측합니다.
- 연체율 중 도덕적해이 연체율을 구분하여 금융포용정책의 실행력을 제고하는 데 목적이 있습니다.
- 도덕적해이 연체율을 파악하여 대안신용평가 모델을 제시합니다.

---

## 📁 프로젝트 구성

<img width="197" alt="image" src="https://github.com/user-attachments/assets/410e289d-f095-470c-aa18-ad5773fac7bb" />

<pre> 📦 BA_Finance_6 ├── 📁 dataset/ # 원본 데이터 CSV 파일들 │ ├── 차주정보.csv │ ├── 개인대출정보.csv │ └── ... 기타 데이터셋 ├── 📄 common_code.py # 공통 코드 static 클래스 정의 ├── 📄 data_builder.py # 데이터 로딩 및 병합 클래스 ├── 📄 data_visualizer.py # 시각화 전용 클래스 ├── 📄 main.py # 메인 실행 파일 └── 📄 README.md # 프로젝트 설명 파일 </pre>

- 데이터셋은 보안상 repository에 올리지 않습니다.
- 신용정보원 AI 학습장(https://ailp.kcredit.or.kr:3446/frt/main.do) 에서 모의데이터를 신청하여 사용가능합니다.

### 1. `dataset/`
- 차주, 대출, 신용카드, 연체정보 등 다양한 금융 데이터셋이 저장된 폴더입니다.
- 원시 CSV 또는 전처리된 파일들이 포함됩니다.

### 2. `common_code.py`
- 공통 코드 테이블(LN_ACCT_CD, LN_CD_1 등)을 포함한 **static 클래스** 정의 파일입니다.

### 3. `data_builder.py`
- `dataset` 폴더에 있는 데이터를 로드하고, 필요한 컬럼을 기준으로 병합하여 **분석용 DataFrame**을 생성하는 역할을 합니다.

### 4. `data_visualizer.py`
- 시각화를 담당하는 클래스입니다.
- seaborn, matplotlib 기반 다양한 그래프 (막대그래프, 박스플롯, 트리맵 등) 를 생성합니다.

### 5. `main.py`
- 이 프로젝트의 **메인 실행 파일**입니다.
- 위의 클래스들을 조합하여 전체 분석 파이프라인을 실행합니다.

---

## 🔧 의존 라이브러리
pandas, matplotlib, seaborn, matplotlib.pyplot

---

## 테이블 ERD 모델링 
![ERD 모델링](https://github.com/user-attachments/assets/a17dbd44-6ce3-48ad-b76a-077e48b80de8)

