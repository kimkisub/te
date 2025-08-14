import pandas as pd
import os
import streamlit as st # st.error를 사용하기 위해 추가

# 파일 경로 설정
DATA_FOLDER = "date"
USERS_CSV_PATH = os.path.join(DATA_FOLDER, "users.csv")

# 사용자 데이터를 로드하는 함수
def load_users():
    """CSV 파일에서 사용자 데이터를 읽어옵니다."""
    try:
        if not os.path.exists(USERS_CSV_PATH):
            return pd.DataFrame(columns=['id', 'password'])
        return pd.read_csv(USERS_CSV_PATH)
    except Exception as e:
        st.error(f"사용자 데이터 로딩 중 오류가 발생했습니다: {e}")
        return pd.DataFrame(columns=['id', 'password'])

# 사용자 데이터를 저장하는 함수
def save_user(new_user_id, new_user_pw):
    """새로운 사용자 정보를 CSV 파일에 저장합니다."""
    try:
        users_df = load_users()
        # 데이터가 없을 경우 초기 DataFrame을 생성
        if users_df.empty:
            updated_df = pd.DataFrame([{'id': new_user_id, 'password': new_user_pw}])
        else:
            new_user_data = pd.DataFrame([{'id': new_user_id, 'password': new_user_pw}])
            updated_df = pd.concat([users_df, new_user_data], ignore_index=True)
        
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
        updated_df.to_csv(USERS_CSV_PATH, index=False)
        return True
    except Exception as e:
        st.error(f"회원 정보 저장 중 오류가 발생했습니다: {e}")
        return False

# 사용자 인증 함수
def authenticate(user_id, password):
    """아이디와 비밀번호가 일치하는지 확인합니다."""
    users_df = load_users()
    user_match = users_df[(users_df['id'] == user_id) & (users_df['password'] == password)]
    return not user_match.empty
