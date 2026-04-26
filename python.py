import streamlit as st
import random

# Page Config
st.set_page_config(page_title="AI Study Planner", page_icon="📚", layout="centered")

# Title
st.title("📚 AI Mood-Based Study Planner")
st.write("Plan your study sessions based on your mood and energy 💡")

# Mood Selection
mood = st.selectbox("How are you feeling today?",
                    ["😊 Happy", "😐 Neutral", "😫 Tired", "😔 Sad"])

# Study Time Input
time = st.slider("How many hours can you study today?", 1, 8, 2)

# Subject Input
subjects = st.text_input("Enter subjects (comma separated)",
                         "Math, English, Computer")

# Motivational Quotes
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success starts with self-discipline.",
    "Small progress is still progress.",
    "Dream big. Start small. Act now."
]

# Study Plan Logic
def generate_plan(mood, time, subjects):
    subjects = subjects.split(",")
    plan = []

    if "Tired" in mood or "Sad" in mood:
        duration = max(20, int((time * 60) / len(subjects)))
    else:
        duration = int((time * 60) / len(subjects))

    for sub in subjects:
        plan.append(f"📖 Study {sub.strip()} for {duration} minutes")

    return plan

# Generate Button
if st.button("Generate Study Plan 🚀"):
    plan = generate_plan(mood, time, subjects)

    st.subheader("📅 Your Study Plan:")
    for p in plan:
        st.write(p)

    st.subheader("💬 Motivation:")
    st.success(random.choice(quotes))

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")