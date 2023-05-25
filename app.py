import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main():
    st.title('자동차 가격 예측 앱')

    menu = ['Home', 'EDA', 'ML']

    choice = st.sidebar.selectbox('메뉴', menu) # 유저가 선택한 것을 choice에 담아라

    if choice == menu[0] : 
        run_app_home()
    elif choice == menu[1] :
        run_app_eda()
    else : 
        run_app_ml()



if __name__ == '__main__' :
    main()
