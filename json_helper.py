import json
import os
import pickle

def read_json(file_path):
    try:
        # Attempt to open the specified JSON file
        with open(file_path, 'r') as file:
            # Create an empty string to store file content
            file_content = ""

            # Use a for loop to read each line from file than concatenate file content
            for line in file:
                file_content += line

                # Use json.loads to parse the JSON data from concatenated file content
                json_data = json.loads(file_content)

            # Return resulting json object
            return json_data

    except FileNotFoundError:
        # What to print in case file is not found
        print(f"Error: '{file_path}' was not found")
        return None

    except json.JSONDecodeError:
        # If there's an issue decoding JSON data
        print(f"Error: Unable to decode JSON from '{file_path}")
        return None

def read_all_json_files(directory_path):
    # Create an empty list and store json objects
    json_objects = []

    # Check if path is a directory
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory")
        return json_objects

    # Loop through all files in directory
    for filename in os.listdir(directory_path):
        # construct through full file path
        file_path = os.path.join(directory_path, filename)

        # Check if file is a JSON file
        if filename.endswith('.json'):
            # Use the read_json function to read and append the JSON object to the list
            json_objects = read_json(file_path)

            # Check if the read_json function was successful
            if json_objects is not None:
              json_objects.append(json_objects)

    # Return the list of all JSON objects
    return json_objects


def write_pickle(file_path, data):
    try:
        # Open the file in write mode using the with statement
        with open(file_path, 'wb') as file:
            # Use pickle.dump to write data to the file
            pickle.dump(data, file)
            print (f"Data is written to {file_path}")
    except Exception as e:
        # Handle exceptions during the file writing process
        print(f"Error: Unable to write data to {file_path}. {e}")


def load_pickle(file_path):
    try:
        # Open file path with read mode using with statement
        with open(file_path, 'rb') as file:
            # Use pickle.load to read data from the file
            loaded_data = pickle.load(file)
            return loaded_data
    except Exception as e:
        # Handle exceptions during the file reading process
        print(f"Error: Can't load data from {file_path}. {e}")
        return None





