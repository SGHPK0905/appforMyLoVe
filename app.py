import streamlit as st
import datetime
import requests

def send_discord_message(content):
    webhook_url = "https://discord.com/api/webhooks/1488241713003892958/if86rMDuP_xW_8A-WlL90OpbeidNcfBQWNB35YxFl83C_BbPeuL2GWRSA_Ptbg0SjYa_" 
    
    data = {
        "content": content,
        "username": "Trạm Yêu Thương"
    }
    
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        st.error("Lỗi gửi thông báo rồi!")

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="For You ❤️", page_icon="🎁", layout="centered")

st.title("Hi bé yêu của anh 🩵👋")
st.write("Chào mừng em đến với trạm tiếp sức năng lượng!")

st.divider()

# --- 2. BẢNG ĐẾM NGƯỢC ---
st.header("⏳ Đang đếm ngược nè!")

target_date = datetime.date(2026, 4, 1) 
today = datetime.date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.info(f"Chỉ còn **{days_left} ngày** nữa là đến ngày gặp nhau roii 😊")
elif days_left == 0:
    st.success("Hôm nay là ngày đi chơi! Lên đồ thôi! 🎉")
else:
    st.write("Chúng ta đã có một chuyến đi thật vui!")

st.divider()

# --- 3. CỬA HÀNG COUPON (Kết hợp Discord sau) ---
st.header("🎟️ Cửa hàng Vé Tình Yêu")
st.write("Bấm vào để dùng vé, anh sẽ biết ngay lập tức!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧋 Vé buồn miệng")
    if st.button("Dùng vé này", key="trasua"):
        st.toast("Đã gửi tín hiệu đòi Matcha Latte cho anh! Đợi tí nhé.") 
        send_discord_message("@sghpk0905 🚨 TING TING! Bé nhà vừa dùng 1 Vé Trà Sữa. Mua mau lên!! 🧋")

with col2:
    st.markdown("### 🫂 Vé Một Cái Ôm")
    if st.button("Dùng vé này", key="om"):
        st.toast("Ting ting! Đã báo cho anh. Chuẩn bị anh bay tới ôm em nè.")
        send_discord_message("@sghpk0905 🚨 TING TING! Bé nhà đang cần 1 Cái Ôm ngay lập tức!! 🫂")

st.divider()

st.header("🚨 Góc Cấp Cứu (SOS)")
st.write("Tụt mood hay áp lực quá thì ấn vào đây nha 🥺")

if st.button("Cứu em!!!", type="primary"):
    st.video("love.mp4") 
    st.caption("Anh luôn ở đây! Xem cái này cho đỡ buồn nha.")