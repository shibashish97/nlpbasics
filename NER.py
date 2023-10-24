import spacy

# Load the English NER model
nlp = spacy.load("en_core_web_sm")

email_text = """
Subject: PCB Manufacturing Inquiry

Dear [Your Company Name],

I hope this email finds you well. We are in the process of designing a new electronic product and are interested in your PCB manufacturing services. We have heard great things about your company's expertise in this field.

Here are some details about our project:

Product: Advanced IoT Device
Quantity: 5000 units
PCB Specifications:
- Double-sided PCB
- FR-4 Material
- 4-layer stackup
- Dimensions: 100mm x 100mm
- Surface Finish: ENIG (Electroless Nickel Immersion Gold)
- Minimum Trace/Space: 6 mils
- Minimum Hole Size: 0.2mm
- RoHS compliant

We would like to request a quote for the manufacturing of these PCBs. Additionally, please provide information on lead times and any other relevant details.

If you require any further information or have specific questions about our project, please do not hesitate to contact me.

Thank you for your prompt attention to this matter. We look forward to hearing from you soon.

Best regards,
[Your Name]
[Your Company Name]
[Your Contact Information]
"""

# You can now use this email_text variable for Named Entity Recognition (NER) or any other processing as needed.

# Process the email text
doc = nlp(email_text)

# Extract named entities and their labels
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the extracted entities
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
