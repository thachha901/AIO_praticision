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


if __name__ == "__main__":
    s1 = "hola"
    s2 = "hello"
    
    print(f"Levenshtein distance between '{s1}' and '{s2}': {levenshtein_distance(s1, s2)}")