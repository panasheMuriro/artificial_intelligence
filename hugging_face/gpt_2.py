from transformers import pipeline

# Load the GPT-2 model for text generation
generator = pipeline('text-generation', model='gpt2')

# Generate text
output = generator("Hugging Face is", max_length=50)
print(output)