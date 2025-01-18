import os

def find_missing_rows(words):
    file_list = os.listdir("output")
    generated_phrase_list = [f.replace(".mp3", '') for f in file_list]
    print(len(words), len(generated_phrase_list))
    return [p for p in generated_phrase_list if p not in words] 

def find_duplicate(words):
    seen = set()
    duplicates = []
    for w in words:
        if w not in seen:
            seen.add(w)
        else:
            duplicates.append(w)
        
    print(duplicates)  
