import os
from google import genai

# Initialize the Gemini client (it automatically picks up GEMINI_API_KEY from your environment)
client = genai.Client()

def run_basic_automation():
    print("🤖 Agent is talking to Gemini...")
    
    # Send a prompt to the model (using gemini-2.5-flash as a fast, highly capable default)
    response = client.models.generate_content(
        model="gemini-3.8-flash",  # Updated model name
        contents="Write a short, 3-sentence summary of why using WSL and GitHub together is great for AI development.",
    )
    
    print("\n--- Gemini's Response ---")
    print(response.text)

if __name__ == "__main__":
    run_basic_automation()