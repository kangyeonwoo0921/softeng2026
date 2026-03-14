from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import streamlit as st
import koreanize_matplotlib 
from sklearn.metrics import mean_squared_error, r2_score



#생체량 계산식
def biomass_concentration(W_1, W_2, V):
    X = (W_2 - W_1) / V
    return X

#생장률 계산식
def specific_growth_rate(X_1, X_2, t_1, t_2):
    u = (np.log(X_2) - np.log(X_1)) / (t_2 - t_1)
    return u

#수확량 계산식
def productivity (X, t):
    P = X / t
    return P

def temperature_cf(T, T_opt=32, T_sigma=4):
    return np.exp(-((T - T_opt) ** 2) / (2 * T_sigma ** 2))

def light_cf(I):
    return I / (I + 80)  # 단순 포화 반응형

def pH_cf(pH, pH_opt=9.5, pH_sigma=0.5):
    return np.exp(-((pH - pH_opt) ** 2) / (2 * pH_sigma ** 2))

def mixxing_cf(M):  # 교반 여부: "O" 또는 "X"
    return 1 if M == "O" else 0.85

#로지스틱 계산식
def logistic(t, X0, K, r):
    result = K / (1 + ((K - X0) / X0) * np.exp(-r * t))
    return result


def main():
   
    st.title("스피루리나 생장 모델")
    
    uploaded_file = st.file_uploader("파일을 업로드 하세요.",  type=["csv"])
 
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding="utf-8-sig")
        
        #변수 정리
        t_1= (df["t1"])
        t_2= (df["t2"])
        X_1= (df["X1"])
        X_2= (df["X2"])
        W_1= (df["W1"])
        W_2= (df["W2"])
        t= (df["t2"] - df["t1"])
        V = (df["volume"])
        df["date"] = (df["t1"] + df["t2"])/ 2 
        
        #사용자 입력값
        with st.sidebar:
            st.header("환경 조건 정리")
        
            T = st.slider("온도 (℃)", 20, 40, 32)
            I = st.slider("광도 (µmol/m²/s)", 0, 300, 100)
            pH = st.slider("pH", 6.5, 11.0, 9.5)
            M = st.radio("교반 여부", ("O", "X"))
            st.markdown("---")

        

        #생체량, 수확량, 생장률 계산
        growth_biomass= specific_growth_rate(X_1, X_2, t_1, t_2)
        df["growth_biomass"] =growth_biomass
        df["biomass_rate"] = biomass_concentration(W_1, W_2, V)    
                    
        #데이터 정리(로지스틱용 데이터)
        t_data = df["date"] - df["date"].min()
        t_extend = np.linspace(0, t_data.max() + 10, 100)

        x_data = df["biomass_rate"]

        #피팅 수행
        params, _ = curve_fit(logistic, t_data, x_data, p0=[0.1, 1.5, 0.2])
        X0_fit, K_fit, r_fit = params
        
        #보정계수 정리
        r_fit = params[2]  
        f_T = temperature_cf(T)
        f_I = light_cf(I)
        f_pH = pH_cf(pH)
        f_M = mixxing_cf(M)

        reff = r_fit * f_T * f_I * f_pH * f_M
        
        
        #예측값 계산
        X_fit = logistic(t_data, *params)
        X_extend = logistic(t_extend, *params)
        X_biofit = logistic(t_extend, X0_fit, K_fit, reff)
        
        #그래프 시각화
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(t_data, x_data, color = "blue", label="실측 생체량", marker ="o")   
        ax.plot(t_extend, X_extend, color = "green", linestyle= "-", linewidth = 2,
                label ="로지스틱 피팅")
        ax.plot(t_extend, X_biofit, color="orange", linestyle="--", linewidth=2, label="보정된 생장률 예측")

        
        ax.set_title("스피루리나 생장 곡선", fontsize = 14)
        ax.set_xlabel("시간 (day)")
        ax.set_ylabel("생체량 (g/L)")
        ax.legend()
        ax.grid(True)
        
        #정확도 (r2값)
        if st.button("정확도 지표 계산"):
            rmse = np.sqrt(mean_squared_error(x_data, X_fit))
            r2 = r2_score(x_data, X_fit)
            
            st.subheader("로지스틱 피팅 정확도 지표")
            st.write(f"**RMSE (평균 제곱근 오차)**: {rmse:.4f}")
            st.write(f"**R² (결정계수)**: {r2:.4f}")
        
        
        st.pyplot(fig)
        
        #결과값 저장
        result_df = pd.DataFrame({
            "시간(day)":t_extend,
            "피팅 생체량(g/L)": X_extend,
            "보정 생체량(g/L)": X_biofit
        })
        
        if not result_df.empty:
            csv = result_df.to_csv(index=False).encode("utf-8-sig")
            st.download_button("예측 결과 CSV 다운로드", csv, "spiruilina_prediction.csv", "text/csv" )
        

    #streamlit run c:/code/ppp2025/project/curve_fitting.py
    
    
if __name__ =="__main__":
    main()