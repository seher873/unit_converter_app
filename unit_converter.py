import streamlit as st

st.title("🔄 Simple Unit Converter ✨")

unit_type = st.selectbox("🔍 Select Unit Type", ["📏 Length", "⚖️ Weight"])

if unit_type == "📏 Length":
    length_units = ["Meter (m)", "Kilometer (km)", "Centimeter (cm)", "Millimeter (mm)", "Mile (mi)", "Yard (yd)", "Foot (ft)", "Inch (in)"]
    from_unit = st.selectbox("📤 From Unit", length_units)
    to_unit = st.selectbox("📥 To Unit", length_units)
    value = st.number_input("✍️ Enter Value", min_value=0.0)

    if st.button("🚀 Convert Length"):
        to_meter = {
            "Meter (m)": 1,
            "Kilometer (km)": 1000,
            "Centimeter (cm)": 0.01,
            "Millimeter (mm)": 0.001,
            "Mile (mi)": 1609.34,
            "Yard (yd)": 0.9144,
            "Foot (ft)": 0.3048,
            "Inch (in)": 0.0254
        }
        from_meter = {
            "Meter (m)": 1,
            "Kilometer (km)": 0.001,
            "Centimeter (cm)": 100,
            "Millimeter (mm)": 1000,
            "Mile (mi)": 0.000621371,
            "Yard (yd)": 1.09361,
            "Foot (ft)": 3.28084,
            "Inch (in)": 39.3701
        }

        meters = value * to_meter[from_unit]
        result = meters * from_meter[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "⚖️ Weight":
    weight_units = ["Kilogram (kg)", "Gram (g)", "Pound (lb)", "Ounce (oz)"]
    from_unit = st.selectbox("📤 From Unit", weight_units)
    to_unit = st.selectbox("📥 To Unit", weight_units)
    value = st.number_input("✍️ Enter Value", min_value=0.0)

    if st.button("🚀 Convert Weight"):
        to_kg = {
            "Kilogram (kg)": 1,
            "Gram (g)": 0.001,
            "Pound (lb)": 0.453592,
            "Ounce (oz)": 0.0283495
        }
        from_kg = {
            "Kilogram (kg)": 1,
            "Gram (g)": 1000,
            "Pound (lb)": 2.20462,
            "Ounce (oz)": 35.274
        }

        kg = value * to_kg[from_unit]
        result = kg * from_kg[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
