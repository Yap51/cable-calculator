import streamlit as st
import pandas as pd


# Custom CSS to force Black & Orange Theme
st.markdown("""
    <style>
    /* Main Background to Black */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
   
    /* --- NEW RULE FOR LABELS ---
      This targets the labels for selectboxes and number inputs
      and forces them to be white.
    */
    .stSelectbox label, .stNumberInput label {
        color: white !important;
        font-weight: bold;
    }
   
    /* Input Fields Background */
    .stSelectbox > div > div {
        background-color: #262730;
        color: white;
    }
    .stNumberInput > div > div > input {
        background-color: #262730;
        color: white;
    }
   
    /* Primary Headers to Orange */
    h1, h2, h3 {
        color: #FF8C00 !important; /* Dark Orange */
    }
   
    /* The Calculate Button - Orange Background */
    div.stButton > button {
        background-color: #FF4500; /* Orange Red */
        color: white;
        border: none;
        font-weight: bold;
        padding: 10px 20px;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FF8C00;
        border: 1px solid white;
    }
   
    /* Success Message Box - Darker Green/Black with Orange Text */
    .stSuccess {
        background-color: #1E1E1E;
        border-left: 5px solid #FF4500;
        color: #FAFAFA;
    }
    </style>
    """, unsafe_allow_html=True)
 
# --- 2. FULL DATA TRANSCRIPTION ---
data = [
    # --- MTP (Spring No) ---
    {"Fiber": "Black loose tube", "Conn": "MTP", "Spring": "No", "Offset": 28},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "MTP", "Spring": "No", "Offset": 32},
    {"Fiber": "Aqua Loose Tube", "Conn": "MTP", "Spring": "No", "Offset": 54},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "MTP", "Spring": "No", "Offset": 54},
    {"Fiber": "Jacketed Ribbon", "Conn": "MTP", "Spring": "No", "Offset": 28},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "MTP", "Spring": "No", "Offset": 32},
 
    # --- MT (Spring No) ---
    {"Fiber": "Black loose tube", "Conn": "MT", "Spring": "No", "Offset": 28},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "MT", "Spring": "No", "Offset": 32},
    {"Fiber": "Aqua Loose Tube", "Conn": "MT", "Spring": "No", "Offset": 54},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "MT", "Spring": "No", "Offset": 54},
    {"Fiber": "Jacketed Ribbon", "Conn": "MT", "Spring": "No", "Offset": 28},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "MT", "Spring": "No", "Offset": 32},
 
    # --- Bayonet (Spring No) ---
    {"Fiber": "Black loose tube", "Conn": "Bayonet", "Spring": "No", "Offset": 28},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "Bayonet", "Spring": "No", "Offset": 32},
    {"Fiber": "Aqua Loose Tube", "Conn": "Bayonet", "Spring": "No", "Offset": 54},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "Bayonet", "Spring": "No", "Offset": 54},
    {"Fiber": "Jacketed Ribbon", "Conn": "Bayonet", "Spring": "No", "Offset": 28},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "Bayonet", "Spring": "No", "Offset": 32},
 
    # --- Vita 66.X (Spring Yes) ---
    {"Fiber": "Black loose tube", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Aqua Loose Tube", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Jacketed Ribbon", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "Vita 66.X", "Spring": "Yes", "Offset": 53},
 
    # --- U Cable (Connector NA) ---
    {"Fiber": "U cable Jacketed Ribbon", "Conn": "NA", "Spring": "No", "Offset": 40},
    {"Fiber": "U cable Aqua Loose tube", "Conn": "NA", "Spring": "No", "Offset": 108},
    {"Fiber": "U cable Black Loose tube", "Conn": "NA", "Spring": "No", "Offset": 40},
    {"Fiber": "U cable Jacketed Ribbon with strain relief", "Conn": "NA", "Spring": "No", "Offset": 40},
    {"Fiber": "U cable Aqua Loose tube with strain relief", "Conn": "NA", "Spring": "No", "Offset": 108},
    {"Fiber": "U cable Black Loose tube with strain relief", "Conn": "NA", "Spring": "No", "Offset": 40},
 
    # --- MT38999 (Spring No) ---
    {"Fiber": "Black loose tube", "Conn": "MT38999", "Spring": "No", "Offset": 28},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "MT38999", "Spring": "No", "Offset": 28},
    {"Fiber": "Aqua Loose Tube", "Conn": "MT38999", "Spring": "No", "Offset": 54},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "MT38999", "Spring": "No", "Offset": 54},
    {"Fiber": "Jacketed Ribbon", "Conn": "MT38999", "Spring": "No", "Offset": 28},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "MT38999", "Spring": "No", "Offset": 28},
 
    # --- LC DUPLEX (Spring No) ---
    {"Fiber": "Black loose tube", "Conn": "LC DUPLEX", "Spring": "No", "Offset": 28},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "LC DUPLEX", "Spring": "No", "Offset": 32},
    {"Fiber": "Aqua Loose Tube", "Conn": "LC DUPLEX", "Spring": "No", "Offset": 54},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "LC DUPLEX", "Spring": "No", "Offset": 54},
 
    # --- MT (Spring Yes) ---
    {"Fiber": "Black loose tube", "Conn": "MT", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "MT", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Aqua Loose Tube", "Conn": "MT", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "MT", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Jacketed Ribbon", "Conn": "MT", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "MT", "Spring": "Yes", "Offset": 53},
 
    # --- MT38999 (Spring Yes) ---
    {"Fiber": "Black loose tube", "Conn": "MT38999", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Black loose tube with Strain Relief", "Conn": "MT38999", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Aqua Loose Tube", "Conn": "MT38999", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Aqua Loose Tube with Strain Relief", "Conn": "MT38999", "Spring": "Yes", "Offset": 79},
    {"Fiber": "Jacketed Ribbon", "Conn": "MT38999", "Spring": "Yes", "Offset": 53},
    {"Fiber": "Jacketed Ribbon with Strain Relief", "Conn": "MT38999", "Spring": "Yes", "Offset": 53},
]
 
