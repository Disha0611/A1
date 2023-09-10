import pandas as pd
import csv


with open("job_data.csv", "r") as file:
	data = file.read()
	print(data)

with open("sample_data1.txt", "r") as file:
	data = file.read()
	print(data)


csvfile = "job_data.csv"

def average_salaries(csvfile, job_titles):
    # Read the CSV file 
    df = pd.read_csv(csvfile)

    # To include only the specified job titles
    updated_df = df[df['job_title'].isin(job_titles)]

    # Group the filtered data by job title and calculate the average num_of_salaries, using inbuilt groupby function
    average_salaries = updated_df.groupby('job_title')['num_of_salaries'].mean()

    return average_salaries


# Specify the job titles 
job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer"]


average_salaries_result = average_salaries(csvfile, job_titles)

# Print the result
print("Average Salaries for Specified Job Titles:")
print(average_salaries_result)


