import streamlit as st
import datetime
import requests
import random
import json
import os
import re
import streamlit.components.v1 as components

MY_DISCORD_ID = "<@472746897812226059>" 

# --- HÀM XỬ LÝ DỮ LIỆU (PERSISTENCE) ---
def load_data():
    default_data = {
        "last_opened_date": "", 
        "opened_indices": [],
        "events": [],
        "custom_coupons": [],
        "spotify_url": "https://open.spotify.com/embed/playlist/37i9dQZF1EJMlmaDUAhknC?utm_source=generator",
        "boyfriend_reply": ""
    }
    if os.path.exists("progress.json"):
        try:
            with open("progress.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if "events" not in data:
                    data["events"] = []
                if "spotify_url" not in data:
                    data["spotify_url"] = default_data["spotify_url"]
                if "custom_coupons" not in data: 
                    data["custom_coupons"] = []           
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

st.markdown("""
<style>
div.stButton > button {
    min-height: 55px; 
    font-size: 16px !important; 
    font-weight: 500 !important; 
    border-radius: 12px !important; 
}

div.stButton > button[kind="primary"] {
    min-height: 120px !important;
    font-size: 30px !important;
    font-weight: 900 !important;
    text-transform: uppercase;
    background-color: #FF0000 !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4) !important;
}

div.stButton > button[kind="primary"]:hover {
    background-color: #CC0000 !important; /* Đỏ sậm hơn chút khi hover */
}
</style>
""", unsafe_allow_html=True)

user_data = load_data()

st.title("Hi bé yêu của anh 🩵👋")

if user_data.get("boyfriend_reply"):
    st.success(f"💌 **Tin nhắn từ anh:** {user_data['boyfriend_reply']}")
else:
    st.write("Chào mừng em đến với trạm tiếp sức năng lượng!")
    
st.divider()

# --- TRẠM PHÁT NHẠC ---
st.header("🎵 Playlist chung của mình nè!")
raw_spotify_link = user_data.get("spotify_url", "")

if raw_spotify_link:
    embed_link = raw_spotify_link.strip().split("?")[0]
    
    embed_link = re.sub(r'intl-[a-zA-Z0-9]+/', '', embed_link)
    
    if "spotify.com/" in embed_link and "/embed/" not in embed_link:
        embed_link = embed_link.replace("spotify.com/", "spotify.com/embed/")
        
    components.html(
        f'<iframe style="border-radius:12px" src="{embed_link}" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>',
        height=360
    )
st.divider()


# --- 2. HỘP QUÀ NGẪU NHIÊN ---
st.header("🎁 Hộp Quà Mỗi Ngày")
st.write("Mỗi ngày một điều bất ngờ nhỏ dành cho em!")
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
    for index, event in enumerate(user_data["events"]):
        event_date = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        days_left = (event_date - today).days
        vn_date_str = event_date.strftime("%d/%m/%Y")

        col_text, col_btn = st.columns([0.85, 0.15])
        with col_text:
            if days_left > 0:
                st.info(f"✨ Còn **{days_left} ngày**: **{event['name']}** ({vn_date_str})")
            elif days_left == 0:
                st.success(f"🎉 Hôm nay là **{event['name']}** ({vn_date_str})! Quẩy thôi!")
            else:
                st.write(f"Đã qua: ~~{event['name']} ({vn_date_str})~~")
        
        with col_btn:
            if st.button("❌", key=f"del_{index}", help="Xóa sự kiện này"):
                user_data["events"].pop(index)
                save_data(user_data)
                st.rerun()
            
with st.expander("➕ Thêm sự kiện đếm ngược mới"):
    new_event_name = st.text_input("Nội dung (VD: Ngày đi chơi, Đi Đà Lạt, ...):")
    new_event_date = st.date_input("Chọn ngày:", format="DD/MM/YYYY") 
    
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

# A. Các vé mặc định
st.subheader("Vé mặc định")
c1, c2 = st.columns(2)
with c1:
    if st.button("🧋 Vé trà sữa", use_container_width=True):
        st.toast("Đã báo anh mua Matcha Latte!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn uống Matcha Latte kìa! 🧋")
    if st.button("🍳 Vé anh nấu ăn", use_container_width=True):
        st.toast("Menu hôm nay do bé chọn hết!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn ăn cơm anh nấu! 👨‍🍳")
    if st.button("🏰 Vé đi chơi", use_container_width=True):
        st.toast("Bé muốn đi đâu nàoo 🏍️")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn đi chơi cùng anh nè! 🍿")
with c2:
    if st.button("🫂 Vé một cái ôm", use_container_width=True):
        st.toast("Anh đang bay tới ôm bé đây!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé đang cần 1 cái ôm! 🫂")
    if st.button("😤 Vé giận 5 phút", use_container_width=True):
        st.toast("Đã báo anh chuẩn bị dỗ bé!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 CẢNH BÁO! Bé đang giận! Mau dỗ đi! 😤")
    if st.button("✨ Vé làm nũng", use_container_width=True):
        st.toast("Bé muốn làm nũng hãa, anh nghe nè!")
        send_discord_message(f"{MY_DISCORD_ID} 🚨 TING TING! Bé muốn làm nũng rồi kìa! 🥺")

# B. Các vé tự chế (Custom)
if user_data["custom_coupons"]:
    st.write("")
    st.subheader("Vé do bé tự chế ✨")
    for i in range(0, len(user_data["custom_coupons"]), 2):
        cols = st.columns(2)
        for j in range(2):
            idx = i + j
            if idx < len(user_data["custom_coupons"]):
                coupon = user_data["custom_coupons"][idx]
                with cols[j]:
                    cc1, cc2 = st.columns([0.8, 0.2])
                    with cc1:
                        icon = coupon.get("emoji", "🎫")
                        if st.button(f"{icon} {coupon['name']}", key=f"use_c_{idx}", use_container_width=True):
                            st.toast(f"Đã dùng vé {coupon['name']}!")
                            send_discord_message(f"{MY_DISCORD_ID} 🎫 **VÉ TỰ CHẾ:** Bé vừa dùng vé **[{coupon['name']}]**! Chuẩn bị tinh thần nha! 😂")
                    with cc2:
                        if st.button("🗑️", key=f"del_c_{idx}", help="Xóa vé này"):
                            user_data["custom_coupons"].pop(idx)
                            save_data(user_data)
                            st.rerun()

with st.expander("🎨 Tự tạo vé mới theo ý bé"):
    col_emj, col_text = st.columns([0.25, 0.75])
    with col_emj:
        custom_emoji = st.text_input("Icon:", value="🎫", max_chars=2, help="Dùng bàn phím đt để chọn Icon")
    with col_text:
        custom_name = st.text_input("Tên vé (VD: Vé được đi nhậu, Vé được bắt anh im lặng...):")
        
    if st.button("Tạo vé ngay", use_container_width=True):
        if custom_name:
            user_data["custom_coupons"].append({
                "name": custom_name,
                "emoji": custom_emoji if custom_emoji else "🎫"
            })
            save_data(user_data)
            st.success(f"Đã tạo vé thành công!")
            st.rerun()

st.divider()

# --- 5. HÒM THƯ BÍ MẬT ---
st.header("💌 Hòm Thư Tâm Sự")
st.write("Có điều gì muốn nói, hay tự nhiên muốn đòi quà thì bé cứ nhắn vào đây nha!")
tam_su = st.text_area("Bé gõ vào đây nè:", placeholder="Ví dụ: Tự nhiên thèm ăn lẩu quá anh ơiii...", height=100)

if st.button("Gửi cho anh 🚀", use_container_width=True):
    if tam_su.strip() == "":
        st.warning("Bé chưa gõ gì kìa!")
    else:
        st.toast("Đã gửi thư thành công! Đợi anh check nhaa.")
        send_discord_message(f"{MY_DISCORD_ID} 💌 **THƯ TỪ BÉ YÊU:**\n> {tam_su}")

with st.expander("Góc của anh 👀)"):
    loi_nhan_moi = st.text_input("Gõ lời nhắn để rep bé:", value=user_data.get("boyfriend_reply", ""))
    col_save, col_del = st.columns(2)
    with col_save:
        if st.button("Cập nhật lời nhắn", use_container_width=True):
            user_data["boyfriend_reply"] = loi_nhan_moi
            save_data(user_data)
            st.rerun()
    with col_del:
        if st.button("Xóa lời nhắn", use_container_width=True):
            user_data["boyfriend_reply"] = ""
            save_data(user_data)
            st.rerun()
st.divider()

# --- 6. GÓC SOS ---
st.markdown("<h2 style='text-align: center;'>🚨 Góc Cấp Cứu</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; margin-top: -15px;'>Tụt mood hay áp lực quá thì ấn vào đây nha 🥺</p>", unsafe_allow_html=True)

sos_c1, sos_c2, sos_c3 = st.columns([1, 5, 1])

with sos_c2:
    if st.button("Cứu em!!!", type="primary", use_container_width=True, key="sos_btn"):
        st.toast("Đã phát tín hiệu cấp cứu!") 
        send_discord_message(f"{MY_DISCORD_ID} 🚨 BÁO ĐỘNG ĐỎ! Bé nhà đang TỤT MOOD/ÁP LỰC kìa! Nhắn tin dỗ dành ngay!!! 🥺")
        st.video("love.mp4") 
        st.caption("Anh luôn ở đây! Xem cái này cho đỡ buồn nha.")
st.write("")
st.write("")