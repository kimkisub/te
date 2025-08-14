import pandas as pd
import os

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
        new_user_data = {'id': new_user_id, 'password': new_user_pw}
        
        # 기존 데이터를 딕셔너리 리스트로 변환하고 새 데이터를 추가
        updated_data_list = users_df.to_dict('records')
        updated_data_list.append(new_user_data)
        
        updated_df = pd.DataFrame(updated_data_list)
        
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
