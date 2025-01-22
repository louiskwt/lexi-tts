import gtts, csv, os, argparse
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Lexi-tts", description="The text to speech tool for generating sound of the words. It's mainly used for the lexi project to create sound for a language learning game, but can also be used for other purposes", epilog="It's open source and in active development. So feel free to contribute")
    parser.add_argument('file_name', type=str, help='The program requires a file name to run. The file should be located in the same directory.')
    parser.add_argument('target_column', type=str, nargs="?", default="word", help="The program requires a target column to extract words from the csv. The default is set to 'word'")

    args = parser.parse_args()
    file_name = args.file_name
    target_column = args.target_column

    words = get_word_from_csv(file_name, target_column)
    generate_audio(words)
    find_duplicate(words)