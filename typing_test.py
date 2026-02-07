##Ideas that can be used as extension

#1)Instead of using a seperate python file for text_samples, import them from any external library
#2)Instead of giving similar text, give seperate text according to the level
#3)Can run a time limit instead of waiting until the user stops typing

from samples import SAMPLES
import random
import time

def get_random_text(difficulty):
    return random.choice(SAMPLES[difficulty])

def wpm(typed_text,start_time,end_time):
    time = (end_time-start_time)/60
    if time == 0:
        return 0
    text = typed_text.split()

    return round(len(text)/time)

def accuracy(typed_text,original_text):
    type = typed_text.split()
    original = original_text.split()
    if len(original) == 0:
        return 0.0
    correct = 0
    for o,t in zip(original,type):
        if t == o:
            correct +=1

    return round((correct/len(original))*100,2)

def main():
    print("\n Welcome to Python typing test! \n")
    print("Please enter your difficulty as Easy/Hard:")
    difficulty = (input().strip()).upper()
    Text = get_random_text(difficulty)
    print("\nType the following text as fast and accurately as you can:\n")
    print(f"\033[1;31m{Text}\033[0m\n")
    print("Press enter to start your typing")
    input()
    print("Start!")
    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    Acc = accuracy(typed_text,Text)
    wp_m = wpm(typed_text,start_time,end_time)
    elapsed = round(end_time-start_time,2)

    print("\n--- Results ---")
    print(f"Time taken: {elapsed} seconds")
    print(f"Words per minute (WPM): {wp_m}")
    print(f"Accuracy: {Acc}%")
    print("\nThank you for using the Typing Speed Test! Keep practicing!\n")


if __name__ == "__main__":
    main()


    
        

