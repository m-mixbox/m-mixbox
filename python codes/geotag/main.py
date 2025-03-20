import requests
from PIL import Image, UnidentifiedImageError, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

def fetch_map_image(lat, lon, zoom=12):
    # Use OpenStreetMap's static map service
    map_url = f"https://staticmap.openstreetmap.de/staticmap.php?center={lat},{lon}&zoom={zoom}&size=400x400&maptype=roadmap"
    response = requests.get(map_url)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            return Image.open(BytesIO(response.content))  # Return the image object
        except UnidentifiedImageError:
            print("Error: Unable to identify the image. The content may not be an image.")
            return None  # Return None if there's an error
    else:
        print(f"Error: Received status code {response.status_code}.")
        return None  # Return None on error

def add_geotag_to_image(image_path, lat, lon):
    # Open the image to be geotagged
    img = Image.open(image_path)

    # Fetch the map image
    map_img = fetch_map_image(lat, lon)
    
    if map_img is None:
        print("Failed to fetch the map image. Exiting.")
        return  # Exit if the map image cannot be fetched

    # Combine images (you can customize the position as needed)
    img = img.resize((800, 600))  # Resize original image
    map_img = map_img.resize((400, 400))  # Resize map image
    img.paste(map_img, (400, 0))  # Paste map image to the right of the original

    # Add text information
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text = f"Location: {lat}, {lon}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    draw.text((10, 10), text, fill="white", font=font)

    # Save the new image
    img.save('geotagged_image.png')
    print("Geotagged image saved as 'geotagged_image.png'.")

# Example usage
if __name__ == "__main__":
    # Path to your image
    image_path = r'python codes\geotag\1.JPG'  # Replace with your image path
    lat = 40.73061  # Example latitude
    lon = -73.935242  # Example longitude
    add_geotag_to_image(image_path, lat, lon)
