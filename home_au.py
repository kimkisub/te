import pandas as pd
import os
from datetime import datetime

# 파일 경로 설정
DATA_FOLDER = "date"
POSTS_CSV_PATH = os.path.join(DATA_FOLDER, "post.csv")

# 게시글 데이터를 로드하는 함수
def load_posts():
    """CSV 파일에서 게시글 데이터를 읽어옵니다."""
    try:
        if not os.path.exists(POSTS_CSV_PATH):
            return pd.DataFrame(columns=['author', 'content', 'timestamp'])
        return pd.read_csv(POSTS_CSV_PATH)
    except Exception as e:
        st.error(f"게시글 데이터 로딩 중 오류가 발생했습니다: {e}")
        return pd.DataFrame(columns=['author', 'content', 'timestamp'])

# 게시글 데이터를 저장하는 함수
def save_post(author, content):
    """새로운 게시글을 CSV 파일에 저장합니다."""
    try:
        posts_df = load_posts()
        new_post_data = {'author': author, 'content': content, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        updated_data_list = posts_df.to_dict('records')
        updated_data_list.append(new_post_data)
        
        updated_df = pd.DataFrame(updated_data_list)
        
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
        updated_df.to_csv(POSTS_CSV_PATH, index=False)
        return True
    except Exception as e:
        st.error(f"게시글 저장 중 오류가 발생했습니다: {e}")
        return False
