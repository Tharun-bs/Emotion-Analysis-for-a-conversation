import streamlit as st
from utils.emotion_analyzer import analyze_conversation
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

st.set_page_config(page_title="Emotion Analyzer", layout="centered")

st.title("🧠 Emotion Analysis of Multi-Person Conversation")
st.markdown("Paste a **conversation** between 3 people (format: `Name: sentence`)")

conversation = st.text_area("Conversation:", height=250, placeholder="""
Alice: I’m feeling down today.
Bob: What happened?
Charlie: We’re here for you.
Alice: Just work pressure.
Bob: You’ve got this!
Charlie: Let's go for a walk.
Alice: That sounds great, thank you all.
""")

if st.button("Analyze"):
    if conversation.strip():
        start_emotions, end_emotions, speaker_results = analyze_conversation(conversation)

        st.subheader("🔍 Overall Emotion Summary")
        from collections import Counter

        # Get most common emotion
        most_common_start = Counter(start_emotions).most_common(1)[0][0]
        most_common_end = Counter(end_emotions).most_common(1)[0][0]

        st.markdown(f"**🟡 Overall Start Emotion:** `{most_common_start}`")
        st.markdown(f"**🟢 Overall End Emotion:** `{most_common_end}`")

        st.subheader("🗣️ Speaker-wise Emotion Transition")
        for speaker, res in speaker_results.items():
            st.write(f"- **{speaker}**: {res['start']} ➡️ {res['end']}")
    else:
        st.warning("Please enter a conversation to analyze.")
