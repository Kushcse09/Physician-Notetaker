# app.py

import streamlit as st
import json

# Placeholder functions – replace with your actual logic or import from modules
from transformers import pipeline
import spacy

# Load spaCy model (use en_core_web_sm or en_core_sci_sm if you use scispaCy)
nlp = spacy.load("en_core_web_sm")

# -------- Sample Logic Start (replace with yours) --------
def extract_entities(text):
    doc = nlp(text)
    symptoms, treatments, diagnosis, prognosis = [], [], "", ""
    for ent in doc.ents:
        if ent.label_ == "NORP" or "pain" in ent.text.lower():
            symptoms.append(ent.text)
        elif "therapy" in ent.text.lower():
            treatments.append(ent.text)
    diagnosis = "Whiplash injury"
    prognosis = "Full recovery expected within six months"
    return {
        "Symptoms": list(set(symptoms)),
        "Diagnosis": diagnosis,
        "Treatment": list(set(treatments)),
        "Prognosis": prognosis
    }

def summarize_transcript(text):
    return {
        "Patient_Name": "Janet Jones",
        "Symptoms": ["Neck pain", "Back pain", "Head impact"],
        "Diagnosis": "Whiplash injury",
        "Treatment": ["10 physiotherapy sessions", "Painkillers"],
        "Current_Status": "Occasional backache",
        "Prognosis": "Full recovery expected within six months"
    }

def analyze_sentiment_intent(text):
    return {
        "Sentiment": "Anxious",
        "Intent": "Seeking reassurance"
    }

def generate_soap_note(text):
    return {
        "Subjective": {
            "Chief_Complaint": "Neck and back pain",
            "History_of_Present_Illness": "Patient had a car accident, experienced pain for four weeks, now occasional back pain."
        },
        "Objective": {
            "Physical_Exam": "Full range of motion in cervical and lumbar spine, no tenderness.",
            "Observations": "Patient appears in normal health, normal gait."
        },
        "Assessment": {
            "Diagnosis": "Whiplash injury and lower back strain",
            "Severity": "Mild, improving"
        },
        "Plan": {
            "Treatment": "Continue physiotherapy as needed, use analgesics for pain relief.",
            "Follow-Up": "Patient to return if pain worsens or persists beyond six months."
        }
    }
# -------- Sample Logic End --------


# Streamlit UI
st.title("Physician Notetaker - AI Medical NLP Assistant")

st.markdown("""
This app processes physician-patient transcripts and extracts medical information using AI techniques:
- Named Entity Recognition
- Medical Summary
- Sentiment & Intent Detection
- SOAP Note Generation (Bonus)
""")

transcript_input = st.text_area("Paste the physician-patient transcript below:", height=300)

if st.button("Run Analysis"):
    if not transcript_input.strip():
        st.error("Please enter a transcript to analyze.")
    else:
        with st.spinner("Processing..."):

            # Run all modules
            ner = extract_entities(transcript_input)
            summary = summarize_transcript(transcript_input)
            sentiment_intent = analyze_sentiment_intent(transcript_input)
            soap = generate_soap_note(transcript_input)

        st.subheader("1. Named Entity Recognition (NER)")
        st.json(ner)

        st.subheader("2. Medical Summary")
        st.json(summary)

        st.subheader("3. Sentiment & Intent Analysis")
        st.json(sentiment_intent)

        st.subheader("4. SOAP Note Generation")
        st.json(soap)

st.markdown("---")
st.caption("Developed by Kushal Mahesh Handigund")
