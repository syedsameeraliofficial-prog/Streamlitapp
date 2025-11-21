import streamlit as st
import pickle


#to load the model and Label Encoder
model = pickle.load(open("car_model.pkl","rb"))
le = pickle.load(open("label_encoder.pkl","rb"))


## for title - Heading
st.title("Car prediction app")

## dropdown for car models

car_model = st.selectbox("Select Car Model", le.classes_)

## User inputs
mileage = st.number_input("Enter mileage (in miles)", min_value=0)

age=st.slider("Car age(year)" , 0 , 8 )


## selected car model to encode value for prediction

encoded_model= le.transform([car_model])[0]

if st.button("Predict Price"):
    input_data=[[encoded_model , mileage,age]]
    predicted_price = model.predict(input_data)
    st.success(f"Estimated selling price: {predicted_price[0]}")
