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
        return True  # 如果Firebase已初始化，则直接返回True
    except ValueError as e:  # 没有初始化应用程序时，继续以下过程
        if 'STREAMLIT_PUBLIC_PATH' in os.environ:  # 判斷是否在 Streamlit 服務器上
            try:
                firebase_config_str = st.secrets[Constants.ST_FIREBASE_CONFIG_STR]
                cred_info = json.loads(firebase_config_str)
                cred = credentials.Certificate(cred_info)
            except Exception as e:
                st.error(f'解析服務器上的憑證出錯：{e}')
                return False
        else:  # 本地环境
            try:
                # 由于您没有在本地使用secrets.toml，因此需要一个本地JSON文件路径。这里假设你已经有了这个文件。
                with open('myproject01-be1b7-firebase-adminsdk-1mh85-3ede5c2672.json', 'r') as f:  # 确保此路径指向您的本地Firebase JSON文件
                    cred_info = json.load(f)
                cred = credentials.Certificate(cred_info)
            except FileNotFoundError as e:
                st.error(f'未找到本地Firebase憑證，請確保路徑正確並且文件存在。錯誤訊息：{e}')
                return False
            except Exception as e:
                st.error(f'讀取本地 Firebase 憑證出錯，錯誤訊息：{e}')
                return False

        try:
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://myproject01-be1b7-default-rtdb.asia-southeast1.firebasedatabase.app/'
            })
        except Exception as e:
            st.error(f'Firebase初始化失敗：{e}')
            return False
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

