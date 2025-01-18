import gtts, csv, os

def get_word_from_csv(filename, target_column="word"):
    words = []
    with open(filename, mode='r') as f:
        csvFile = csv.DictReader(f)
        for row in csvFile:
            words.append(row[target_column])
    return words

def generate_audio(words):
    if not os.path.exists('output'):
        os.makedirs("output")
    else:
        for word in words:
            tts = gtts.gTTS(f'{word}', slow=True)
            tts.save(f'output/{word}.mp3')

words = get_word_from_csv('phrase.csv', "phrase")
generate_audio(words)
