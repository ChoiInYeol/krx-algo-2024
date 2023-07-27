#RMSE는 예측값과 실제 값 간의 차이를 제곱하여 평균을 낸 후, 그 결과의 제곱근을 구하는 방식으로 계산됩니다. RMSE 값이 작을수록 예측이 정확하다는 것을 의미합니다.
#평균 절대 오차(Mean Absolute Error, MAE) 또한 유사성을 판단하는 데 사용할 수 있습니다. MAE는 예측값과 실제 값의 차이의 절대값을 평균한 값입니다.
#결정 계수(R-squared, R^2) 는 예측값이 실제 값에 얼마나 가까운지를 나타내는 통계적 척도입니다. R^2 값이 1에 가까울수록 예측이 실제 값을 잘 설명하고 있다는 것을 의미합니다.

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# 실제 종가 데이터
file_dir = "C:\Users\82107\OneDrive - 경희대학교\빅데이터응용학과\KRX 박재균/KRX 평가용.csv" # 여기에 csv 경로 입력
df_actual = pd.read_csv(file_dir)
df_actual['일자'] = pd.to_datetime(df_actual['일자'].astype(str))
df_actual_20230621 = df_actual[df_actual['일자'] == '2023-06-21']

# 예측 종가 데이터
df_predicted = pd.read_csv('/mnt/data/predicted_prices.csv')
df_predicted['일자'] = pd.to_datetime(df_predicted['일자'].astype(str))
df_predicted_20230621 = df_predicted[df_predicted['일자'] == '2023-06-21']

# RMSE 계산
rmse = np.sqrt(mean_squared_error(df_actual_20230621['종가'], df_predicted_20230621['종가']))

# MAE 계산
mae = mean_absolute_error(df_actual_20230621['종가'], df_predicted_20230621['종가'])

# R^2 계산
r2 = r2_score(df_actual_20230621['종가'], df_predicted_20230621['종가'])


print(rmse, mae, r2)