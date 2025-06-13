from transformers import pipeline

# Load emotion classifier
emotion_classifier = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    top_k=1
)

def get_emotion(text):
    try:
        prediction = emotion_classifier(text)[0][0]
        return prediction['label']
    except:
        return "Neutral"

def analyze_conversation(convo_text):
    lines = [line.strip() for line in convo_text.strip().split('\n') if line.strip()]
    if len(lines) < 2:
        return None, None, {}

    start_lines = lines[:len(lines)//2]
    end_lines = lines[len(lines)//2:]

    def extract_emotions(lines):
        emotions = []
        speaker_emotions = {}
        for line in lines:
            if ':' in line:
                speaker, msg = line.split(':', 1)
                emotion = get_emotion(msg.strip())
                speaker = speaker.strip()
                emotions.append(emotion)
                if speaker not in speaker_emotions:
                    speaker_emotions[speaker] = []
                speaker_emotions[speaker].append(emotion)
        return emotions, speaker_emotions

    start_emotions, start_speakers = extract_emotions(start_lines)
    end_emotions, end_speakers = extract_emotions(end_lines)

    speaker_results = {}
    for speaker in set(start_speakers.keys()).union(end_speakers.keys()):
        start = start_speakers.get(speaker, ["Neutral"])[0]
        end = end_speakers.get(speaker, ["Neutral"])[-1]
        speaker_results[speaker] = {"start": start, "end": end}

    return start_emotions, end_emotions, speaker_results

