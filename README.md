# krx-algo-2024

제2회 KRX 주식 투자 알고리즘 경진대회용 실험 저장소입니다. KRX 종목별 일별 가격 데이터에 거시 변수, 시가총액, 가치지표를 결합하고, 기술적 지표와 트리 기반 회귀 모델을 이용해 종목 순위를 생성하는 흐름으로 구성되어 있습니다.

## 프로젝트 개요

이 저장소는 다음 작업을 포함합니다.

- KRX 가격 데이터 전처리 및 수정종가 기반 학습 데이터 생성
- 기준금리, CPI, 실업률, 환율 등 외생 변수 결합
- 시가총액, BPS, PER, PBR, EPS, DIV, DPS 등 가치지표 결합
- 기술적 지표 생성 및 train/test 데이터 분리
- XGBoost 기반 수익률 예측 모델 학습
- 예측값 기반 종목 순위 산출 및 제출 파일 생성
- 제출 결과의 MSE, MAE, R2, Sharpe ratio 평가

## 저장소 구조

```text
.
├── 1. 수정종가+종목명.ipynb
├── 2. 의사결정나무기반 모델링.ipynb
├── 3. XGBoost_최신.ipynb
├── 모델평가.ipynb
├── requirements.txt
├── data/
│   ├── train.csv
│   ├── train_adj.csv
│   ├── train_additional.csv
│   ├── combined_train_4.csv
│   └── test_future.csv
├── additional_dataset/
│   ├── 가치지표.csv
│   ├── 시가총액.csv
│   └── 외생변수.csv
├── sub/
│   ├── sample_submission.csv
│   ├── model01_281724.csv
│   ├── XGBoost*.csv
│   └── 앙상블_*.csv
├── temp_file/
└── 참고 파일/
```

## 주요 데이터

### `data/train.csv`

대회 기본 학습 데이터입니다. 주요 컬럼은 다음과 같습니다.

- `일자`
- `종목코드`
- `종목명`
- `거래량`
- `시가`
- `고가`
- `저가`
- `종가`

### `data/train_adj.csv`

가격 데이터에 외생 변수와 가치지표를 결합하고 수정종가 처리 여부를 표시한 학습용 데이터입니다.

주요 컬럼:

- `date`, `ticker`, `firm`
- `volume`, `open`, `high`, `low`, `close`
- `rate`, `cpi`, `un_rate`, `fx`
- `cap`, `bps`, `per`, `pbr`, `eps`, `div`, `dps`
- `adjustTrue`

### `data/combined_train_4.csv`

원본 가격 데이터와 `additional_dataset`의 외생 변수, 시가총액, 가치지표를 병합한 데이터입니다.

### `data/test_future.csv`

미래 구간 예측 및 제출 파일 생성을 위한 테스트 데이터입니다.

### `additional_dataset/`

모델 입력 피처 확장을 위한 보조 데이터입니다.

- `외생변수.csv`: 기준금리, CPI, 실업률, 환율
- `시가총액.csv`: 일자별 종목 시가총액
- `가치지표.csv`: BPS, PER, PBR, EPS, DIV, DPS

### `sub/`

제출 및 실험 결과 파일을 저장합니다.

- `sample_submission.csv`: 제출 형식 예시
- `XGBoost*.csv`: XGBoost 실험 결과
- `앙상블_*.csv`: 앙상블 제출 후보

## 노트북 실행 흐름

### 1. `1. 수정종가+종목명.ipynb`

가격 데이터 전처리 노트북입니다.

주요 작업:

- 원본 KRX 가격 데이터 로드
- 종목코드와 종목명 정리
- 수정종가 처리
- 기술적 분석 지표 생성
- 학습/테스트 구간 분리

사용 라이브러리:

- `pandas`
- `numpy`
- `pandas_ta`
- `tqdm`

### 2. `2. 의사결정나무기반 모델링.ipynb`

트리 기반 회귀 모델링 실험 노트북입니다.

주요 작업:

- 전처리된 학습 데이터 로드
- 피처/타깃 구성
- XGBoost 회귀 모델 학습
- 예측 결과를 종목 순위로 변환
- 제출 파일 생성

사용 라이브러리:

- `pandas`
- `numpy`
- `pandas_ta`
- `xgboost.XGBRegressor`

### 3. `3. XGBoost_최신.ipynb`

XGBoost 최신 실험과 파라미터 탐색을 수행하는 노트북입니다.

주요 작업:

- `TimeSeriesSplit` 기반 시계열 교차검증
- `GridSearchCV` 기반 파라미터 탐색
- 병렬 학습 보조를 위한 `joblib` 사용
- 최종 제출 후보 생성

사용 라이브러리:

- `sklearn.model_selection.GridSearchCV`
- `sklearn.model_selection.TimeSeriesSplit`
- `xgboost.XGBRegressor`
- `joblib`

### 4. `모델평가.ipynb`

모델 예측 결과를 평가하는 노트북입니다.

주요 작업:

- 예측 결과와 실제 결과 비교
- MSE, MAE, R2 계산
- 포트폴리오 성과 및 Sharpe ratio 계산
- 제출 후보 간 성능 비교

사용 라이브러리:

- `pandas`
- `numpy`
- `sklearn.metrics`

## 설치

Python 가상환경 사용을 권장합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 요구 패키지

`requirements.txt` 기준 주요 패키지는 다음과 같습니다.

- `pandas`
- `numpy`
- `tqdm`
- `statsmodels`
- `yfinance`
- `seaborn`
- `PyPortfolioOpt`
- `matplotlib`
- `scikit-learn`
- `cvxopt`
- `pandas_ta`
- `xgboost`

일부 딥러닝 실험은 GPU 환경을 전제로 작성되어 있으며, 주석 기준 CUDA 11.1.1 및 cuDNN 8.1.1 환경을 사용했습니다.

## 실행 순서

1. `requirements.txt`를 설치합니다.
2. `data/`와 `additional_dataset/`의 CSV 파일이 존재하는지 확인합니다.
3. `1. 수정종가+종목명.ipynb`를 실행해 수정종가 및 기술적 지표 기반 데이터를 만듭니다.
4. `2. 의사결정나무기반 모델링.ipynb` 또는 `3. XGBoost_최신.ipynb`에서 모델을 학습합니다.
5. 생성된 제출 후보를 `sub/`에 저장합니다.
6. `모델평가.ipynb`에서 예측 성능과 Sharpe ratio를 확인합니다.

## 브랜치 정책

현재 기준 최신 작업 브랜치는 `main`입니다. 과거 저장소의 `master`와 `develop` 이력은 통합되어 있으며, `main`은 대회 종료 시점의 최신 실험 결과를 기준으로 관리합니다.

## 참고

- 이 저장소는 노트북 중심의 실험 저장소입니다.
- 대용량 학습 데이터와 제출 결과가 포함되어 있어 clone 및 checkout 시간이 길 수 있습니다.
- `data/combined_train_4.csv`와 `data/train_adj.csv`는 Git LFS로 관리합니다.
- `data/train.csv`는 약 57MB의 일반 Git 추적 파일입니다. GitHub 권장 용량보다 크므로, 추가 대용량 CSV를 커밋할 때는 LFS 추적 여부를 먼저 확인하세요.
- 일부 노트북 출력에는 과거 로컬 절대경로가 남아 있을 수 있습니다. 새 환경에서 실행할 때는 데이터 경로를 현재 저장소 기준 상대경로로 맞춰 주세요.
- `*.pkl`, 가상환경, 캐시 파일은 `.gitignore`로 제외합니다.
