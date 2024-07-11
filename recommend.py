import joblib
import pandas as pd

# # 모델과 LabelEncoder 불러오기
# loaded_model = joblib.load('random_forest_model.pkl')
# loaded_le = joblib.load('label_encoder.pkl')

import pickle

# 모델 불러오기
with open('random_forest_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# LabelEncoder 불러오기
with open('label_encoder.pkl', 'rb') as le_file:
    loaded_le = pickle.load(le_file)

# 새로운 데이터 예시
new_data = pd.DataFrame([{
  "쇼핑": 0.36,
  "쇼핑_weight": 0.35,
  "배달": 0.14,
  "배달_weight": 0.83,
  "오락": 0.06,
  "오락_weight": 0.7,
  "술": 0.10,
  "술_weight": 0.3,
  "야식": 0.07,
  "야식_weight": 0.9,
  "카페": 0.06,
  "카페_weight": 0.8,
  "구독서비스": 0.02,
  "구독서비스_weight": 0.1,
  "택시": 0.013,
  "택시_weight": 0.0
}])

# 예측
predicted_label = loaded_model.predict(new_data)
predicted_label_name = loaded_le.inverse_transform(predicted_label)
print(predicted_label_name)
