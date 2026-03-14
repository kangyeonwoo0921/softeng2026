import streamlit as st

st.title("🛠️ 연우 응소 과제")
st.markdown("202410055 스마트팜학과 강연우")

st.sidebar.title("📋 기능 선택")
option = st.sidebar.selectbox("원하는 기능을 선택하세요", ["짝수/홀수 확인", "온도 변환", "길이 변환", "팩토리얼 계산", "소수 찾기", "소수 확인", "2의 배수 합"])

if option == "짝수/홀수 확인":
    st.header("🔢 짝수/홀수 확인")
    st.write("입력한 숫자가 짝수인지 홀수인지 확인합니다.")
    num = st.number_input("숫자를 입력하세요", value=0, step=1)
    if st.button("확인"):
        if num % 2 == 0:
            st.success("입력한 숫자는 짝수입니다. ✅")
        else:
            st.error("입력한 숫자는 홀수입니다. ❌")

elif option == "온도 변환":
    st.header("🌡️ 화씨에서 섭씨로 변환")
    st.write("화씨 온도를 섭씨로 변환합니다.")
    temp_f = st.number_input("화씨 온도를 입력하세요", value=0.0)
    if st.button("변환"):
        temp_c = (temp_f - 32) * 5 / 9
        st.write(f"섭씨 온도는 {temp_c:.2f}도입니다. ❄️")

elif option == "길이 변환":
    st.header("📏 미터에서 인치로 변환")
    st.write("미터를 인치로 변환합니다.")
    meters = st.number_input("미터를 입력하세요", value=0.0)
    if st.button("변환"):
        inches = meters * 39.3701
        st.write(f"{meters}미터는 {inches:.2f}인치입니다. 📐")

elif option == "팩토리얼 계산":
    st.header("🔢 팩토리얼 계산")
    st.write("숫자의 팩토리얼을 계산합니다.")
    n = st.number_input("숫자를 입력하세요", value=1, step=1, min_value=1)
    if st.button("계산"):
        def fact(n):
            if n == 1:
                return 1
            return n * fact(n - 1)
        result = fact(n)
        st.write(f"{n}! = {result} 🎉")

elif option == "소수 찾기":
    st.header("🔍 소수 찾기")
    st.write("주어진 숫자까지의 소수를 찾습니다.")
    n = st.number_input("숫자를 입력하세요", value=10, step=1, min_value=2)
    if st.button("찾기"):
        def find_prime(n):
            primes = []
            for i in range(2, n + 1):
                is_prime = True
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(i)
            return primes
        primes = find_prime(n)
        st.write(f"{n}까지의 소수: {primes} 🧮")

elif option == "소수 확인":
    st.header("✅ 소수 확인")
    st.write("숫자가 소수인지 확인합니다.")
    n = st.number_input("숫자를 입력하세요", value=2, step=1, min_value=0)
    if st.button("확인"):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        if is_prime(n):
            st.success(f"{n}은 소수입니다. ✅")
        else:
            st.error(f"{n}은 소수가 아닙니다. ❌")

elif option == "2의 배수 합":
    st.header("📊 1부터 100까지 2의 배수의 합")
    st.write("1부터 100까지의 2의 배수들의 합을 계산합니다.")
    
    nums = [x for x in range(1, 101) if x % 2 == 0]
    total = sum(nums)
    
    st.write(f"합계: {total} 💰")
    
    with st.expander("2의 배수들 보기"):    
        st.text(nums) 
        # st.write(str(nums)) # 방법 B: 문자열로 변환해서 출력