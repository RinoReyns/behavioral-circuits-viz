"""
app.py — Streamlit interactive tool entry point.
Run with: streamlit run src/tool/app.py

Flow:
  1. User inputs a prompt
  2. Model runs + activations extracted
  3. Probes applied at each layer
  4. Causal scores loaded (or computed)
  5. Behavior Flow Map rendered inline
"""
import streamlit as st

st.set_page_config(page_title="Behavioral Circuits Viz", layout="wide")
st.title("🧠 Behavioral Circuits Visualizer")
st.info("Tool under construction — connect src/model, src/probes, and src/visualization.")
