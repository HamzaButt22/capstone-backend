import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
    return full_text


def preprocess_text(text):
    doc = nlp(text)
    
    clean_tokens = [
        token.lemma_.lower() 
        for token in doc 
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    
    return " ".join(clean_tokens)

def analyze_resume(pdf_path):
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = preprocess_text(raw_text)
    
    CATEGORIES = {
        'Data Science': ['python', 'sql', 'machine', 'learning', 'data', 'analytics', 'statistics', 'modeling'],
        'Web Development': ['javascript', 'react', 'html', 'css', 'node', 'frontend', 'backend', 'developer'],
        'Security Ops': ['security', 'guard', 'safety', 'protecting', 'guarding', 'criminal', 'justice', 'defense']
    }
    
    best_category = "Unknown"
    max_score = 0
    detected_skills = []
    
    for category, skills in CATEGORIES.items():
        match_count = 0
        for skill in skills:
            if skill in cleaned_text:
                detected_skills.append(skill)
                match_count += 1
                
        if match_count > max_score:
            max_score = match_count
            best_category = category
            
    return best_category, list(set(detected_skills))