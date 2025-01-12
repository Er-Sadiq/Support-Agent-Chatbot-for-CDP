import google.generativeai as genai
import json


def read_json_file(file_path):
    """
    Function to read data from a JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            file_data = json.load(file)
        return file_data
    except Exception as e:
        return f"Error reading the file: {str(e)}"

def format_response(raw_text):
    """
    Format the raw response from the Gemini model into a systematic structure.
    """
    formatted_text = ""
    lines = raw_text.split('\n')
    for line in lines:
        if line.strip():
            formatted_text += f"- {line.strip()}\n"
    return f"**Generated Response:**\n\n{formatted_text.strip()}"

def responser(userinput, file_path="data/cdp_docs.json"):
    try:
        
        genai.configure(api_key="AIzaSyAgIcGdPcv7MgKmwDtTX8mCQns0QR4QXZI")
     
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Read data from the JSON file
        file_data = read_json_file(file_path)
        
        if "Error" in file_data:
            return file_data  # Return file read error message
        
        # Prepare file data to be used as context for generating responses
        input_data = f"File Knowledge Base:\n{json.dumps(file_data, indent=2)}\n\nUser Input: {userinput}"

        # Generate content using the combined input (file data + user input)
        response = model.generate_content(input_data)
        
        formatted_response = format_response(response.text)
        
       
        return formatted_response
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    responser()