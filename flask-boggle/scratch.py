import boggle

def try_to_read_words():
    with open(r'C:\Users\valex\Desktop\Springboard_Assignments\springboard_boggle\flask-boggle\words.txt') as words:
        my_words = [word.strip() for word in words]
        print(my_words)
try_to_read_words()