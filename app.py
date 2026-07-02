import streamlit as st

# 1. 보라색 농도 구간 판정 로직
def get_purple_status(intensity):
    if intensity == 0: return "블루 (Blue)"
    elif 1 <= intensity <= 30: return "파랑에 가까운 퍼플"
    elif 31 <= intensity <= 49: return "진한 퍼플"
    elif intensity == 50: return "퍼플 원색"
    elif 51 <= intensity <= 70: return "연한 퍼플"
    elif 71 <= intensity <= 99: return "레드에 가까운 퍼플"
    elif intensity == 100: return "레드 (Red)"
    else: return "측정 불가"

# 2. UI 구성
st.title("💜 퍼플 밸런스 (Purple Balance)")

# 3. 입력 섹션
intensity = st.slider("오늘의 보라색 농도를 확인하세요", 0, 100, 50)
status = get_purple_status(intensity)
st.write(f"현재 농도: {intensity}% | 상태: **{status}**")

col1, col2 = st.columns(2)
with col1:
    photo = st.file_uploader("사진 업로드")
with col2:
    keyword = st.text_input("오늘의 키워드를 입력하세요")

emotion = st.radio("오늘의 감정 상태는?", ("블루(위로)", "레드(열정)"))

# 4. 저장 버튼
if st.button("기록 저장하기"):
    st.success(f"저장 완료! '{keyword}' 기록이 성공적으로 반영되었습니다.")
