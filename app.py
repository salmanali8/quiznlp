import streamlit as st
from nltk import ngrams, word_tokenize
import nltk

nltk.download('punkt')

st.title("N-gram Generator")

# Function to generate n-grams
def generate_ngrams(text, n):
    tokenized_text = word_tokenize(text)
    return list(ngrams(tokenized_text, n))

def main():
    text_input = st.text_area("Enter a text passage:")
    n_value = st.slider("Select the value of n for n-grams:", 2, 5)

    if st.button("Generate n-grams"):
        if text_input:
            st.write(f"### Generated {n_value}-grams:")
            n_grams = generate_ngrams(text_input, n_value)
            for gram in n_grams:
                st.write(gram)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
