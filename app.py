import streamlit as st

# 1. 보라색 농도 및 색상 로직 (QC 표준)
def get_purple_style(intensity):
    if intensity == 0: return "블루", "#3b82f6"
    elif 1 <= intensity <= 30: return "파랑에 가까운 퍼플", "#7e22ce"
    elif 31 <= intensity <= 49: return "진한 퍼플", "#9333ea"
    elif intensity == 50: return "퍼플 원색", "#a855f7"
    elif 51 <= intensity <= 70: return "연한 퍼플", "#c084fc"
    elif 71 <= intensity <= 99: return "레드에 가까운 퍼플", "#ef4444"
    elif intensity == 100: return "레드", "#dc2626"
    return "측정 불가", "#000000"

# 2. UI 구성
st.title("💜 퍼플 밸런스 (Purple Balance)")

# 농도 슬라이더
intensity = st.slider("오늘의 보라색 농도를 설정하세요", 0, 100, 50)
status_text, color_code = get_purple_style(intensity)

# 시각적 변화 (색상 박스 및 상태)
st.markdown(f"""
    <div style="background-color: {color_code}; padding: 20px; border-radius: 10px; color: white; text-align: center;">
        <h2>{status_text} ({intensity}%)</h2>
    </div>
""", unsafe_allow_html=True)

# 달성도 게이지
st.write("### 밸런스 달성도")
st.progress(intensity / 100)

# 입력 섹션
col1, col2 = st.columns(2)
with col1:
    photo = st.file_uploader("사진 업로드", type=['png', 'jpg', 'jpeg'])
    if photo is not None:
        st.image(photo, caption="업로드한 일상", use_column_width=True)
with col2:
    keyword = st.text_input("오늘의 키워드를 입력하세요 (Enter를 누르세요)")
    emotion = st.radio("오늘의 감정 상태는?", ("블루(위로)", "레드(열정)"))

# 4. 저장 버튼
if st.button("기록 저장하기"):
    if keyword:
        st.success(f"저장 완료! '{keyword}'({emotion}) 기록이 반영되었습니다.")
    else:
        st.warning("키워드를 입력해 주세요!")
