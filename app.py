import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#make containers
header = st.container()

data_sets= st.container()

features = st.container()



# Streamlit App
with header:
    st.title("Titanic Application")
    st.text("In this project, the work will be done on the Titanic dataset.")
    # Display an image
    image_url = 'https://s3.eu-west-1.amazonaws.com/prod-mh-ireland/caded62c-95ab-11ed-a5fc-0210609a3fe2.JPG'
    st.image(image_url, use_column_width=True)



with data_sets:
    st.subheader("TIP: Import dataset from seaborn library")
    # import dataset
    df = sns.load_dataset("titanic")

with features:
    st.header("These are our apps features")
    st.markdown("1. **Quiz**: Test your knowledge about the Titanic disaster with trivia questions.")
    st.markdown("2. **Fare Calculator**: Calculate the fare you would have paid for a similar journey on the Titanic.")
    st.markdown("3. **Survivor Chance**: Determine your chance of survival if you were on the Titanic based on your age,gender, passenger class, and number of siblings/spouse.")


# heading for quiz game
st.header("QUIZ TIME")
# Define the trivia questions
trivia_questions = [
    {
        "question": "Which ocean did the Titanic sink in?",
        "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean"],
        "answer": "Atlantic Ocean"
    },
    {
        "question": "How many lifeboats were on the Titanic?",
        "options": ["12", "16", "20"],
        "answer": "20"
    },
    {
        "question": "Which was the first ship to respond to Titanic's distress signals?",
        "options": ["RMS Carpathia", "RMS Olympic", "SS Californian"],
        "answer": "RMS Carpathia"
    },
    {
        "question": "What was the name of the ship that collided with the Titanic?",
        "options": ["SS Californian", "RMS Olympic", "HMHS Britannic"],
        "answer": "SS Californian"
    },
    {
        "question": "Which actor played Jack Dawson in the movie 'Titanic'?",
        "options": ["Leonardo DiCaprio", "Tom Hanks", "Brad Pitt"],
        "answer": "Leonardo DiCaprio"
    },
    {
        "question": "Who composed the soundtrack for the movie 'Titanic'?",
        "options": ["James Cameron", "Hans Zimmer", "James Horner"],
        "answer": "James Horner"
    },
    {
        "question": "How many passengers survived the sinking of the Titanic?",
        "options": ["705", "813", "936"],
        "answer": "705"
    },
    # Add more trivia questions here
]

# Display the trivia quiz
for i, trivia in enumerate(trivia_questions):
    st.write(f"**Q{i + 1}: {trivia['question']}**")
    selected_option = st.radio("Select an option:", trivia['options'], key=i)
    if selected_option == trivia['answer']:
        st.write("Correct!")
    else:
        st.write("Incorrect. The correct answer is:", trivia['answer'])
    st.write("---")


# Fare Calculator
st.header("Fare Calculator")

age = st.number_input("Enter your age", min_value=0, max_value=150, value=30)
pclass = st.selectbox("Select passenger class", ["1st", "2nd", "3rd"])
destinations = df['embarked'].unique()
destination = st.selectbox("Select destination", destinations)

def calculate_fare(age, pclass, destination):
    fare_df = df[(df['age'] == age) & (df['pclass'] == pclass) & (df['embarked'] == destination)]
    if not fare_df.empty:
        fare = fare_df['Fare'].values[0]
        return fare
    return None

fare = calculate_fare(age, pclass, destination)

if fare is not None:
    st.write("Estimated Fare: $", fare)
else:
    st.write("Fare data not available for the provided details.")

# heading for survival chance
st.header("If you were on a boat, will you survived or not?")
# Display input fields for age, gender, class, and siblings/spouse
age = st.number_input("Age", min_value=0, max_value=150, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
pclass = st.selectbox("Class", ["1st", "2nd", "3rd"])
siblings_spouse = st.number_input("Number of Siblings/Spouse", min_value=0, max_value=10, value=0)

# Calculate survivor chance based on the inputs
survivor_chance = (
    (age / 100) +
    (1 if gender == "Female" else 0) +
    (0.5 if pclass == "1st" else 0) +
    (0.2 if pclass == "2nd" else 0) +
    (-0.2 if siblings_spouse > 0 else 0)
)

# Display the "Survivor Chance" slider
slider_label = "Survivor Chance"
slider_value = st.slider(slider_label, min_value=0.0, max_value=1.0, value=survivor_chance, step=0.01)

# Display humorous messages based on the slider value
if slider_value < 0.2:
    st.write("Slim chances! You might need a miracle.")
elif slider_value < 0.5:
    st.write("50-50! It's a toss-up.")
elif slider_value < 0.8:
    st.write("You're in with a good chance!")
else:
    st.write("You're definitely making it!")

# Display the calculated survivor chance
st.write(f"Calculated Survivor Chance: {slider_value * 100:.2f}%")

st.header("This Streamlit application was created by Mahrose Siddiqui.")
