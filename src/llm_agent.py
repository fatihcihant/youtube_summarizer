import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class LLMAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def summarize_video(self, transcript):
        """Generate a detailed summary of the video transcript."""
        prompt = f"""
        Summarize the following video transcript in 300-500 words, capturing key points, themes, and insights in detail:
        {transcript[:4000]}  # Limit to avoid API token limits
        """
        response = self.model.generate_content(prompt)
        return response.text

    def generate_diagram_description(self, summary):
        """Generate a description for a diagram related to the video topic."""
        prompt = f"""
        Based on the following summary, describe a diagram (e.g., flowchart, concept map) that visually represents the main topic or concepts discussed. Provide a detailed description of the diagram's structure and elements:
        {summary}
        """
        response = self.model.generate_content(prompt)
        return response.text

    def generate_quiz(self, summary):
        """Generate a quiz with 5 multiple-choice questions based on the video summary."""
        prompt = f"""
        Create a quiz with 5 multiple-choice questions (4 options each) based on the following video summary. Include the correct answer and a brief explanation for each question:
        {summary}
        """
        response = self.model.generate_content(prompt)
        return response.text