import streamlit as st
import datetime
import requests
import random
import json
import os

MY_DISCORD_ID = "<@472746897812226059>" 

# --- HÀM XỬ LÝ DỮ LIỆU (PERSISTENCE) ---
def load_data():
    default_data = {
        "last_opened_date": "", 
        "opened_indices": [],
        "events": []
    }
    if os.path.exists("progress.json"):
        try:
            with open("progress.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if "events" not in data:
                    data["events"] = []
                return data
        except Exception:
            pass
    return default_data

def save_data(data):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def send_discord_message(content):
    webhook_url = "https://discord.com/api/webhooks/1488241713003892958/if86rMDuP_xW_8A-WlL90OpbeidNcfBQWNB35YxFl83C_BbPeuL2GWRSA_Ptbg0SjYa_" 
    data = {"content": content, "username": "Trạm Yêu Thương"}
    try:
        requests.post(webhook_url, json=data)
    except:
        pass

# --- HÀM QUÀ TẶNG ---
@st.dialog("Tèn ten! Quà của bé đâyyy 🎁")
def show_gift_popup(gift_item, is_new=True):
    if is_new:
        st.balloons()
    
    st.markdown(
        f"<h2 style='text-align: center; color: #ff4b4b; line-height: 1.5;'>{gift_item['text']}</h2>", 
        unsafe_allow_html=True
    )
    
    if gift_item.get("image"):
        st.image(gift_item["image"], use_container_width=True)
        
    st.write("")
    
    if st.button("Dạ yêuuu 🥰", use_container_width=True):
        st.rerun()

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="For You ❤️", page_icon="🎁", layout="centered")
st.title("Hi bé yêu của anh 🩵👋")
st.write("Chào mừng em đến với trạm tiếp sức năng lượng!")
st.divider()

# --- 2. HỘP QUÀ NGẪU NHIÊN ---
st.header("🎁 Hộp Quà Mỗi Ngày")
st.write("Mỗi ngày một điều bất ngờ nhỏ dành cho em!")
user_data = load_data()
today_str = str(datetime.date.today())

gifts = [
    {
        "text": "Gửi em một chiếc ôm to bự từ xa nèeee 🫂", 
        "image": "https://media.tenor.com/Z4XEqJk4kXEAAAAM/hug.gif"
    },
    {
        "text": "Bé bị phạt! Hình phạt là phải thơm anh 1 cái 😘", 
        "image": "https://media.tenor.com/2RoSIfK_R_AAAAAM/cat-kiss.gif"
    },
    {
        "text": "Anh sẽ luôn bảo vệ em như Howl bảo vệ Sophie vậy đó 🏰✨", 
        "image": "https://media.tenor.com/bX0m2gT5GkMAAAAM/howls-moving-castle.gif"
    },
    {
        "text": "Ting ting! Một suất gội đầu massage thư giãn miễn phí do chính tay anh phục vụ nha 💆‍♀️✨", 
        "image": "https://media.tenor.com/M22T2I3g5vMAAAAM/massages-meow.gif"
    },
    
    # Nhóm quà chỉ có chữ (giữ nguyên cảm xúc mộc mạc)
    {"text": "Hôm nay em cực kỳ xinh đẹp! ✨", "image": None},
    {"text": "Anh yêu em nhiều hơn ngày hôm qua ❤️", "image": None},
    {"text": "Một voucher: Được anh đấm bóp vai 15 phút 💆‍♀️", "image": None},
    {"text": "Em là điều tuyệt vời nhất từng đến với anh 🌟", "image": None},
    {"text": "Nụ cười của em là liều thuốc cho anh đó 😊", "image": None},
    {"text": "Chúc công chúa của anh một ngày thật năng suất nhé!", "image": None},
    {"text": "Em luôn đẹp trong mắt anh và lúc mãi mãi là vậy nên là đừng tự ti nhaa ❤️", "image": None},
    {"text": "Check tin nhắn của anh chuaa 👀", "image": None},
    {"text": "Chỉ muốn nói là nhớ em lắm, yêu bé lắm 🩵🥰", "image": None},
    {"text": "Bé nhớ nói 'dạ' với anh nhiều nhaa, anh thích lắm á, yêu cực luonn 🥹🥹", "image": None},
    {"text": "Bé muốn gì nhắn anh ngay nàooo, anh sẵn sàng roi đâyyy 🥰", "image": None},
    {"text": "Buồn nè, cười lên nhaa đừng buồn như zay nữa áaa! 😤🥰", "image": "lib/features/daily_gift/buon.jpg"}
]

if user_data["last_opened_date"] == today_str:
    gift_index = user_data["opened_indices"][-1]
    st.info("Nay em bé đã nhận quà roii. Mai quay lại nhaa! ❤️")
    if st.button("Xem lại quà hôm nay"):
        show_gift_popup(gifts[gift_index], is_new=False)
