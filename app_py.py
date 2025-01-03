# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-vHlweHBxp027FOV2lh4bxn3yf3I7D7Z
"""

!pip install openai
!pip install transformers
!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import openai
# from transformers import pipeline
# import streamlit as st
# import random
# 
# illness_remedies = {
#     'cold': ['Drink warm water with honey and ginger.', 'Rest and stay hydrated.'],
#     'fever': ['Drink fluids like water and herbal tea.', 'Take a lukewarm bath to reduce the fever.'],
#     'headache': ['Apply a cold compress to the forehead.', 'Drink water and rest in a quiet place.'],
#     'stomach ache': ['Drink warm ginger tea.', 'Eat bland foods like rice or bananas.'],
#     # Add more illnesses and remedies as needed
# }
# 
# openai.api_key = "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"  # Replace with your OpenAI key
# 
# def identify_illness(problem, duration, symptoms):
#     prompt = f"User has the following symptoms: {symptoms}. The problem is: {problem} and has been going on for {duration}. What is the likely illness and its home remedy?"
# 
#     # Query GPT model
#     response = openai.Completion.create(
#         model="text-davinci-003",  # You can change to another GPT model
#         prompt=prompt,
#         max_tokens=150,
#         temperature=0.7
#     )
# 
#     return response.choices[0].text.strip()
# 
# def chatbot_interface():
#     st.title("AI Health Chatbot")
# 
#     # Get user inputs
#     problem = st.text_input("What is your health problem?")
#     duration = st.text_input("How long have you been experiencing this?")
#     symptoms = st.text_area("List your symptoms (separate with commas):")
# 
#     # When the button is pressed
#     if st.button("Get Home Remedy"):
#         if problem and duration and symptoms:
#             illness = identify_illness(problem, duration, symptoms)
# 
#             # Check if the illness has a predefined remedy
#             illness_name = illness.split()[0].lower()  # Extract illness name
#             remedy = illness_remedies.get(illness_name, ["No specific remedy found for this illness."])
# 
#             st.write(f"Identified Illness: {illness}")
#             st.write("Home Remedies:")
#             st.write("\n".join(remedy))
#         else:
#             st.write("Please fill in all fields.")
# 
# !streamlit run app.py
# 
# 
#