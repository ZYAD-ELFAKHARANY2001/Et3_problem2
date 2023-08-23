# Et3_problem2

**Professional Documentation:**

**Project Overview:**
This Python script is designed to accomplish the following tasks:
1. Parse a text file containing object information (e.g., number of image, coordinates, dimensions).
2. Create a JSON file that includes the parsed object information.
3. Add additional metadata to the JSON structure, such as image rotation and a reference to an image file.
4. Save the JSON data to an output JSON file.

**Solution Components:**
The solution comprises the following key components:

1. `parse_text_file(input_file)`: This function reads and parses the specified input text file to extract object information (e.g., object name, coordinates, dimensions). It then structures this information into a list of dictionaries.

2. `output_json_file`: This variable defines the path and name of the output JSON file where the parsed data will be stored.

3. `json_data`: This dictionary structure is used to format the final JSON output. It includes a list of parsed object annotations and additional metadata, such as image rotation and a reference to an image file.

**Instructions to Run the Solution:**
To run the solution, follow these steps:

1. Ensure that you have Python installed on your system.

2. Prepare the input data:
   - Create an input text file (`input_txt_file`) that contains object information. The file should have the following format, where each line represents an object:
     ```
     number of image x_coordinate y_coordinate width height
     ```

   - Define the path to the input image file (`input_img_file`) that corresponds to the object data.

3. Define the desired path and name for the output JSON file (`output_json_file`). Make sure to specify the correct location where you want to save the generated JSON file.

4. Run the Python script containing the provided code. For example, you can use a command prompt or terminal to execute the script:
   ```
   python Solve 2.py
   ```


5. After running the script, it will parse the input text file, structure the data, add metadata, and create the specified output JSON file. You will see a message indicating that the JSON file has been created successfully.

The resulting JSON file (`second_system_input.json`) will contain the parsed object information along with additional metadata, making it suitable for further processing or integration with other systems.

This solution streamlines the conversion of object data from a text file to a structured JSON format, facilitating data interoperability and analysis.
