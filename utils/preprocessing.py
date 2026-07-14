import re
def clean_resume(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_name(resume_text):
    
        lines = resume_text.split("\n")
    
    
        for line in lines:
    
            line = line.strip()
    
    
            if line.lower().startswith("name"):
    
                name = line.split(":",1)[1].strip()
    
                return name
    
    
        # If no Name: found
    
        for line in lines[:5]:
    
            if len(line.split()) <= 3 and len(line.strip()) > 2:
    
                return line.strip()
    
    
        return "Unknown"