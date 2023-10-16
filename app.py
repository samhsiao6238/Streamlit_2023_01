import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import json
import os

# 常數：環境使用
class Constants:
    # Streamlit 環境參數
    ST_FIREBASE_CONFIG_STR = 'FIREBASE_CONFIG_STR'

# 初始化 Firebase 
def initialize_firebase():
    try:
        firebase_admin.get_app()
    except ValueError as e:
        if 'STREAMLIT_PUBLIC_PATH' in os.environ:  # 判斷是否在 Streamlit 服務器上
            try:
                firebase_config_str = st.secrets[Constants.ST_FIREBASE_CONFIG_STR]
                cred_info = json.loads(firebase_config_str)
                cred = credentials.Certificate(cred_info)
            except Exception as e:
                st.error(f'解析服務器上的憑證出錯：{e}')
                return False
        else:
            try:
                with open('myproject01-be1b7-firebase-adminsdk-1mh85-3ede5c2672.json', 'r') as f:
                    cred_info = json.load(f)
                cred = credentials.Certificate(cred_info)
            except Exception as e:
                st.error(f'讀取本地 Firebase 憑證出錯，錯誤訊息：{e}')
                return False

        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://myproject01-be1b7-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
    return True

# Streamlit 主要內容
def main():
    st.title("Streamlit & Firebase 整合範例")

    if not initialize_firebase():
        st.error("Firebase 初始化失敗！")
        return

    # 寫入
    def write_to_firebase():
        ref = db.reference('data')
        ref.set({
            'example_key': 'Hello, Firebase!'
        })

    # 讀取
    def read_from_firebase():
        ref = db.reference('data')
        data = ref.get()
        return data

    # 按鈕
    if st.button("寫入 Firebase"):
        write_to_firebase()
        st.success("完成寫入到 Firebase 節點！")
    
    # 按鈕
    if st.button("讀取 Firebase"):
        data = read_from_firebase()
        if data:
            st.write(data)
        else:
            st.warning("Firebase 節點上無資料!")

if __name__ == "__main__":
    main()
