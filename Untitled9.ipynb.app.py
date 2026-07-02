{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMze/mCF+hqOaxDsoGGZFHN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ParkSHyeon2456/blank-app/blob/main/Untitled9.ipynb.app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ws9ra--Cs6uy",
        "outputId": "b3fd559d-b25e-4a39-91f5-62dc9c88cb17"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- [QC 검사 보고서] ---\n",
            "기록 ID: 1 | 유저 ID: 101\n",
            "농도: 15% | 상태: 파랑에 가까운 퍼플\n",
            "내용: 오늘따라 위로가 필요해\n",
            "사진 첨부: 있음\n",
            "--------------------------\n",
            "\n",
            "--- [QC 검사 보고서] ---\n",
            "기록 ID: 2 | 유저 ID: 101\n",
            "농도: 50% | 상태: 퍼플 원색\n",
            "내용: 정말 완벽한 균형의 날이야\n",
            "사진 첨부: 없음\n",
            "--------------------------\n",
            "\n",
            "--- [QC 검사 보고서] ---\n",
            "기록 ID: 3 | 유저 ID: 101\n",
            "농도: 85% | 상태: 레드에 가까운 퍼플\n",
            "내용: 열정이 솟구친다!\n",
            "사진 첨부: 있음\n",
            "--------------------------\n",
            "\n"
          ]
        }
      ],
      "source": [
        "# 퍼플 밸런스 데이터 모델 및 로직 시뮬레이션 코드\n",
        "\n",
        "# 1. 보라색 농도 구간 판정 로직 (QC 품질 표준)\n",
        "def get_purple_status(intensity):\n",
        "    if intensity == 0: return \"블루 (Blue)\"\n",
        "    elif 1 <= intensity <= 30: return \"파랑에 가까운 퍼플\"\n",
        "    elif 31 <= intensity <= 49: return \"진한 퍼플\"\n",
        "    elif intensity == 50: return \"퍼플 원색\"\n",
        "    elif 51 <= intensity <= 70: return \"연한 퍼플\"\n",
        "    elif 71 <= intensity <= 99: return \"레드에 가까운 퍼플\"\n",
        "    elif intensity == 100: return \"레드 (Red)\"\n",
        "    else: return \"측정 불가\"\n",
        "\n",
        "# 2. 데이터 구조 시뮬레이션 (Daily_Log 레코드 예시)\n",
        "def check_record(record_id, user_id, intensity, content, has_photo=False):\n",
        "    status = get_purple_status(intensity)\n",
        "    print(f\"--- [QC 검사 보고서] ---\")\n",
        "    print(f\"기록 ID: {record_id} | 유저 ID: {user_id}\")\n",
        "    print(f\"농도: {intensity}% | 상태: {status}\")\n",
        "    print(f\"내용: {content}\")\n",
        "    print(f\"사진 첨부: {'있음' if has_photo else '없음'}\")\n",
        "    print(f\"--------------------------\\n\")\n",
        "\n",
        "# 3. 테스트 데이터 입력 (품질 검사)\n",
        "check_record(1, 101, 15, \"오늘따라 위로가 필요해\", has_photo=True)\n",
        "check_record(2, 101, 50, \"정말 완벽한 균형의 날이야\", has_photo=False)\n",
        "check_record(3, 101, 85, \"열정이 솟구친다!\", has_photo=True)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit -q\n",
        "import streamlit as st\n",
        "\n",
        "# UI 제목\n",
        "st.title(\"💜 퍼플 밸런스 (Purple Balance)\")\n",
        "\n",
        "# 1. 농도 게이지 (가상의 50%)\n",
        "intensity = st.slider(\"오늘의 보라색 농도를 확인하세요\", 0, 100, 50)\n",
        "st.write(f\"현재 농도: {intensity}%\")\n",
        "\n",
        "# 2. 입력 섹션\n",
        "col1, col2 = st.columns(2)\n",
        "with col1:\n",
        "    photo = st.file_uploader(\"사진 업로드\")\n",
        "with col2:\n",
        "    keyword = st.text_input(\"오늘의 키워드를 입력하세요\")\n",
        "\n",
        "# 3. 감정 선택\n",
        "emotion = st.radio(\"오늘의 감정 상태는?\", (\"블루(위로)\", \"레드(열정)\"))\n",
        "\n",
        "# 4. 저장 버튼\n",
        "if st.button(\"기록 저장하기\"):\n",
        "    st.success(f\"저장 완료! {keyword} 기록이 반영되었습니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fx9vccyHtjqo",
        "outputId": "6346fb3b-1a1c-4cbc-d8be-ad8540aa7150"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.2/9.2 MB\u001b[0m \u001b[31m55.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m82.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-07-02 07:25:05.217 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.346 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-07-02 07:25:05.347 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.349 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.350 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.350 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.351 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.353 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.353 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.355 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.357 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.358 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.359 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.360 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.361 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.362 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.363 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.364 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.365 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.366 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.367 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.369 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.370 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.370 Session state does not function when running a script without `streamlit run`\n",
            "2026-07-02 07:25:05.371 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.372 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.373 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.374 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.377 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.380 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.380 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-02 07:25:05.386 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}