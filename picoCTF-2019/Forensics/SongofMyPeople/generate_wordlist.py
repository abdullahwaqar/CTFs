def generate_word_list(word_seed, word_count=None):
    if word_count is None:
        word_count = len(word_seed)
    file = open('wordlist.txt', 'w+')
    for current in range(word_count):
        a = [i  for i in word_seed]
        for y in range(current):
            a = [x + i for i in word_seed for x in a]
        file.write(b'a')
    file.close()

if __name__ == '__main__':
    generate_word_list('Check Yo Self')
