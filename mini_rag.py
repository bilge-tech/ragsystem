# --- STEP 1: Read documents ---

def read_file(filename):
    """Opens a text file and returns its content as a string."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# Read the 3 documents
documents = {
    "doc1.txt": read_file("doc1.txt"),
    "doc2.txt": read_file("doc2.txt"),
    "doc3.txt": read_file("doc3.txt"),
}




# --- STEP 2: Chunking (split into sentences) ---

def chunk_text(text, source_file):
    """Splits a text into sentences, returns each chunk with its source."""
    sentences = text.split(".")
    chunks = []
    for sentence in sentences:
        sentence = sentence.strip()  # remove leading/trailing whitespace
        if sentence:  # skip empty strings
            chunks.append({
                "text": sentence,
                "source": source_file
            })
    return chunks

# Chunk all documents, collect them into one list
all_chunks = []
for name, content in documents.items():
    all_chunks.extend(chunk_text(content, name))

