import time
import sys

def print_lyrics():
    lyrics = [
        "Tanne main likhu rani dil ki...",
        "Ya tanne Mumtaj likhunga...",
        "Je likhne mein baith gaya tanne...",
        "To pakka main kitab likhunga...",
        "",
        "Re hothan ne gulaab likhunga...",
        "Re akhya ne sharaab likhunga...",
        "",
        "Jo dikh ja tu khwaab likhunga...",
        "To pakka main kitab likhunga..."]
    
    delays = [0.2, 0.5]

    print("Kitab:\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()

        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()