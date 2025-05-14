# youtube_summarizer

A Python application that summarizes YouTube videos, generates topic-related diagrams, and creates quizzes using the Gemini API and Gradio interface.

### Features

Summarize YouTube videos based on their transcripts.
Generate diagrams (e.g., flowcharts, concept maps) related to the video topic.
Create multiple-choice quizzes to test understanding.
User-friendly web interface powered by Gradio.

### Structure
```
youtube_summarizer/
├── src/
│   ├── llm_agent.py           # Handles Gemini API interactions
│   ├── transcript_fetcher.py  # Fetches YouTube video transcripts
│   ├── diagram_generator.py   # Generates topic-related diagrams
│   ├── quiz_generator.py      # Generates quizzes based on video content
│   └── app.py                # Gradio interface and main application logic
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── pyproject.toml            # UV package manager configuration
├── .env
└── LICENSE                   # MIT License
```

### Setup

* Clone the repository:
```bash
        git clone https://github.com/fatihcihant/youtube_summarizer.git
        cd youtube_summarizer
```

* Install uv:

        Follow instructions at uv documentation.

* Install dependencies:
```bash
        uv sync
```

* Set up environment variables:Create a .env file in the project root:
```bash
        GEMINI_API_KEY=your_gemini_api_key
```

* Run the application:
```bash
        uv run python src/app.py
```


### Usage

Open the Gradio interface in your browser.
Enter a YouTube video URL.
Click "Process Video" to generate the summary, diagram, and quiz.

### Dependencies

        Python 3.10+

        google-generativeai

        youtube-transcript-api

        gradio

        matplotlib

        graphviz

        python-dotenv

        pytest

### Contributing

Fork the repository.

Create a feature branch (git checkout -b feature/your-feature).

Commit changes (git commit -m 'Add your feature').

Push to the branch (git push origin feature/your-feature).

Open a pull request.

### License
MIT License. See LICENSE for details.
