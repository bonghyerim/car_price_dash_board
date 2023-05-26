import streamlit as st

def run_app_home():
    
    st.subheader('안녕하세요!')
    st.markdown('좋은 서비스로 제공하겠습니다.')
    st.markdown('자동 배포 처리된 앱입니다.')

    st.markdown('이 앱은 고객 데이터의 자동차 구매 데이터에 대한 내용입니다.')
    st.markdown('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측해 줍니다.')
    
    img_url = 'https://m.renaultkoream.com/upload/asset/sm6/vr/color/BGAALZSG31EDF/QXD/001.png'

    st.image(img_url)