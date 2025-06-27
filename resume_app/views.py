from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
import docx2txt, re
from pdfminer.high_level import extract_text

# Predefined skills to match against
SKILLS_DB = ['python', 'java', 'django', 'flask', 'sql', 'html', 'css', 'javascript']
import tempfile

def extract_resume_text(file):
    if file.name.endswith('.pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            for chunk in file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name
        return extract_text(tmp_path)
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    return ""

# Extract skills using simple keyword match
def extract_skills(text):
    found_skills = [skill for skill in SKILLS_DB if skill.lower() in text.lower()]
    score = len(found_skills) / len(SKILLS_DB) * 100
    return ", ".join(found_skills), round(score, 2)

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            text = extract_resume_text(request.FILES['file'])
            skills, score = extract_skills(text)
            resume.skills = skills
            resume.score = score
            resume.save()
            return render(request, 'result.html', {'resume': resume})
    else:
        form = ResumeForm()
    return render(request, 'upload.html', {'form': form})