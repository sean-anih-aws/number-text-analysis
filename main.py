import re


def get_avg_length(user_text):
    sentences = re.split(r"[.!?]", user_text)
    words_per_sentence = [len(s.split(" ")) for s in sentences]
    return round(sum(words_per_sentence) / len(words_per_sentence), 1)


nums_or_text_prompt = input(
    "Enter 'numbers' to process numbers (0,1,2,etc.) or 'text' to process alphameric text: "
)


if nums_or_text_prompt == "text":
    try:
        user_prompt = input("Enter the text you want to analyze:\n")

        characters = len(user_prompt)

        word_count = len(user_prompt.split(" "))

        sentence_count = len(re.split(r"[.!?]+", user_prompt.rstrip(".!?")))

        avg_word_length = round(
            sum(len(word) for word in user_prompt.split(" ")) / word_count, 1
        )

        avg_sentence_length = get_avg_length(user_prompt)

        most_frequent_word = max(
            set(user_prompt.split(" ")), key=user_prompt.split(" ").count
        )

        print(
            f"""
            Text analysis results
            ---------------------
            Total characters: {characters}
            Total words: {word_count}
            Total sentences: {sentence_count}
            Most frequent word: {most_frequent_word}
            Avg word length: {avg_word_length} letters
            Avg sentence length: {avg_sentence_length} words
            """
        )
    except Exception as e:
        print(f"Please try again. An error occurred: {e}")

elif nums_or_text_prompt == "numbers":
    user_nums = input("Enter a list of numbers separated by a space:\n")

    try:
        nums = [int(num) for num in user_nums.split(" ")]
        total_nums = len(nums)
        sum_nums = sum(nums)
        range_nums = max(nums) - min(nums)
        most_frequent_num = max(set(nums), key=nums.count)
        avg_num = sum_nums / total_nums

        print(
            f"""
            Number analysis results
            ---------------------
            Total numbers: {total_nums}
            Sum of numbers: {sum_nums}
            Range of numbers: {range_nums}
            Most frequent number: {most_frequent_num}
            Total Average: {avg_num}
            """
        )

    except ValueError:
        print("Please enter only numbers separated by spaces.")
        exit()

else:
    print('Only the options "numbers" or "text" will be accepted. Please try again.')
