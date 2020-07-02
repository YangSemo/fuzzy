import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 조건 - 세탁물의 양(kg), 오염(%)   결과 - 세탁 시간(분), 세제의 양(g)
laundry_amount = ctrl.Antecedent(np.arange(0, 31, 1), 'laundry_amount')
pollution = ctrl.Antecedent(np.arange(0, 100, 1), 'pollution')
wash_time = ctrl.Consequent(np.arange(0, 121, 1), 'wash_time')
detergent_amount = ctrl.Consequent(np.arange(0, 181, 1), 'detergent_amount')

# 각 조건과 결과에 대한 범위 지정
# 세탁물의 양(kg)
laundry_amount_low = fuzz.trimf(laundry_amount.universe, [0, 0, 10])
laundry_amount_medium = fuzz.trimf(laundry_amount.universe, [5, 10, 15])
laundry_amount_high = fuzz.trimf(laundry_amount.universe, [10, 25, 30])



# 오염 정도(%)
pollution_low = fuzz.trimf(pollution.universe, [0, 0, 30])
pollution_medium = fuzz.trimf(pollution.universe, [20, 45, 60])
pollution_high = fuzz.trimf(pollution.universe, [45, 75, 99])

# 세탁 시간(분)
wash_time_tooLow = 35
wash_time_low = 50
wash_time_medium = 60
wash_time_high = 90
wash_time_tooHigh= 120

# 세제 양(g)
detergent_amount_low = 60
detergent_amount_medium = 120
detergent_amount_high = 170

# input value
print("세탁물의 양을 입력하세요.")
laundry_amount_input = input()
laundry_amount_input = int(laundry_amount_input)
print("오염 정도를 입력하세요.")
pollution_input = input()
pollution_input = int(pollution_input)

# 최솟값들 저장 리스트
min_value_list =[]
# 각 조건의 최솟값 * 결과값 저장
result=[]

# rule 1: laundry_amount=low and pollution= low  then washtime= low and detergent= low
if 0 <= laundry_amount_input <= 10 and 0 <= pollution_input <= 30:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_low[laundry_amount_input]
    b = pollution_low[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a,b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_tooLow, min_value * detergent_amount_low])
    print(result)

# rule 2: laundry_amount=low and pollution= medium  then washtime= low and detergent= low
if 0 <= laundry_amount_input <= 10 and 20 <= pollution_input <= 60:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_low[laundry_amount_input]
    b = pollution_medium[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_low, min_value * detergent_amount_medium])

"""
 rule 2 ~ rule 8 생략
"""
# rule 3: laundry_amount=low and pollution= medium  then washtime= low and detergent= low
if 0 <= laundry_amount_input <= 10 and 45 <= pollution_input <= 99:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_low[laundry_amount_input]
    b = pollution_high[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_medium, min_value * detergent_amount_medium])

# rule 4: laundry_amount=low and pollution= medium  then washtime= low and detergent= low
if 5 <= laundry_amount_input <= 15 and 0 <= pollution_input <= 30:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_medium[laundry_amount_input]
    b = pollution_low[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_medium, min_value * detergent_amount_low])

# rule 5: laundry_amount=low and pollution= medium  then washtime= low and detergent= low
if 5 <= laundry_amount_input <= 15 and 20 <= pollution_input <= 60:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_medium[laundry_amount_input]
    b = pollution_medium[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_medium, min_value * detergent_amount_medium])

# rule 6: laundry_amount=low and pollution= medium  then washtime= low and detergent= low
if 5 <= laundry_amount_input <= 15 and 45 <= pollution_input <= 99:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_medium[laundry_amount_input]
    b = pollution_high[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_high, min_value * detergent_amount_low])

# rule 7: laundry_amount=high and pollution= high  then washtime= too_high and detergent= high
if 10 <= laundry_amount_input < 30 and 0 <= pollution_input < 30:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_high[laundry_amount_input]
    b = pollution_low[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_high, min_value * detergent_amount_medium])

# rule 8: laundry_amount=high and pollution= high  then washtime= too_high and detergent= high
if 10 <= laundry_amount_input < 30 and 20 <= pollution_input < 60:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_high[laundry_amount_input]
    b = pollution_medium[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_high, min_value * detergent_amount_high])


# rule 9: laundry_amount=high and pollution= high  then washtime= too_high and detergent= high
if 10 <= laundry_amount_input < 30 and 45 <= pollution_input < 99:
    # 입력 값(a=세탁물 양, b=오염정도)에 대한 y좌표 값 추출
    a = laundry_amount_high[laundry_amount_input]
    b = pollution_high[pollution_input]

    # 두 값 중 최소값 추출
    min_value = min(a, b)
    min_value_list.append(min_value)

    # 최소값 * 결과값
    result.append([min_value * wash_time_tooHigh, min_value * detergent_amount_high])

# washtime 리스트 추출 후 sum
washtime_result =[]
for i in result:
    washtime_result.append(i[0])
sum_washtime = sum(washtime_result)

# detergent 리스트 추출 후 sum
detergent_result=[]
for i in result:
    detergent_result.append(i[1])
sum_detergent = sum(detergent_result)

# 최종 결과값 계산
real_washtime = sum_washtime / sum(min_value_list)
print("real_washtime: ",real_washtime)
real_detergent = sum_detergent / sum(min_value_list)
print("real_detergent: ",real_detergent)


