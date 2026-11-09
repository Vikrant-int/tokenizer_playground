import tiktoken

# Initialize tokenizer for GPT-4
tokenizer = tiktoken.encoding_for_model("gpt-4")

# Input text
text = "Who are you?"

# Encode text into token IDs
token_ids = tokenizer.encode(text)

print("Original Text:", text)
print("Token IDs:", token_ids)
print("Number of Tokens:", len(token_ids))

# Decode token IDs back into text
result = tokenizer.decode(token_ids)

print("Decoded Text:", result)
