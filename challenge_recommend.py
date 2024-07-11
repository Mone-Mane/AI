import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pickle


data = [{'쇼핑': 0.35, '쇼핑_weight': 0.91, '배달': 0.146, '배달_weight': 0.48, '오락': 0.056, '오락_weight': 0.33, '술': 0.05, '술_weight': 0.57, '야식': 0.07, '야식_weight': 0.1, '카페': 0.0433, '카페_weight': 0.73, '구독서비스': 0.02, '구독서비스_weight': 0.15, '택시': 0.0133, '택시_weight': 0.02, 'label': '쇼핑 줄이기'},
         {'쇼핑': 0.35, '쇼핑_weight': 0.98, '배달': 0.146, '배달_weight': 0.46, '오락': 0.056, '오락_weight': 0.31, '술': 0.05, '술_weight': 0.65, '야식': 0.07, '야식_weight': 0.13, '카페': 0.0433, '카페_weight': 0.68, '구독서비스': 0.02, '구독서비스_weight': 0.15, '택시': 0.0133, '택시_weight': 0.0, 'label': '쇼핑 줄이기'}, 
         {'쇼핑': 0.35, '쇼핑_weight': 1, '배달': 0.146, '배달_weight': 0.47, '오락': 0.056, '오락_weight': 0.3, '술': 0.05, '술_weight': 0.61, '야식': 0.07, '야식_weight': 0.1, '카페': 0.0433, '카페_weight': 0.71, '구독서비스': 0.02, '구독서비스_weight': 0.14, '택시': 0.0133, '택시_weight': 0, 'label': '쇼핑 줄이기'},
         {'쇼핑': 0.3, '쇼핑_weight': 0.26, '배달': 0.17, '배달_weight': 0.84, '오락': 0.06, '오락_weight': 0.4, '술': 0.055, '술_weight': 0.28, '야식': 0.065, '야식_weight': 0.18, '카페': 0.04, '카페_weight': 0.84, '구독서비스': 0.025, '구독서비스_weight': 0.16, '택시': 0.015, '택시_weight': 0.05, 'label': '배달 덜 먹기'},
         {'쇼핑': 0.3, '쇼핑_weight': 0.3, '배달': 0.17, '배달_weight': 0.81, '오락': 0.06, '오락_weight': 0.43, '술': 0.055, '술_weight': 0.31, '야식': 0.065, '야식_weight': 0.2, '카페': 0.04, '카페_weight': 0.77, '구독서비스': 0.025, '구독서비스_weight': 0.14, '택시': 0.015, '택시_weight': 0.04, 'label': '배달 덜 먹기'}, 
         {'쇼핑': 0.3, '쇼핑_weight': 0.29, '배달': 0.17, '배달_weight': 0.98, '오락': 0.06, '오락_weight': 0.36, '술': 0.055, '술_weight': 0.31, '야식': 0.065, '야식_weight': 0.22, '카페': 0.04, '카페_weight': 0.78, '구독서비스': 0.025, '구독서비스_weight': 0.15, '택시': 0.015, '택시_weight': 0.07, 'label': '배달 덜 먹기'},
         {'쇼핑': 0.4, '쇼핑_weight': 0.54, '배달': 0.14, '배달_weight': 0.28, '오락': 0.065, '오락_weight': 0.8, '술': 0.045, '술_weight': 0.19, '야식': 0.075, '야식_weight': 0.29, '카페': 0.045, '카페_weight': 0.3, '구독서비스': 0.03, '구독서비스_weight': 0.11, '택시': 0.01, '택시_weight': 0, 'label': '오락 줄이기'},
         {'쇼핑': 0.4, '쇼핑_weight': 0.54, '배달': 0.14, '배달_weight': 0.29, '오락': 0.065, '오락_weight': 0.77, '술': 0.045, '술_weight': 0.19, '야식': 0.075, '야식_weight': 0.3, '카페': 0.045, '카페_weight': 0.31, '구독서비스': 0.03, '구독서비스_weight': 0.09, '택시': 0.01, '택시_weight': 0.0, 'label': '오락 줄이기'}, 
         {'쇼핑': 0.4, '쇼핑_weight': 0.54, '배달': 0.14, '배달_weight': 0.33, '오락': 0.065, '오락_weight': 0.79, '술': 0.045, '술_weight': 0.19, '야식': 0.075, '야식_weight': 0.31, '카페': 0.045, '카페_weight': 0.32, '구독서비스': 0.03, '구독서비스_weight': 0.11, '택시': 0.01, '택시_weight': 0.0, 'label': '오락 줄이기'}, 
         {'쇼핑': 0.33, '쇼핑_weight': 0.57, '배달': 0.13, '배달_weight': 0.44, '오락': 0.07, '오락_weight': 0.2, '술': 0.06, '술_weight': 0.64, '야식': 0.06, '야식_weight': 0.42, '카페': 0.035, '카페_weight': 0.32, '구독서비스': 0.022, '구독서비스_weight': 0.13, '택시': 0.012, '택시_weight': 0.01, 'label': '술줄이기'},
          {'쇼핑': 0.33, '쇼핑_weight': 0.56, '배달': 0.13, '배달_weight': 0.52, '오락': 0.07, '오락_weight': 0.2, '술': 0.06, '술_weight': 0.63, '야식': 0.06, '야식_weight': 0.45, '카페': 0.035, '카페_weight': 0.28, '구독서비스': 0.022, '구독서비스_weight': 0.14, '택시': 0.012, '택시_weight': 0.02, 'label': '술줄이기'},
            {'쇼핑': 0.33, '쇼핑_weight': 0.58, '배달': 0.13, '배달_weight': 0.56, '오락': 0.07, '오락_weight': 0.19, '술': 0.06, '술_weight': 0.67, '야식': 0.06, '야식_weight': 0.39, '카페': 0.035, '카페_weight': 0.29, '구독서비스': 0.022, '구독서비스_weight': 0.13, '택시': 0.012, '택시_weight': 0.04, 'label': '술줄이기'},
              {'쇼핑': 0.32, '쇼핑_weight': 0.28, '배달': 0.135, '배달_weight': 0.31, '오락': 0.065, '오락_weight': 0.11, '술': 0.048, '술_weight': 0.42, '야식': 0.098, '야식_weight': 0.84, '카페': 0.042, '카페_weight': 0.29, '구독서비스': 0.023, '구독서비스_weight': 0.15, '택시': 0.014, '택시_weight': 0.01, 'label': '야식 덜 먹기'},
                {'쇼핑': 0.32, '쇼핑_weight': 0.33, '배달': 0.135, '배달_weight': 0.27, '오락': 0.065, '오락_weight': 0.1, '술': 0.048, '술_weight': 0.37, '야식': 0.098, '야식_weight': 0.71, '카페': 0.042, '카페_weight': 0.29, '구독서비스': 0.023, '구독서비스_weight': 0.13, '택시': 0.014, '택시_weight': 0.01, 'label': '야식 덜 먹기'},
                  {'쇼핑': 0.32, '쇼핑_weight': 0.32, '배달': 0.135, '배달_weight': 0.28, '오락': 0.065, '오락_weight': 0.1, '술': 0.048, '술_weight': 0.38, '야식': 0.098, '야식_weight': 0.85, '카페': 0.042, '카페_weight': 0.29, '구독서비스': 0.023, '구독서비스_weight': 0.15, '택시': 0.014, '택시_weight': 0, 'label': '야식 덜 먹기'},
                    {'쇼핑': 0.34, '쇼핑_weight': 0.11, '배달': 0.145, '배달_weight': 0.18, '오락': 0.058, '오락_weight': 0.64, '술': 0.052, '술_weight': 0.34, '야식': 0.072, '야식_weight': 0.76, '카페': 0.069, '카페_weight': 0.87, '구독서비스': 0.02, '구독서비스_weight': 0.11, '택시': 0.015, '택시_weight': 0.0, 'label': '카페 덜 가기'},
                      {'쇼핑': 0.34, '쇼핑_weight': 0.11, '배달': 0.145, '배달_weight': 0.19, '오락': 0.058, '오락_weight': 0.7, '술': 0.052, '술_weight': 0.3, '야식': 0.072, '야식_weight': 0.65, '카페': 0.069, '카페_weight': 0.79, '구독서비스': 0.02, '구독서비스_weight': 0.13, '택시': 0.015, '택시_weight': 0.01, 'label': '카페 덜 가기'}, 
                      {'쇼핑': 0.34, '쇼핑_weight': 0.11, '배달': 0.145, '배달_weight': 0.2, '오락': 0.058, '오락_weight': 0.72, '술': 0.052, '술_weight': 0.29, '야식': 0.072, '야식_weight': 0.71, '카페': 0.069, '카페_weight': 0.84, '구독서비스': 0.02, '구독서비스_weight': 0.13, '택시': 0.015, '택시_weight': 0, 'label': '카페 덜 가기'},
                        {'쇼핑': 0.33, '쇼핑_weight': 0.19, '배달': 0.13, '배달_weight': 0.1, '오락': 0.05, '오락_weight': 0.29, '술': 0.049, '술_weight': 0.22, '야식': 0.063, '야식_weight': 0.57, '카페': 0.038, '카페_weight': 0.12, '구독서비스': 0.018, '구독서비스_weight': 0.08, '택시': 0.012, '택시_weight': 0.03, 'label': '택시 덜 타기'},
                          {'쇼핑': 0.33, '쇼핑_weight': 0.21, '배달': 0.13, '배달_weight': 0.09, '오락': 0.05, '오락_weight': 0.27, '술': 0.049, '술_weight': 0.2, '야식': 0.063, '야식_weight': 0.63, '카페': 0.038, '카페_weight': 0.12, '구독서비스': 0.018, '구독서비스_weight': 0.1, '택시': 0.012, '택시_weight': 0.01, 'label': '택시 덜 타기'},
                            {'쇼핑': 0.33, '쇼핑_weight': 0.21, '배달': 0.13, '배달_weight': 0.1, '오락': 0.05, '오락_weight': 0.32, '술': 0.049, '술_weight': 0.18, '야식': 0.063, '야식_weight': 0.64, '카페': 0.038, '카페_weight': 0.09, '구독서비스': 0.018, '구독서비스_weight': 0.08, '택시': 0.012, '택시_weight': 0.03, 'label': '택시 덜 타기'},
                              {'쇼핑': 0.31, '쇼핑_weight': 0.38, '배달': 0.138, '배달_weight': 0.39, '오락': 0.053, '오락_weight': 0.58, '술': 0.047, '술_weight': 0.1, '야식': 0.064, '야식_weight': 0.52, '카페': 0.037, '카페_weight': 0.19, '구독서비스': 0.015, '구독서비스_weight': 0.07, '택시': 0.011, '택시_weight': 0.01, 'label': '구독 좀 끊기'},
                                {'쇼핑': 0.31, '쇼핑_weight': 0.41, '배달': 0.138, '배달_weight': 0.45, '오락': 0.053, '오락_weight': 0.62, '술': 0.047, '술_weight': 0.1, '야식': 0.064, '야식_weight': 0.51, '카페': 0.037, '카페_weight': 0.18, '구독서비스': 0.015, '구독서비스_weight': 0.08, '택시': 0.011, '택시_weight': 0.02, 'label': '구독 좀 끊기'},
                                  {'쇼핑': 0.31, '쇼핑_weight': 0.4, '배달': 0.138, '배달_weight': 0.41, '오락': 0.053, '오락_weight': 0.64, '술': 0.047, '술_weight': 0.11, '야식': 0.064, '야식_weight': 0.54, '카페': 0.037, '카페_weight': 0.2, '구독서비스': 0.015, '구독서비스_weight': 0.09, '택시': 0.011, '택시_weight': 0.01, 'label': '구독 좀 끊기'}]




