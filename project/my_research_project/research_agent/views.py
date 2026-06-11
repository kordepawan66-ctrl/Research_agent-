from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .utils.parser import extract_pdf_text
from .utils.watson_agent import query_research_agent

def research_dashboard(request):
    """Renders the primary application dashboard."""
    return render(request, 'dashboard.html')

def summarize_paper(request):
    """Processes file upload and invokes Granite for deep analysis."""
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        uploaded_file = request.FILES['pdf_file']
        
        # Save file temporarily or read in-memory
        text_content = extract_pdf_text(uploaded_file)
        
        # Guard against exceeding typical free token boundaries safely
        truncated_text = text_content[:40000] 
        
        system_instruction = "You are an expert academic research assistant. Provide an abstract summary, core hypotheses, methodology, and a critical critique."
        prompt = f"Analyze the following research paper text:\n\n{truncated_text}"
        
        summary_result = query_research_agent(prompt, system_instruction)
        
        return JsonResponse({'status': 'success', 'summary': summary_result})
    
    return JsonResponse({'status': 'failed', 'error': 'Invalid request'}, status=400)

def suggest_hypothesis(request):
    """Generates new scientific hypotheses based on keywords or subject domains."""
    if request.method == 'POST':
        topic = request.POST.get('topic')
        system_instruction = "You are a visionary R&D scientist. Generate 3 unique, verifiable, and novel scientific hypotheses based on the user's topic."
        
        hypotheses = query_research_agent(f"Topic: {topic}", system_instruction)
        return JsonResponse({'hypotheses': hypotheses})