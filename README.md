# GPT-4 Tokenizer Demo (tiktoken)

A small Python project that demonstrates text tokenization using OpenAI's [`tiktoken`](https://github.com/openai/tiktoken) library with the GPT-4 tokenizer.

## What is tokenization?

Tokenization is the process of converting text into smaller units called **tokens** before it is processed by a language model. Tokens can represent whole words, parts of words, punctuation, or whitespace. Language models work with token IDs (integers) rather than raw text, and token counts affect input limits, processing cost, and how text is interpreted.

## What is OpenAI's `tiktoken` library?

`tiktoken` is a fast Byte Pair Encoding (BPE) tokenizer library from OpenAI. It provides tokenizers compatible with OpenAI models, allowing you to encode text into token IDs and decode token IDs back into text. This is useful for understanding prompt length, debugging model inputs, and learning how models represent text.

## How the GPT-4 tokenizer works in this project

This project uses:

```python
tokenizer = tiktoken.encoding_for_model("gpt-4")
```

`tiktoken` selects the encoding appropriate for the specified model (`gpt-4`). The resulting tokenizer can:

- **Encode**: convert a string into a list of integer token IDs.
- **Decode**: convert a list of token IDs back into a string.
- **Count tokens**: determine how many tokens a piece of text uses (`len(token_ids)`).

## Encoding text into token IDs

The script encodes the input text with:

```python
token_ids = tokenizer.encode(text)
```

This produces the token IDs the model would use to represent the text.

## Decoding token IDs into text

The script decodes the token IDs back into text with:

```python
result = tokenizer.decode(token_ids)
```

The decoded result should match the original input text.

## Token counting

Token count is calculated as:

```python
len(token_ids)
```

This shows how many tokens the input consumes for the selected tokenizer.

## Installation

1. Ensure Python 3 is installed.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to run the program

From the project directory, run:

```bash
python main.py
```

## Example output (actual execution)

The following output was produced by running `python main.py` in this project:

```text
Original Text: Who are you?
Token IDs: [15546, 527, 499, 30]
Number of Tokens: 4
Decoded Text: Who are you?
```

## Project files

- `main.py` — demonstrates encoding, decoding, and token counting with the GPT-4 tokenizer.
- `requirements.txt` — Python dependency (`tiktoken`).
- `.gitignore` — common Python/virtual environment exclusions.
- `README.md` — project documentation.