df = pd.DataFrame(data)



le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])

# 특징과 레이블 분리
X = df.drop('label', axis=1)
y = df['label']

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)


# 새로운 데이터 예시
new_data = pd.DataFrame([{
  "쇼핑": 0.36,
  "쇼핑_weight": 0.03,
  "배달": 0.14,
  "배달_weight": 0.83,
  "오락": 0.06,
  "오락_weight": 0.7,
  "술": 0.05,
  "술_weight": 0.6,
  "야식": 0.07,
  "야식_weight": 0.4,
  "카페": 0.02,
  "카페_weight": 0.1,
  "구독서비스": 0.02,
  "구독서비스_weight": 0.1,
  "택시": 0.013,
  "택시_weight": 0.0
}])

# 예측
predicted_label = clf.predict(new_data)
predicted_label_name = le.inverse_transform(predicted_label)
print(predicted_label_name)



# # 모델 저장
# joblib.dump(clf, 'random_forest_model.pkl')
# joblib.dump(le, 'label_encoder.pkl')

# 모델 저장
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)

# LabelEncoder 저장
with open('label_encoder.pkl', 'wb') as le_file:
    pickle.dump(le, le_file)

# # 모델 불러오기
# loaded_model = joblib.load('random_forest_model.pkl')

# # 새로운 데이터 예시
# new_data = pd.DataFrame([{
#   "쇼핑": 0.36,
#   "쇼핑_weight": 0.95,
#   "배달": 0.14,
#   "배달_weight": 0.83,
#   "오락": 0.06,
#   "오락_weight": 0.7,
#   "술": 0.05,
#   "술_weight": 0.6,
#   "야식": 0.07,
#   "야식_weight": 0.4,
#   "카페": 0.045,
#   "카페_weight": 0.3,
#   "구독서비스": 0.02,
#   "구독서비스_weight": 0.1,
#   "택시": 0.013,
#   "택시_weight": 0.0
# }])

# # 예측
# predicted_label = loaded_model.predict(new_data)
# predicted_label_name = le.inverse_transform(predicted_label)
# print(predicted_label_name)
