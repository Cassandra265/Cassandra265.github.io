import mysql.connector
import json

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5618Cassbbb!",
    database="lab5_part1"
)
cursor = db_connection.cursor()

# Execute the query to join the two tables on the API column
query = """
SELECT w.*, ws.*
FROM well_info w
INNER JOIN well_specific_stimulations ws ON w.api = ws.api
WHERE w.latitude != 'N/A' AND w.latitude IS NOT NULL 
AND w.longitude != 'N/A' AND w.longitude IS NOT NULL
"""
cursor.execute(query)

# Fetch all records from the joined tables
records = cursor.fetchall()

# Get the column names from the cursor
column_names = [desc[0] for desc in cursor.description]

# Close the database connection
cursor.close()
db_connection.close()

# Prepare the data for subsequent use
combined_data = [dict(zip(column_names, record)) for record in records]

# Convert to JSON format
json_combined_data = json.dumps(combined_data, ensure_ascii=False, default=str)

# Save the combined data to a .js file
with open("combined_data.js", "w") as file:
    file.write("var combinedData = " + json_combined_data + ";")

print("Combined well and stimulation data are saved in combined_data.js successfully.")
