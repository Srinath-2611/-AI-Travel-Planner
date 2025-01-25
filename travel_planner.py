import streamlit as st
import random

st.title("AI Travel Planner")

# User Inputs
destination = st.text_input("Destination:", value="")
duration = st.number_input("Trip Duration (days):", min_value=1, step=1)
budget = st.selectbox("Budget:", ["Luxury", "Moderate", "Budget-friendly"])
purpose = st.text_input("Purpose of travel (e.g., leisure, work):", value="")
interests = st.text_area("Your interests (e.g., art, food, adventure):", value="")
diet = st.text_input("Dietary preferences (if any):", value="")
mobility = st.text_input("Mobility concerns (e.g., walking tolerance):", value="")
accommodation = st.selectbox("Accommodation preference:", ["Luxury", "Budget", "Central location"])

# Button to Generate Itinerary
if st.button("Generate Itinerary"):
    st.write(f"Here’s a personalized {duration}-day itinerary for {destination}:")

    # Example activities for dynamic generation
    activities_morning = [
        f"Visit a famous landmark in {destination}",
        f"Explore a local market in {destination}",
        f"Enjoy a morning hike or walk",
        f"Take a guided tour of {destination}",
    ]
    activities_afternoon = [
        f"Have lunch at a top-rated restaurant in {destination}",
        f"Visit a historical museum in {destination}",
        f"Relax in a park or garden in {destination}",
        f"Take a cultural tour in {destination}",
    ]
    activities_evening = [
        f"Enjoy dinner at a local hotspot in {destination}",
        f"Attend a live performance or event",
        f"Explore the nightlife of {destination}",
        f"Relax at your accommodation",
    ]

    # Generate itinerary for each day
    for day in range(1, int(duration) + 1):
        st.write(f"**Day {day}:**")
        st.write(f"- Morning: {random.choice(activities_morning)}.")
        st.write(f"- Afternoon: {random.choice(activities_afternoon)}.")
        st.write(f"- Evening: {random.choice(activities_evening)}.")
