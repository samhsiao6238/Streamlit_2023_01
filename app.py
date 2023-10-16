import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, db


def initialize_firebase():
    try:
        firebase_admin.get_app()  # 嘗試獲取應用，如果已經存在則跳過初始化
    except ValueError as e:
        firebase_cred = st.secrets["FIREBASE_CONFIG_STR"]
        if firebase_cred is not None:
            try:
                cred_info = json.loads(firebase_cred)
                cred = credentials.Certificate(cred_info)
            except json.JSONDecodeError:
                # 假如這樣獲取失敗，還有另一個環境變數儲存了文字憑證
                try:
                    # 讀取 json
                    cred = credentials.Certificate(json.loads(firebase_cred))
                except Exception as e:
                    st.error(f'兩種方式皆無法解析服務器上的憑證：{e}')
                    return False
            else:
                st.error('未設置 FIREBASE_CRED 環境變量')
                return False
        # 初始化 Firebase
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://myproject01-be1b7-default-rtdb.asia-southeast1.firebasedatabase.app/'})
    return True

def main():
    if initialize_firebase():
        ref = db.reference('/')
        data = ref.get()
        st.json(data)

if __name__ == "__main__":
    main()
