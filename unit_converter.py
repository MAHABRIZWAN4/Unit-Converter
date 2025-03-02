import streamlit as st
from streamlit.components.v1 import html

# Custom CSS for animations and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
    text-align: center;
    padding: 1.5rem;
 
 
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    animation: slideIn 1s ease;
}

@keyframes slideIn {
   
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.converter-box {
   
    background: white;
    padding: 2rem;
    border-radius: 15px;
   
   
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin: 1rem 0;
    transition: transform 0.3s ease;
}



.stSelectbox > div > div {
    border-radius: 10px!important;
}

.stButton > button {
    width: 100%;
    border: none;
    padding: 1rem 2rem;
    border-radius: 10px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-weight: 600;
    transition: transform 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.result-box {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 1rem 0;
    text-align: center;
    animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.unit-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header">
    <h1 style="color: #2a2a2a; margin: 0;">🌍 Smart Unit Converter</h1>
    <p style="color: #666; margin: 0.5rem 0;">Instantly Convert Between Various Units</p>
</div>
""", unsafe_allow_html=True)

# Main Converter
with st.container():
   
    category = st.selectbox(
        "📚 Category",
        ["Length", "Weight", "Time"],
        key="category"
    )
    
    # Unit selection based on category
    unit_options = {
        
        "Length": ["Kilometers to Miles", "Miles to kilometers"],
        
        "Weight": ["Kilograms to pounds", "Pounds to kilograms"],
        
        "Time": ["Seconds to minutes", "Minutes to Seconds", 
                "Minutes to Hours", "Hours to Minutes", 
                "Hours to Days", "Days to Hours"]
    }
    
    unit_icons = {
        "Length": "📏",
        "Weight": "⚖️",
        "Time": "⏳"
    }
    
    unit = st.selectbox(
        f"{unit_icons[category]} Conversion Type",
        unit_options[category],
        key="unit_type"
    )
    
    value = st.number_input(
        "🔢 Enter Value",
        min_value=0.0,
        format="%f",
        key="value_input"
    )
    
    if st.button("✨ Convert Now"):
        with st.spinner("Converting..."):
            # Conversion logic
            def convert_units(category, value, unit):
                conversion_factors = {
                    "Length": {
                        "Kilometers to Miles": 0.621371,
                        "Miles to kilometers": 1/0.621371
                    },
                    "Weight": {
                        "Kilograms to pounds": 2.20462,
                        "Pounds to kilograms": 1/2.20462
                    },
                    "Time": {
                        "Seconds to minutes": 1/60,
                        "Minutes to Seconds": 60,
                        "Minutes to Hours": 1/60,
                        "Hours to Minutes": 60,
                        "Hours to Days": 1/24,
                        "Days to Hours": 24
                    }
                }
                return value * conversion_factors[category][unit]
            
            result = convert_units(category, value, unit)
            
            st.markdown(f"""
            <div class="result-box">
                <h3 style="color: #2a2a2a; margin: 0 0 1rem 0;">🎉 Result</h3>
                <p style="font-size: 1.5rem; margin: 0; color: #667eea;">
                    {value:.2f} {unit.split()[0]} = 
                    <strong>{result:.2f} {unit.split()[-1]}</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Add some decorative elements
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>🔧 Precision Engineered by ❤️ Mahab Rizwan</p>
</div>
""", unsafe_allow_html=True)

# Add confetti animation on conversion
if st.session_state.get('convert_clicked'):
    html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
    <script>
    const count = 200;
    const defaults = {
        origin: { y: 0.7 }
    };

    function fire(particleRatio, opts) {
        confetti(Object.assign({}, defaults, opts, {
            particleCount: Math.floor(count * particleRatio)
        }));
    }

    fire(0.25, { spread: 26, startVelocity: 55 });
    fire(0.2, { spread: 60 });
    fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
    fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
    fire(0.1, { spread: 120, startVelocity: 45 });
    </script>
    """)