# Convert to DataFrame
df = pd.DataFrame(data)
 
# --- 3. THE APP INTERFACE ---
st.title("Optics Jacket Calculator")
st.markdown("---") # Orange divider line
 
# --- INPUT 1: Total Length ---
st.subheader("1. Enter Dimensions")
total_len = st.number_input("Total Cable Length in mm (XXX)", min_value=0, step=1, value=100)
 
# --- INPUT 2: Fiber Type ---
st.subheader("2. Select Components")
# Get all unique fiber types
fiber_options = df['Fiber'].unique()
fiber_sel = st.selectbox("Select Fiber Type", fiber_options)
 
# --- INPUT 3: Connector Type (Filtered!) ---
# logic: Only show connectors that exist for the SELECTED fiber
compatible_rows_1 = df[df['Fiber'] == fiber_sel]
conn_options = compatible_rows_1['Conn'].unique()
conn_sel = st.selectbox("Select Connector Type", conn_options)
 
# --- INPUT 4: Spring (Filtered!) ---
# logic: Only show spring options compatible with SELECTED Fiber AND Connector
compatible_rows_2 = compatible_rows_1[compatible_rows_1['Conn'] == conn_sel]
spring_options = compatible_rows_2['Spring'].unique()
spring_sel = st.selectbox("Spring?", spring_options)
 
st.write(" ") # Spacer
 
# 4. CALCULATE AND SHOW RESULT
if st.button("CALCULATE JACKET LENGTH"):
    # We narrow down to the single matching row
    match = compatible_rows_2[compatible_rows_2['Spring'] == spring_sel]
   
    if not match.empty:
        offset = match.iloc[0]['Offset']
        result = total_len - offset
       
        # Display Result
        st.success(f"### ✂️ Cut Jacket Length: {result}")
       
        # Show details in an expander
        with st.expander("See Calculation Details"):
            st.write(f"**Formula:** {total_len} (Total) - {offset} (Offset)")
            st.write(f"**Offset Component:** {offset} (Based on {conn_sel} + {spring_sel})")
    else:
        st.error("Error: Configuration not found. Please reset selections.")
 