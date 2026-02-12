import streamlit as st
import requests

st.set_page_config(page_title="Smart Factory Predictor", page_icon="🏭", layout="centered")

st.markdown("""
<style>
body {
background: linear-gradient(to right,#0f2027,#203a43,#2c5364);
}
.big-title {
font-size:36px;
font-weight:bold;
color:white;
text-align:center;
}
.card {
background-color:#ffffff;
padding:25px;
border-radius:12px;
box-shadow:0px 0px 20px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🏭 Manufacturing Output Predictor</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        Injection_Temperature = st.number_input("Injection Temperature")
        Injection_Pressure = st.number_input("Injection Pressure")
        Cycle_Time = st.number_input("Cycle Time")
        Cooling_Time = st.number_input("Cooling Time")
        Material_Viscosity = st.number_input("Material Viscosity")
        Ambient_Temperature = st.number_input("Ambient Temperature")

    with col2:
        Machine_Age = st.number_input("Machine Age", step=1)
        Operator_Experience = st.number_input("Operator Experience", step=1)
        Maintenance_Hours = st.number_input("Maintenance Hours")
        Shift = st.selectbox("Shift", ["Day","Night","Evening"])
        Machine_Type = st.selectbox("Machine Type", ["Type_A","Type_B"])
        Material_Grade = st.selectbox("Material Grade", ["Economy","Standard","Premium"])
        Day_of_Week = st.selectbox("Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

    if st.button("Predict Output 🚀"):
        payload = {
            "Injection_Temperature": Injection_Temperature,
            "Injection_Pressure": Injection_Pressure,
            "Cycle_Time": Cycle_Time,
            "Cooling_Time": Cooling_Time,
            "Material_Viscosity": Material_Viscosity,
            "Ambient_Temperature": Ambient_Temperature,
            "Machine_Age": Machine_Age,
            "Operator_Experience": Operator_Experience,
            "Maintenance_Hours": Maintenance_Hours,
            "Shift": Shift,
            "Machine_Type": Machine_Type,
            "Material_Grade": Material_Grade,
            "Day_of_Week": Day_of_Week
        }

        res = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if res.status_code == 200:
            result = res.json()["parts_per_hour"]
            st.success(f"✅ Estimated Output: {result} Parts/Hour")

    st.markdown("</div>", unsafe_allow_html=True)
