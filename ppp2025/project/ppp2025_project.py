import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import style
import koreanize_matplotlib 

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

#로지스틱 생장 모델
def growth_model(X_0, K, r, t_predict):
    X_t = K / (1 + (K - X_0 / X_0) * np.exp(-r * t_predict))
    return X_t
    
# 생장 곡선 기반 수확시점 계산식
def harvest_time(r, X_0, K, alpha):
    t_harvest = (1 /r) * np.log( ((K - X_0) / X_0) * (1 / (1/alpha - 1)) )
    return t_harvest


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
        
      
        #생체량, 수확량, 생장률 계산
        growth_biomass= specific_growth_rate(X_1, X_2, t_1, t_2)
        df["growth_biomass"] =growth_biomass
        df["biomass_rate"] = biomass_concentration(W_1, W_2, V)
        df["productivity_rate"] = productivity(df["biomass_rate"], t)
        df["cumulative_biomass"] = df["biomass_rate"].cumsum()
        df["cumulative_CO2"] = df["cumulative_biomass"] * 1.83
        
        st.subheader("가공된 데이터")
        st.dataframe(df)
        
        

        # streamlit 파라미터
        alpha = st.slider("수확 목표 비율 (a)", 0.5, 1.0, 0.9, step=0.01)
        X_0 = (df["X1"].iloc[0])
        K = (df["X2"].max())
        r = (df["growth_biomass"].mean())
        t_predict = np.arange(0, 20, 0.1)
        
        #로지스틱 모델 계산
        X_t_predict = growth_model(X_0, K, r, t_predict)
        t_harvest = harvest_time(r, X_0, K, alpha)
        
      
        
        ######그래프 시각화
        
        fig, axs = plt.subplots(2, 2, figsize =(12, 8))
        
        #생장률 그래프
        axs[0, 0].plot(df["date"], df["growth_biomass"], color = "green", marker = ".", label = "생장률")
        axs[0, 0].set_title("생장률")
        axs[0, 0].set_xlabel("time(day)")
        axs[0, 0].set_ylabel("growth rate")
        axs[0, 0].legend()
        
        
        #수확량, 생체량
        axs[0, 1].plot(df["date"], df["biomass_rate"], color = "red", marker = "." , label = "생체량")
        axs[0, 1].plot(df["date"], df["productivity_rate"], color = "blue", marker = ".", label = "수확량")
        axs[0, 1].set_title("생체량 및 수확량")
        axs[0, 1].set_xlabel("time(day)")
        axs[0, 1].set_ylabel("biomass(g/L)")
        axs[0, 1].legend()
        
        
        #로지스틱 생장 모델
        axs[1, 0].plot(t_predict, X_t_predict, color = "green", marker= ".", label = "예측 생체량" )
        axs[1, 0].axvline(x = t_harvest, color = "red", linestyle = "dashed", label = "예상 수확시점")
        axs[1, 0].set_xlabel("time(day)")
        axs[1, 0].set_ylabel("biomass(g/L)")
        axs[1, 0].set_title("로지스틱 생장모델")
        axs[1, 0].legend()
    
        #C02 흡수량
        # axs[1, 1].plot(df["date"], df["cumulative_biomass"], color = "red", marker = ".", label = "누적 생산량")
        axs[1, 1].plot(df["date"], df["cumulative_CO2"], color = "blue", marker = ".", label = "누적 CO2 흡수량")
        axs[1, 1].set_xlabel("time(day)")
        # axs[1, 1].set_ylabel("biomass(g/L)")
        axs[1, 1].set_ylabel("Cumulative CO₂ uptake (g/L)")
        axs[1, 1].set_title("누적 CO₂ 흡수량")
        axs[1, 1].legend()
        
        
        plt.tight_layout()
        st.pyplot(fig)
        
        st.write(f"예상 수확시점(일) : {t_harvest:.2f}일")
        
        
    #streamlit run c:/code/ppp2025/project/ppp2025_project.py


if __name__=="__main__":
    main()
    