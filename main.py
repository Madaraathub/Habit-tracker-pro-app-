
import pandas as pd
from jinja2 import Template

# Read data from CSV files
main_data = pd.read_csv('habits.csv')
daily_tracker = pd.read_csv('daily_tracker.csv')

# Convert daily tracker to a list of dictionaries for Jinja
daily_tracker_rows = daily_tracker.to_dict('records')

# Load template
with open('habit_tracker_template.txt', 'r') as file:
    template = Template(file.read())

# Render template with data from the first row of main_data
output = template.render(
    month=main_data['month'][0],
    primary_goal=main_data['primary_goal'][0],
    why=main_data['why'][0],
    habit1=main_data['habit1'][0],
    habit2=main_data['habit2'][0],
    habit3=main_data['habit3'][0],
    week=main_data['week'][0],
    what_worked=main_data['what_worked'][0],
    challenges=main_data['challenges'][0],
    improvement_plan=main_data['improvement_plan'][0],
    habit1_rating=main_data['habit1_rating'][0],
    habit2_rating=main_data['habit2_rating'][0],
    habit3_rating=main_data['habit3_rating'][0],
    achievement=main_data['achievement'][0],
    reward=main_data['reward'][0],
    note_date=main_data['note_date'][0],
    note=main_data['note'][0],
    small_win1=main_data['small_win1'][0],
    small_win2=main_data['small_win2'][0],
    small_win3=main_data['small_win3'][0],
    start_date=main_data['start_date'][0],
    completion_date=main_data['completion_date'][0],
    signature=main_data['signature'][0],
    daily_tracker=daily_tracker_rows
)

# Save output to a file
with open('habit_tracker_output.md', 'w') as file:
    file.write(output)

print("Template generated successfully as 'habit_tracker_output.md'!")
