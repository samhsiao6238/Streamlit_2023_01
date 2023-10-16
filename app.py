import streamlit as st
import json
import os

def main():
    st.title("檢查並讀取 Streamlit Secrets 或 Firebase JSON 檔")

    # # 如果在 Streamlit Sharing 雲端服務上運行
    # if (True):
    #     db_username = st.secrets['db_username']
    #     db_password = st.secrets['db_password']
    # else:  # 本地運行
    #     with open('myproject01-be1b7-firebase-adminsdk-1mh85-3ede5c2672.json', 'r') as f:
    #         firebase_data = json.load(f)
    #         db_username = firebase_data.get('db_username')  # 這裡的鍵名取決於您的 JSON 檔結構
    #         db_password = firebase_data.get('db_password')  # 這裡的鍵名取決於您的 JSON 檔結構

    # st.write(f"DB 使用者名稱: {db_username}")
    # st.write(f"DB 密碼: {'*' * len(db_password) if db_password else None}")  # 顯示為星號以保密

if __name__ == "__main__":
    main()
