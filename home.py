import streamlit as st
import home_au as hau
from datetime import datetime

def main():
    st.header(f"{st.session_state['user_id']}님, 환영합니다! 🎉", divider=True)
    
    # 게시글 작성 폼
    with st.form("new_post_form", clear_on_submit=True):
        st.subheader("새 글 작성")
        post_content = st.text_area("내용을 입력하세요")
        submit_button = st.form_submit_button("게시글 올리기")

        if submit_button and post_content:
            hau.save_post(st.session_state['user_id'], post_content)
            st.success("게시글이 성공적으로 작성되었습니다.")
            st.rerun()
        elif submit_button and not post_content:
            st.warning("게시글 내용을 입력해 주세요.")
            
    st.divider()

    # 게시글 목록
    st.subheader("게시글 목록")
    posts_df = hau.load_posts()
    
    # 로그인한 사용자의 게시글만 필터링
    user_posts = posts_df[posts_df['author'] == st.session_state['user_id']]
    
    if user_posts.empty:
        st.write("아직 작성한 게시글이 없습니다.")
    else:
        # 최신 글이 먼저 보이도록 정렬
        user_posts = user_posts.sort_values(by='timestamp', ascending=False)
        
        for index, row in user_posts.iterrows():
            st.info(f"**{row['author']}** - _{row['timestamp']}_")
            st.write(row['content'])
            st.markdown("---")
            
    if st.button("로그아웃", key="logout_button"):
        st.session_state['logged_in'] = False
        st.session_state['user_id'] = None
        st.session_state['page'] = 'login'
        st.rerun()

