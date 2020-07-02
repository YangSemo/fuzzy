import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# 조건 - 세탁물의 양(kg), 오염(%)   결과 - 세탁 시간(분), 세제의 양(g)
# x값에 대한 y값 초기화(0~1)
laundry_amount = ctrl.Antecedent(np.arange(0, 31, 1), 'laundry_amount')
pollution = ctrl.Antecedent(np.arange(0, 100, 1), 'pollution')
wash_time = ctrl.Consequent(np.arange(0, 121, 1), 'wash_time')
detergent_amount = ctrl.Consequent(np.arange(0, 181, 1), 'detergent_amount')


# 각 조건과 결과에 대한 범위 지정
# 세탁물의 양(kg)
laundry_amount['low'] = fuzz.trimf(laundry_amount.universe, [0, 0, 10])
laundry_amount['medium'] = fuzz.trimf(laundry_amount.universe, [5, 10, 15])
laundry_amount['high'] = fuzz.trimf(laundry_amount.universe, [10, 25, 30])

# 오염 정도(%)
pollution['low'] = fuzz.trimf(pollution.universe, [0, 0, 30])
pollution['medium'] = fuzz.trimf(pollution.universe, [20, 45, 60])
pollution['high'] = fuzz.trimf(pollution.universe, [45, 75, 99])

# 세탁 시간(분)
wash_time['Too_low'] = fuzz.trimf(wash_time.universe, [20, 30, 35])
wash_time['low'] = fuzz.trimf(wash_time.universe, [30, 40, 50])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [40, 50, 60])
wash_time['high'] = fuzz.trimf(wash_time.universe, [50, 70, 90])
wash_time['Too_high'] = fuzz.trimf(wash_time.universe, [70, 100, 120])

# 세제 양(g)
detergent_amount['low'] = fuzz.trimf(detergent_amount.universe, [30, 50, 60])
detergent_amount['medium'] = fuzz.trimf(detergent_amount.universe, [55, 100, 120])
detergent_amount['high'] = fuzz.trimf(detergent_amount.universe, [100, 145, 170])


# input value
print("세탁물의 양을 입력하세요.")
laundry_amount_input = input()
print("오염 정도를 입력하세요.")
pollution_input = input()

# 조건 설정
rule1 = ctrl.Rule(laundry_amount['low'] & pollution['low'], (wash_time['Too_low'], detergent_amount['low']))
rule2 = ctrl.Rule(laundry_amount['low'] & pollution['medium'], (wash_time['low'], detergent_amount['medium']))
rule3 = ctrl.Rule(laundry_amount['low'] & pollution['high'], (wash_time['medium'], detergent_amount['medium']))

rule4 = ctrl.Rule(laundry_amount['medium'] & pollution['low'], (wash_time['medium'], detergent_amount['low']))
rule5 = ctrl.Rule(laundry_amount['medium'] & pollution['medium'], (wash_time['medium'], detergent_amount['medium']))
rule6 = ctrl.Rule(laundry_amount['medium'] & pollution['high'], (wash_time['high'], detergent_amount['medium']))

rule7 = ctrl.Rule(laundry_amount['high'] & pollution['low'], (wash_time['high'], detergent_amount['medium']))
rule8 = ctrl.Rule(laundry_amount['high'] & pollution['medium'], (wash_time['high'], detergent_amount['high']))
rule9 = ctrl.Rule(laundry_amount['high'] & pollution['high'], (wash_time['Too_high'], detergent_amount['high']))

# 그래프 보여주기(디버깅에만 보임)
laundry_amount.view()
pollution.view()
wash_time.view()
detergent_amount.view()

# 조건 적용
washer_result = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
time_detergent = ctrl.ControlSystemSimulation(washer_result)

time_detergent.input['laundry_amount'] = int(laundry_amount_input)
time_detergent.input['pollution'] = int(pollution_input)



# Mamdami 방법 사용
time_detergent.compute()
print("세탁기 수행 결과")
print("세탁기 수행 시간: ",(int)(time_detergent.output['wash_time']), "분", ", 세제 양: ", (int)(time_detergent.output['detergent_amount']),"g")
wash_time.view(sim=time_detergent)
detergent_amount.view(sim=time_detergent)
input('Press any key to exit')