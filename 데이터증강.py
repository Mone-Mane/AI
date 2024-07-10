import numpy as np
import random
import json


# 원본 데이터
data = [
    {"쇼핑": 0.35, "쇼핑_weight": 1.0, "배달": 0.146, "배달_weight": 0.5, "오락": 0.056, "오락_weight": 0.3, "술": 0.05, "술_weight": 0.6, "야식": 0.07, "야식_weight": 0.1, "카페": 0.0433, "카페_weight": 0.7, "구독서비스": 0.02, "구독서비스_weight": 0.142, "택시": 0.0133, "택시_weight": 0.0, "label": "쇼핑 줄이기"},
    {"쇼핑": 0.3, "쇼핑_weight": 0.3, "배달": 0.17, "배달_weight": 0.9, "오락": 0.06, "오락_weight": 0.4, "술": 0.055, "술_weight": 0.3, "야식": 0.065, "야식_weight": 0.2, "카페": 0.04, "카페_weight": 0.8, "구독서비스": 0.025, "구독서비스_weight": 0.15, "택시": 0.015, "택시_weight": 0.05, "label": "배달 덜 먹기"},
    {"쇼핑": 0.4, "쇼핑_weight": 0.5, "배달": 0.14, "배달_weight": 0.3, "오락": 0.065, "오락_weight": 0.8, "술": 0.045, "술_weight": 0.2, "야식": 0.075, "야식_weight": 0.3, "카페": 0.045, "카페_weight": 0.3, "구독서비스": 0.03, "구독서비스_weight": 0.1, "택시": 0.01, "택시_weight": 0.0, "label": "오락 줄이기"},
    {"쇼핑": 0.33, "쇼핑_weight": 0.6, "배달": 0.13, "배달_weight": 0.5, "오락": 0.07, "오락_weight": 0.2, "술": 0.06, "술_weight": 0.7, "야식": 0.06, "야식_weight": 0.4, "카페": 0.035, "카페_weight": 0.3, "구독서비스": 0.022, "구독서비스_weight": 0.12, "택시": 0.012, "택시_weight": 0.02, "label": "술줄이기"},
    {"쇼핑": 0.32, "쇼핑_weight": 0.3, "배달": 0.135, "배달_weight": 0.3, "오락": 0.065, "오락_weight": 0.1, "술": 0.048, "술_weight": 0.4, "야식": 0.098, "야식_weight": 0.8, "카페": 0.042, "카페_weight": 0.28, "구독서비스": 0.023, "구독서비스_weight": 0.14, "택시": 0.014, "택시_weight": 0.0, "label": "야식 덜 먹기"},
    {"쇼핑": 0.34, "쇼핑_weight": 0.1, "배달": 0.145, "배달_weight": 0.2, "오락": 0.058, "오락_weight": 0.7, "술": 0.052, "술_weight": 0.3, "야식": 0.072, "야식_weight": 0.7, "카페": 0.069, "카페_weight": 0.8, "구독서비스": 0.02, "구독서비스_weight": 0.13, "택시": 0.015, "택시_weight": 0.0, "label": "카페 덜 가기"},
    {"쇼핑": 0.33, "쇼핑_weight": 0.2, "배달": 0.13, "배달_weight": 0.1, "오락": 0.05, "오락_weight": 0.3, "술": 0.049, "술_weight": 0.2, "야식": 0.063, "야식_weight": 0.6, "카페": 0.038, "카페_weight": 0.1, "구독서비스": 0.018, "구독서비스_weight": 0.09, "택시": 0.012, "택시_weight": 0.03, "label": "택시 덜 타기"},
    {"쇼핑": 0.31, "쇼핑_weight": 0.4, "배달": 0.138, "배달_weight": 0.4, "오락": 0.053, "오락_weight": 0.6, "술": 0.047, "술_weight": 0.1, "야식": 0.064, "야식_weight": 0.5, "카페": 0.037, "카페_weight": 0.2, "구독서비스": 0.015, "구독서비스_weight": 0.08, "택시": 0.011, "택시_weight": 0.01, "label": "구독 좀 끊기"}
]


# 데이터 증강 함수
def augment_data(data, num_samples=3):
    augmented_data = []
    for entry in data:
        for _ in range(num_samples):
            new_entry = {}
            for key, value in entry.items():
                if 'weight' in key or key in ["카페 덜 가기","택시 덜 타기","오락 줄이기","쇼핑 줄이기","술 덜 마시기","야식 덜 먹기","배달 덜 먹기","구독 좀 끊기"]:
                    noise = np.random.normal(0, 0.01)  # 가우시안 잡음 추가
                    change = random.uniform(-0.1, 0.1)  # 10% 범위 내에서 임의 조정
                    new_value = value * (1 + change) + noise
                    # 값이 0과 1 사이에 있어야 하는 weight에 대해 조정
                    if "weight" in key:
                        new_value = max(0, min(1, new_value))
                    new_entry[key] = round(new_value, 2)  # 소수점 두 자리로 반올림
                else:
                    new_entry[key] = value  # 라벨은 변경 없이 유지
            augmented_data.append(new_entry)
    return augmented_data

# 데이터 증강 실행
augmented_data = augment_data(data)

# JSON 형식으로 출력
for i in augmented_data:
    for key, value in i.items():
        if isinstance(value, (int, float)):
            i[key] = "{:,}".format(round(value, 2))
    print(json.dumps(i, indent=2))
