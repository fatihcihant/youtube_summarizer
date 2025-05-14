import gradio as gr
from transcript_fetcher import fetch_transcript
from llm_agent import LLMAgent
from diagram_generator import generate_diagram
from quiz_generator import format_quiz

def process_video(youtube_url):
    """Process the YouTube video and return summary, diagram, and quiz."""
    try:
        # Initialize LLM agent
        llm = LLMAgent()
        
        # Fetch transcript
        transcript = fetch_transcript(youtube_url)
        
        # Generate summary
        summary = llm.summarize_video(transcript)
        
        # Generate diagram
        diagram_description = llm.generate_diagram_description(summary)
        diagram_path = generate_diagram(diagram_description)
        
        # Generate quiz
        quiz = llm.generate_quiz(summary)
        formatted_quiz = format_quiz(quiz)
        
        return summary, diagram_path, formatted_quiz
    except Exception as e:
        return f"Error: {str(e)}", None, None

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# YouTube Video Summarizer")
    youtube_url = gr.Textbox(label="YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
    submit_btn = gr.Button("Process Video")
    
    summary_output = gr.Textbox(label="Video Summary")
    diagram_output = gr.Image(label="Topic Diagram")
    quiz_output = gr.HTML(label="Quiz")
    
    submit_btn.click(
        fn=process_video,
        inputs=youtube_url,
        outputs=[summary_output, diagram_output, quiz_output]
    )

if __name__ == "__main__":
    demo.launch()