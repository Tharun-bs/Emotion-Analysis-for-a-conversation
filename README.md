# Emotion-Analysis-for-a-conversation
This web app allows users to analyze the emotional tone of a conversation using the powerful transformer model j-hartmann/emotion-english-distilroberta-base. Built with Streamlit for an intuitive and interactive frontend, this tool helps in visualizing and understanding how emotions shift throughout a dialogue.
# 🧠 Emotion Analysis of Conversations

This project is a Streamlit-based web app that performs **emotion classification** on conversational text using the pre-trained transformer model [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base).

## 📌 Overview

The app takes a multi-turn conversation as input (e.g., dialogue between people) and identifies the **emotional tone of each sentence or utterance**. It also visualizes emotional trends across the conversation using bar charts and emotion timelines.

---

## 🚀 Features

- 💬 Analyze multi-turn dialogues for emotional content
- 🎭 Supports 7 emotion classes:
  - `joy`, `anger`, `sadness`, `fear`, `surprise`, `disgust`, `neutral`
- 📊 Visualizations:
  - Emotion distribution bar chart
  - Timeline of emotion across utterances
- 📈 Summary stats like:
  - Start emotion vs End emotion
  - Most frequent emotion
- ⚡ Lightweight and fast with DistilRoBERTa model
