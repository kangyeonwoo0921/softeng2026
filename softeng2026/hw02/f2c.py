def f2c(temp_f):
    temp_c = (temp_f - 32) * 5/ 9
    return temp_c   

temp_f = float(input("화씨 온도를 입력하세요: "))
temp_c = f2c(temp_f)
print(f"섭씨 온도는 {temp_c:.2f}도입니다.")

def m2is(m):
    return m * 39.3701

meters = float(input("미터를 입력하세요: "))
inches = m2is(meters)
print(f"{meters}미터는 {inches:.2f}인치입니다.")