else:
    if st.button("Mở quà ngay 🎁", key="open_gift"):
        all_indices = list(range(len(gifts)))
        unopened_indices = [i for i in all_indices if i not in user_data["opened_indices"]]
        
        if not unopened_indices:
            user_data["opened_indices"] = []
            unopened_indices = all_indices
            st.toast("Bé mở hết quà rồi! Anh làm mới lại kho quà cho bé hehe ✨")
        
        new_index = random.choice(unopened_indices)
        user_data["last_opened_date"] = today_str
        user_data["opened_indices"].append(new_index)
        save_data(user_data)
        show_gift_popup(gifts[new_index])

st.divider()

# --- 3. BẢNG ĐẾM NGƯỢC ---
st.header("⏳ Các cột mốc sắp tới!")
today = datetime.date.today()
                    
if not user_data["events"]:
    st.write("Hiện chưa có lịch trình nào sắp tới. Anh sẽ cập nhật sau nha!")
else:
    for event in user_data["events"]:
        event_date = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        days_left = (event_date - today).days

        if days_left > 0:
            st.info(f"✨ Còn **{days_left} ngày** nữa là đến **{event['name']}**")
        elif days_left == 0:
            st.success(f"🎉 Hôm nay là **{event['name']}**! Quẩy thôi!")
        else:
            st.write(f"Đã qua: ~~{event['name']}~~")
            
with st.expander("➕ Thêm sự kiện đếm ngược mới"):
    new_event_name = st.text_input("Nội dung (VD: Sinh nhật anh, Đi Đà Lạt):")
    new_event_date = st.date_input("Chọn ngày:")
    
    if st.button("Lưu sự kiện"):
        if new_event_name:
            user_data["events"].append({
                "name": new_event_name,
                "date": str(new_event_date)
            })
            save_data(user_data)
            st.success("Đã thêm thành công!")
            st.rerun()
        else:
            st.error("Ghi nội dung vào đã nào!")

st.divider()

# --- 4. CỬA HÀNG COUPON ---
st.header("🎟️ Cửa hàng Vé Tình Yêu")
st.write("Bấm vào để dùng vé, anh sẽ biết ngay lập tức!")

row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)
row3_col1, row3_col2 = st.columns(2)

with row1_col1:
    st.markdown("### 🧋 Vé trà sữa")
    if st.button("Dùng vé", key="v_trasua"):
        st.toast("Đã báo anh mua Matcha Latte!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn uống Matcha Latte kìa! 🧋")

with row1_col2:
    st.markdown("### 🫂 Vé một cái ôm")
    if st.button("Dùng vé", key="v_om"):
        st.toast("Anh đang bay tới ôm bé đây!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé đang cần 1 cái ôm ngay lập tức! 🫂")

with row2_col1:
    st.markdown("### 🍳 Vé anh nấu ăn")
    if st.button("Dùng vé", key="v_nau"):
        st.toast("Menu hôm nay do bé chọn hết!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn ăn cơm anh nấu. Chuẩn bị vào bếp thôi! 👨‍🍳")

with row2_col2:
    st.markdown("### 😤 Vé giận 5 phút")
    if st.button("Dùng vé", key="v_gian"):
        st.toast("Đã báo anh chuẩn bị dỗ bé!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 CẢNH BÁO! Bé đang giận! Mau nhắn tin dỗ dành đi!!! 😤")

with row3_col1:
    st.markdown("### 🏰 Vé đi chơi")
    if st.button("Dùng vé", key="v_choi"):
        st.toast("Bé muốn đi đâu nàoo 🏍️")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn đi chơi cùng anh nè! 🍿")

with row3_col2:
    st.markdown("### ✨ Vé làm nũng")
    if st.button("Dùng vé", key="v_nung"):
        st.toast("Bé muốn làm nũng hãa, anh nghe nè!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn làm nũng rồi kìa, rep tin nhắn ngay! 🥺")

st.divider()

# --- 5. GÓC SOS ---
st.header("🚨 Góc Cấp Cứu (SOS)")
st.write("Tụt mood hay áp lực quá thì ấn vào đây nha 🥺")

if st.button("Cứu em!!!", type="primary"):
    st.toast("Đã phát tín hiệu cấp cứu cho anh! Anh sẽ onl liền. 🥺") 
    send_discord_message(f"{MY_DISCORD_ID} 🚨 BÁO ĐỘNG ĐỎ! Bé nhà đang TỤT MOOD/ÁP LỰC kìa! Nhắn tin dỗ dành ngay!!! 🥺")
    st.video("love.mp4") 
    st.caption("Anh luôn ở đây! Xem cái này cho đỡ buồn nha.")