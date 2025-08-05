import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import speech_recognition as sr
import subprocess
import os
import time

backend_url = st.secrets.get("BACKEND_URL", "http://localhost:8000")

# Start the FastAPI server (only once)
if not os.path.exists("fastapi_started.txt"):
    with open("fastapi_started.txt", "w") as f:
        f.write("started")
    subprocess.Popen(["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"])
    time.sleep(3)  # Give FastAPI a few seconds to boot

st.set_page_config(page_title="MindMosaic", layout="wide")

# Session initialization
if "username" not in st.session_state:
    st.session_state.username = ""
if "analysis" not in st.session_state:
    st.session_state.analysis = None

st.title("🧠 MindMosaic - Mental Health Journal")

# 🔐 Login Page
if not st.session_state.username:
    st.subheader("🔐 Login")
    username_input = st.text_input("Enter your username")
    if st.button("Login"):
        res = requests.post(f"{backend_url}/login", json={"username": username_input})
        if res.status_code == 200:
            st.session_state.username = username_input
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Login failed")
else:
    st.subheader(f"Welcome, {st.session_state.username}!")

    if st.button("Logout"):
        st.session_state.username = ""
        st.session_state.analysis = None
        st.rerun()

    # Journal Entry Box
    entry = st.text_area("Write your thoughts:", height=200)

    if st.button("🎙️ Use Voice to Journal"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            audio = recognizer.listen(source)
            try:
                entry = recognizer.recognize_google(audio)
                st.success("Transcribed Entry: " + entry)
            except sr.UnknownValueError:
                st.warning("Sorry, could not understand audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results; {e}")

    if st.button("Analyze My Entry"):
        with st.spinner("Analyzing..."):
            response = requests.post(f"{backend_url}/analyze", json={
                "username": st.session_state.username,
                "text": entry
            })
            if response.status_code == 200:
                st.session_state.analysis = response.json()
            else:
                st.error("Something went wrong.")

    # ✅ Display Analysis Results
    if st.session_state.analysis:
        data = st.session_state.analysis
        st.success(f"Emotion: {data['emotion'].capitalize()}")
        st.info(data['feedback'])

        # 🎯 Suggested Activities Box
        with st.expander("🎯 Suggested Activities to Improve Your Mood", expanded=True):
            st.write(f"💡 Primary Suggestion: {data['suggestions'][0]}")

            if data['emotion'] not in ["happy", "neutral"]:
                uplift_response = requests.get(f"{backend_url}/uplift/{data['emotion']}")
                if uplift_response.status_code == 200:
                    uplift = uplift_response.json()
                    for suggestion in uplift.get("activities", []):
                        st.markdown(f"✅ {suggestion}")

        if st.button("Clear Analysis"):
            st.session_state.analysis = None

    # 📊 Mood Trends and Visualizations
    st.markdown("---")
    st.subheader("📊 Emotion Trend")
    if st.button("Show Chart"):
        hist = requests.get(f"{backend_url}/history/{st.session_state.username}")
        df = pd.DataFrame(hist.json())

        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            fig = px.line(df, x="timestamp", y="emotion", title="Mood Trend")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📊 Emotion Distribution")
            emotion_counts = df["emotion"].value_counts().reset_index()
            emotion_counts.columns = ["emotion", "count"]
            pie_fig = px.pie(emotion_counts, names="emotion", values="count", title="Overall Emotion Breakdown")
            st.plotly_chart(pie_fig, use_container_width=True)

            st.subheader("📊 Emotion Frequency Over Time")
            bar_df = df.groupby(["emotion", pd.Grouper(key="timestamp", freq="W")]).size().reset_index(name="count")
            bar_fig = px.bar(bar_df, x="timestamp", y="count", color="emotion", title="Weekly Emotion Frequency")
            st.plotly_chart(bar_fig, use_container_width=True)

            st.subheader("🗓️ Journaling Activity")
            df["date"] = df["timestamp"].dt.date
            count_df = df.groupby("date").size().reset_index(name="entries")
            habit_fig = px.line(count_df, x="date", y="entries", title="Daily Journal Count")
            st.plotly_chart(habit_fig, use_container_width=True)

    # 🔎 Semantic Search
    st.markdown("---")
    st.subheader("🔎 Semantic Search")
    search_text = st.text_input("Search your journal")
    if st.button("Search"):
        results = requests.post(f"{backend_url}/search", json={
            "username": st.session_state.username,
            "query": search_text
        })
        if results.status_code == 200:
            for i, result in enumerate(results.json(), 1):
                st.write(f"{i}. {result}")
        else:
            st.error("Search failed")