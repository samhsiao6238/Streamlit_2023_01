import streamlit as st
import json
import os
import firebase_admin
from firebase_admin import credentials, db

def main():
    st.title("從 Firebase 讀取資料並在 Streamlit 顯示")

    # 初始化 Firebase Admin
    if not firebase_admin._apps:
        firebase_config_str = st.secrets['FIREBASE_CONFIG_STR']
        firebase_config = json.loads(firebase_config_str)
        
        cred = credentials.Certificate(firebase_config)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://myproject01-be1b7-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })

    # 讀取 Firebase 實時資料庫的資料
    ref = db.reference('/')
    data = ref.get()

    # 在 Streamlit 上顯示資料
    # st.json(data)

if __name__ == "__main__":
    # st.write(st.secrets)
    # main()
    st.title("這是 main")
