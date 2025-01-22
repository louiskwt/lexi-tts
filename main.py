import gtts, csv, os
from utils import find_duplicate

def get_word_from_csv(filename: str, target_column: str ="word") -> list[str]:
    words = []
    with open(filename, mode='r') as f:
        csvFile = csv.DictReader(f)
        for row in csvFile:
            words.append(row[target_column])
    return words

def generate_audio(words: list[str]) -> None:
    if not os.path.exists('output'):
        os.makedirs("output")
    else:
        for word in words:
            tts = gtts.gTTS(f'{word}', slow=True)
            tts.save(f'output/{word}.mp3')

words = get_word_from_csv('words.csv', "word")

generate_audio(words)
find_duplicate(words)