from transformers import pipeline
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
# Initialize the Hugging Face pipeline for text-generation with GPT-2 model
generator = pipeline('text-generation', model="gpt2")

# Function to generate an essay for a given topic
def generate_essay(topic, max_length=600):
    prompt = f"Write a detailed essay on '{topic}' (300-600 words). Include sub-topics, analysis, and insights."
    
    # Generate the essay using the GPT-2 model
    essay = generator(prompt, 
                      max_length=max_length, 
                      num_return_sequences=1,
                      truncation=True,  # Explicitly activate truncation
                      pad_token_id=50256)  # Set pad_token_id to eos_token_id (50256)
    print(topic)

    return essay[0]['generated_text']

# Save generated essays as a PDF using ReportLab
def save_pdf_reportlab(essays, filename="generated_essays.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y_position = height - 40  # Starting Y position for text

    for topic, essay in essays.items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y_position, f"Essay on: {topic}")
        y_position -= 20

        c.setFont("Helvetica", 12)
        for line in essay.split("\n"):
            if y_position < 40:  # Start a new page if space is too low
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 40

            c.drawString(40, y_position, line)
            y_position -= 15

        y_position -= 30  # Space between essays

    c.save()
    print(f"PDF saved as {filename}")

# Read topics from a file (you can replace this with your own list of topics)
topics = []
essays = {}
with open(r"C:\Users\MBSPL-Ayush\Desktop\topics.txt", 'r', encoding="utf-8") as file:
    # Read each line in the file
    for line in file:
        if len(line) > 1:
            topics.append(line.strip())  # Add the topic to the list
print(len(topics))
# Generate essays for each topic using Hugging Face's GPT-2 model
print('started writing')
for topic in topics :
    if topic != "AFSPA":
        essays[topic] = {topic: generate_essay(topic) }
    else:
        break
with open('essay.json',"w") as file:
    json.dump(essays,file,indent=4)
print('finished writing')

# Save the generated essays as a PDF
#save_pdf_reportlab(essays)
