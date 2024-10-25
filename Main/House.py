import streamlit as st
import pandas as pd
import pickle
try:
    import importlib.metadata
except ImportError:
    import importlib as importlib_metadata


header = st.header("Fill in these inputs to predict")
model = pickle.load(open(r"C:\Users\MMADHOSIND\Desktop\model_RFR.pkl", "rb"))

# Features used during model training
features = [
    'Median_Income', 'Median_Age', 'Tot_Rooms', 'Tot_Bedrooms', 
    'Population', 'Households', 'Latitude', 'Longitude', 
    'Rooms_per_Household', 'Bedrooms_per_Household', 
    'Population_Density', 'Income_per_Person', 
    'Distance_to_coast', 'Distance_to_LA', 'Distance_to_SanDiego', 
    'Distance_to_SanJose', 'Distance_to_SanFrancisco'
]

# Initialize input dictionary
input_data = {}

# Function to validate and convert inputs
def validate_and_convert(value, default=None):
    if value.strip() == "":
        return default  # Return default if empty
    try:
        return float(value)  # Try converting to float
    except ValueError:
        return None  # Invalid if not a valid float

# Get inputs from the user for each feature
for feature in features:
    user_input = st.text_input(feature)
    input_data[feature] = validate_and_convert(user_input)  # Add validated input to input_data

# Add a collapsible HELP section
with st.expander("HELP"):
    st.write("""
    Median_income = Median of each person's income

    Median_Age = Median of each person's age

    Tot_Rooms = Total Rooms 

    Tot_BedRooms = Total BedRooms

    Households =  The number of homes in an area.

    Latitude = Distance north or south on Earth.

    Longitude = Distance east or west on Earth.  
    
    
    """)

# When Predict button is clicked
if st.button("Predict"):
    invalid_fields = []

    # Validate all fields
    for feature in features:
        if input_data[feature] is None:
            invalid_fields.append(feature)

    # Display error if there are invalid fields
    if invalid_fields:
        st.error(f"The following fields are invalid or empty: {', '.join(invalid_fields)}. Please correct them.")
    else:
        # Convert input_data to DataFrame
        df_input = pd.DataFrame([input_data])

        # Predict the house price
        try:
            prediction = model.predict(df_input)
            st.success(f"The predicted house price is: {prediction[0]}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
