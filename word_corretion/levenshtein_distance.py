import streamlit as st

def levenshtein_distance(s1, s2):
    
    distances = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    
    for t1 in range(len(s1) + 1):
        distances[t1][0] = t1
    
    for t2 in range(len(s2) + 1):
        distances[0][t2] = t2
    
    for idx in range(1, len(s1) + 1):
        for jdx in range(1, len(s2) + 1):
            distances[idx][jdx] = min(
                distances[idx - 1][jdx] + 1, # deletion
                distances[idx][jdx - 1] + 1, #insertion
                distances[idx - 1][jdx -1] + (0 if s1[idx - 1] == s2[jdx - 1] else 1)
            )
        
    
    return distances[-1][-1]

def load_vocabulary(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    words = sorted(set([line.strip().lower() for line in lines]))
    return words




if __name__ == "__main__":
    st.title("Word Correction Tool")
    word = st.text_input("Your word:")
    
    vocabs = load_vocabulary("vocab.txt")
    
    if st.button("Compute"):
        distances = dict()
        for vocab in vocabs:
            distance = levenshtein_distance(word, vocab)
            distances[vocab] = distance
            
        sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        
        word_correct = list(sorted_distances.keys())[0]
        st.write('Corrected word: ', word_correct)
        
        col1, col2 = st.columns(2)
        col1.write(vocabs)
        col2.write(sorted_distances)
    
