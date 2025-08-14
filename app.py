import streamlit as st
import app_au as au

# 세션 상태 초기화: 로그인 여부, 사용자 ID, 현재 페이지 상태를 저장
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'login' # 'login' 또는 'home'

# 로그인/회원가입 페이지
def login_signup_page():
    st.header("나만의 소셜", divider=True)
    tab1, tab2 = st.tabs(["로그인", "회원가입"])

    with tab1:
        st.header("로그인")
        login_id = st.text_input("아이디", key="login_id")
        login_pw = st.text_input("비밀번호", type="password", key="login_pw")
        
        if st.button("로그인", key="login_button"):
            if au.authenticate(login_id, login_pw):
                st.session_state['logged_in'] = True
                st.session_state['user_id'] = login_id
                st.session_state['page'] = 'home'
                st.success("로그인 성공!")
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
                
    with tab2:
        st.header("회원가입")
        signup_id = st.text_input("아이디", key="signup_id")
        signup_pw = st.text_input("비밀번호", type="password", key="signup_pw")
        signup_pw_confirm = st.text_input("비밀번호 확인", type="password", key="signup_pw_confirm")

        if st.button("회원가입", key="signup_button"):
            users_df = au.load_users()
            if not signup_id or not signup_pw or not signup_pw_confirm:
                st.error("모든 필드를 입력해 주세요.")
            elif signup_pw != signup_pw_confirm:
                st.error("비밀번호가 일치하지 않습니다.")
            elif signup_id in users_df['id'].values:
                st.error("이미 존재하는 아이디입니다.")
            else:
                if au.save_user(signup_id, signup_pw):
                    st.success("회원가입이 완료되었습니다! 로그인 탭으로 이동해 주세요.")
                    st.balloons()
                    st.rerun()

# 페이지 전환
if st.session_state['page'] == 'login':
    login_signup_page()
elif st.session_state['page'] == 'home':
    # home.py를 import해서 실행
    import home
    home.main()
