import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Create a simple mock dataset and train the model automatically
data = {
    'CGPA': [6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5],
    'Internships': [0, 1, 1, 2, 2, 3, 3],
    'Projects': [1, 1, 2, 2, 3, 3, 4],
    'Package_LPA': [3.5, 4.2, 5.0, 6.5, 7.8, 9.5, 11.0]
}
df = pd.DataFrame(data)

# Features and Target
X = df[['CGPA', 'Internships', 'Projects']]
y = df['Package_LPA']

# Train the Regression Model
model = LinearRegression()
model.fit(X, y)

# 2. Streamlit Web Interface Design
st.title("🎓 Placement Package Prediction System")
st.write("Enter your academic and technical details below to predict your expected salary package.")

# User Input Controls
cgpa = st.slider("Enter your CGPA", 5.0, 10.0, 7.5)
internships = st.slider("Number of Internships Completed", 0, 4, 1)
projects = st.slider("Number of Projects Built", 0, 5, 2)

# 3. Prediction Button Logic
if st.button("Predict Package"):
    # Make prediction using the trained model
    input_data = pd.DataFrame([[cgpa, internships, projects]], columns=['CGPA', 'Internships', 'Projects'])
    prediction = model.predict(input_data)[0]
    
    # Display Result
    st.success(f"🎉 Estimated Placement Package: ₹{prediction:.2f} LPA")