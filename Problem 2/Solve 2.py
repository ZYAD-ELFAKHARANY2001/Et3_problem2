import json
import os
# Define the input text file path
input_txt_file = "problem2/problem2/image1.txt"

input_img_file = "problem2/problem2/image1.jpg"

# Define the output JSON file path
output_json_file = "Solve 2/second_system_input.json"

# Initialize a list to store object information
object_info_list = []

# Function to parse the text file and extract object information
def parse_text_file(input_file):

   
    with open(input_file, "r") as txt_file:
        for line in txt_file:
            line = line.strip()
            parts = line.split()
            object_name = parts[0]
            x_coordinate = parts[1]
            y_coordinate = parts[2]
            width = parts[3]
            height = parts[4]
            object_info = {
                "image_rotation": object_name,
                'value': {
                    'x': x_coordinate,
                    'y': y_coordinate,
                    'width': width,
                    'height': height,
                    "rotation":0,
                    "rectanglelabels":[
                        "object"
                    ]
            }}
            object_info_list.append(object_info)

# Parse the text file and extract object information
parse_text_file(input_txt_file)

#output_json_file = os.path.dirname(output_json_file)
#os.makedirs(output_json_file, exist_ok=True)
# Create the JSON structure
json_data = {"annotation": object_info_list,
    "data": {
        "image": "\/data\/upload\/image1.jpg"
    }}

# Write the JSON data to the output file
with open(output_json_file, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON file '{output_json_file}' created successfully.")
