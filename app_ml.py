import streamlit as st
import numpy as np
import joblib


def run_app_ml() :
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을
    # 유저한테 입력 받는다.

    # 버튼을 누르면 예측한 금액을 표시한다.

    gender = st.radio('성별 선택', ['남자','여자'])

    if gender == '남자' :
        gender = 0 
    else : 
        gender = 1

    age = st.number_input('나이 입력',18, 100)
    salary = st.number_input('연봉 입력', 5000, 100000)
    dept = st.number_input('카드 빚', 0, 1000000)
    worth = st.number_input('자산입력', 1000, 10000)

    # 버튼을 누르면 예측한 금액이 표시된다.

    if st.button("금액 예측"):
        
        new_data = np.array([gender, age, salary, dept, worth])
        new_data = new_data.reshape(1, 5)
        regressor = joblib.load('model/regressor.pkl')
        y_pred = regressor.predict(new_data)
        print(y_pred)


        price = round(y_pred[0])

        # print(str(price)+'달러짜리 차량 구매 가능합니다.')
        # print(f'{price}달러짜리 차량 구매 가능합니다.')
        # print('{}달러짜리 차량 구매 가능합니다.'.format(price))

        
        st.text(f'{price}달러짜리 차량 구매 가능합니다.')
        # 버튼을 누르면 예측한 금액을 표시한다