import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv("udemy_output_All_Finance__Accounting_p1_p626.csv")

# Set up the app layout
st.title("Finance & Accounting Courses")
st.sidebar.title("Filters")

# Filter by rating
rating_range = st.sidebar.slider("Select Rating Range", min_value=0.0, max_value=5.0, step=0.1, value=(0.0, 5.0))
filtered_data = data[(data['rating'] >= rating_range[0]) & (data['rating'] <= rating_range[1])]

# Display filtered results
st.dataframe(filtered_data)

# Question 1: What are the top-rated courses in the dataset?
top_rated_courses = data.sort_values('rating', ascending=False).head(10)['title']
st.write("Top-rated courses:")
st.write(top_rated_courses)

# Question 2: Which courses have the highest number of subscribers?
most_subscribed_courses = data.sort_values('num_subscribers', ascending=False).head(10)['title']
st.write("Courses with the highest number of subscribers:")
st.write(most_subscribed_courses)

# Question 3: What is the average duration of the courses?
average_duration = data['num_published_lectures'].mean()
st.write("Average duration of courses (number of lectures):")
st.write(average_duration)

# Question 6: What is the distribution of course prices?
price_distribution = data['price_detail__amount'].value_counts()
st.write("Distribution of course prices:")
st.write(price_distribution)

# Question 7: How many free courses are available?
free_course_count = data[data['is_paid'] == False].shape[0]
st.write("Number of free courses available:")
st.write(free_course_count)

# Question 8: Which courses cover topics related to financial analysis?
financial_analysis_courses = data[data['title'].str.contains('financial analysis', case=False)]['title']
st.write("Courses related to financial analysis:")
st.write(financial_analysis_courses)

# Question 9: What are the most common course titles or keywords?
common_keywords = data['title'].str.lower().str.split().explode().value_counts().head(10).index.tolist()
st.write("Most common course titles or keywords:")
st.write(common_keywords)

# Question 10: Are there any courses that offer a certificate upon completion?
courses_with_certificates = data[data['title'].str.contains('certificate', case=False)]['title']
st.write("Courses that offer a certificate upon completion:")
st.write(courses_with_certificates)

# Set up the app layout
st.title("Finance & Accounting Courses")

# Filtering options
discount_filter = st.sidebar.slider("Discounted Price", 0.0, float(data['discount_price__amount'].max()), step=1.0)


# Apply filtering
filtered_data = data[data['discount_price__amount'] <= discount_filter]



# Display filtered results
st.write(f"Displaying {len(filtered_data)} courses:")


st.table(filtered_data[['title', 'num_subscribers', 'avg_rating', 'num_published_lectures', 'url']])
    
