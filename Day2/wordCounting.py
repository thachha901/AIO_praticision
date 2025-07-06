def count_word(input_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()
        
    words = text.split()
    
    word_count = {}
    for word in words:
        word = word.strip('.,;:[](){}!?')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

if __name__ == "__main__":
    input_file = "data.txt"
    result = count_word(input_file)
    print(f"Word count for '{input_file}': {result}")