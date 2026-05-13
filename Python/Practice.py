import itertools
import string
import time

target = "BrokEnBoY320#"
chars = string.ascii_letters + string.digits + string.punctuation
start = time.time()

for length in range(1, 8):
    for guess in itertools.product(chars, repeat=length):
        guess = ''.join(guess)
        print(f"Trying: {guess}")
        if guess == target:
            print(f"\n Password cracked: {guess}")
            print(f"Took {round(time.time() - start, 2)} seconds")
            break
    else:
        continue
    break



