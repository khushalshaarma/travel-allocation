import streamlit as st
from rules import choose_transport, choose_hotel
from data import TRANSPORT_COST, HOTEL_COST

st.set_page_config(page_title="Travel Allocation AI", page_icon="✈️", layout="centered")

st.title("✈️ Travel Allocation AI (Rule-Based, Non-ML)")
st.caption("Explainable planning using rules & constraints (no Machine Learning)")

with st.container(border=True):
    distance = st.number_input("Distance (km)", min_value=1, value=300, step=10)
    budget = st.number_input("Budget (₹)", min_value=500, value=7000, step=500)
    role = st.selectbox("Role", ["intern", "staff", "manager"])
    urgency = st.selectbox("Urgency", ["normal", "urgent"])

def allocate_travel(distance_km, budget, role, urgency):
    explanation = []

    transport, exp1 = choose_transport(distance_km, urgency, budget)
    hotel, exp2 = choose_hotel(role)

    explanation.extend(exp1)
    explanation.extend(exp2)

    transport_cost = TRANSPORT_COST[transport]
    hotel_cost = HOTEL_COST[hotel]
    total_cost = transport_cost + hotel_cost

    if total_cost > budget:
        return {
            "approved": False,
            "reason": "Budget exceeded",
            "transport": transport,
            "hotel": hotel,
            "total_cost": total_cost,
            "explanation": explanation
        }

    return {
        "approved": True,
        "transport": transport,
        "hotel": hotel,
        "total_cost": total_cost,
        "explanation": explanation
    }

if st.button("🚀 Allocate Travel", use_container_width=True):
    result = allocate_travel(distance, budget, role, urgency)

    st.subheader("Decision")
    if result["approved"]:
        st.success("APPROVED ✅")
    else:
        st.error("REJECTED ❌")
        st.warning(result["reason"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Transport", result["transport"])
    col2.metric("Hotel", result["hotel"])
    col3.metric("Total Cost (₹)", result["total_cost"])

    st.subheader("Why this decision?")
    for i, exp in enumerate(result["explanation"], 1):
        st.write(f"{i}. {exp}")


# AI appended note: prompt => change the theme keep all same just theme color and   a littlt ui
