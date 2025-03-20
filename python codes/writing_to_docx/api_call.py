import requests
import os

def download_docx_file(api_url, save_directory, filename):
    """
    Downloads a .docx file from an API and saves it to the specified directory.

    :param api_url: The URL of the API endpoint to fetch the .docx file.
    :param save_directory: The directory where the file should be saved.
    :param filename: The name to save the file as.
    """
    try:
        # Send GET request to the API
        response = requests.post(api_url, stream=True)
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        # Ensure the save directory exists
        os.makedirs(save_directory, exist_ok=True)
        
        # Full path to save the file
        file_path = os.path.join(save_directory, filename)
        
        # Write the content to the file in binary mode
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File saved successfully at {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading the file: {e}")

# Example usage
api_url = "http://127.0.0.1:8000/generate-docx/"  # Replace with your API endpoint
save_directory = "./generated"
filename = "document.docx"

download_docx_file(api_url, save_directory, filename)
