'''
pip install toml
'''

import streamlit as st
import os
import toml

# 檢查是否存在標識本地運行的檔案
if os.path.exists(".LOCAL"):
    # 在本地運行
    with open("secrets.toml", "r") as file:
        st.secrets = toml.load(file)
else:
    # 在伺服器上運行，Streamlit 會自動載入默認的 secrets.toml
    pass

st.write("DB 使用者名稱:", st.secrets["db_username"])
st.write("DB 密碼:", st.secrets["db_password"])
# 
st.write("私密的項目清單", st.secrets["secrets"]["items"])
#
st.write("從項目清單取出指定的第二個物件:", st.secrets["secrets"]["items"][1])
#
if not os.path.exists(".LOCAL"):
    st.write("這部分是觀察 os 設定值與 st 設定值是否一致", os.environ["db_username"] == st.secrets["db_username"])