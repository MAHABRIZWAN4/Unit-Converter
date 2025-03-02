import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts length, Weight and Time Instantly")
st.write("Welcome! Select a Category, Enter a value and get the converted result in real time")


category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])



def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
    
    elif unit == "Miles to kilometers":
        return value / 0.621371



    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
    elif unit == "Pounds to kilograms":
        return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit  == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24





if category == "Lenght":
    unit = st.selectbox("📏 Select Conversation", ["Kilometers to Miles", "Miles to kilometers"])



if category == "Weight":
    unit = st.selectbox("❓❔❓ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])




if category == "Time":
    unit = st.selectbox("⏱️⌚⏲️ Select Conversation", ["Seconds to minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])



value = st.number_input("Enter the value to convert")




if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")