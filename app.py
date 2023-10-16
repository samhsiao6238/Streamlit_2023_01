import streamlit as st
import json
import os

def main():
    st.title("檢查並讀取 Streamlit Secrets")

    # 判斷是否在 Streamlit Sharing 或其他平台上運行
    if os.environ.get('STREAMLIT_SHARING', '').lower() == 'true' or os.environ.get('DEPLOYMENT_PLATFORM', '').lower() == 'true':

        # 讀取 db_username 和 db_password
        db_username = st.secrets.get('db_username', None)
        db_password = st.secrets.get('db_password', None)

        st.write(f"DB 使用者名稱: {db_username}")
        st.write(f"DB 密碼: {'*' * len(db_password) if db_password else None}")  # 顯示為星號以保密

        # 讀取 items
        items = st.secrets.get('items', None)
        st.write(f"項目清單: {', '.join(items) if items else None}")

        # 讀取 FIREBASE_CONFIG_STR
        firebase_config_str = st.secrets.get('FIREBASE_CONFIG_STR', None)
        if firebase_config_str:
            try:
                firebase_config = json.loads(firebase_config_str)
                st.write("Firebase 憑證已讀取，以下是部分信息：")
                st.write(f"Project ID: {firebase_config.get('project_id')}")
                st.write(f"Client Email: {firebase_config.get('client_email')}")
            except json.JSONDecodeError:
                st.error("讀取 Firebase 憑證時 JSON 解析失敗。")
    else:
        st.write("您目前在本地運行，沒有設定 secrets。")

if __name__ == "__main__":
    main()
