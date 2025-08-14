numbers = {1: 'One',
           2: 'Two',
           3: 'Three',
           4: 'Four',
           5: 'Five',
           6: 'Six',
           7: 'Seven',
           8: 'Eight',
           9: 'Nine',
           10: 'Ten',
           11: 'Eleven',
           12: 'Twelve',
           13: 'Thirteen',
           14: 'Fourteen',
           15: 'Fifteen',
           16: 'Sixteen',
           17: 'Seventeen',
           18: 'Eighteen',
           19: 'Nineteen',
           20: 'Twenty',
           30: 'Thirty',
           40: 'Forty',
           50: 'Fifty',
           60: 'Sixty',
           70: 'Seventy',
           80: 'Eighty',
           90: 'Ninety'
           }

words_to_num = {v: k for k, v in numbers.items()}
words_to_num['Zero'] = 0  

multipliers = {
    'Hundred': 100,
    'Thousand': 1000,
    'Million': 1000000,
    'Billion': 1000000000,
    'Trillion': 1000000000000
}

amounts = []
for num in range(0, 27):
    if num == 0:
        amounts.append('')
    elif num <= 20:
        amounts.append(numbers[num])
    else:
        tens = (num // 10) * 10
        ones = num % 10
        amounts.append(numbers[tens] + " " + numbers[ones])

def convertTwoDigit(n):
    if n == 0:
        return ''
    if n <= 20:
        return numbers.get(n)
    tens = (n // 10) * 10
    ones = n % 10
    if ones == 0:
        return numbers.get(tens)
    else:
        return numbers.get(tens) + " " + numbers.get(ones)

def convertThreeDigit(n):
    if n == 0:
        return ''
    if n < 100:
        return convertTwoDigit(n)
    hundreds = n // 100
    remain = n % 100
    if remain == 0:
        return numbers.get(hundreds) + " Hundred"
    else:
        remainder_string = convertTwoDigit(remain)
        return numbers.get(hundreds) + " Hundred " + remainder_string

def chunk_divide(n):
    if n == 0:
        return ''
    elif n <= 20:
        return numbers.get(n)
    elif n < 100:
        return convertTwoDigit(n)
    else:
        return convertThreeDigit(n)

def amountInWords(n):
    if n == 0:
        return 'Zero'
    chunks = []
    temp = n
    while temp > 0:
        chunks.append(temp % 1000)
        temp //= 1000
    chunks.reverse()

    magnitudes = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
    words_parts = []

    for i in range(len(chunks)):
        chunk = chunks[i]
        if chunk == 0:
            continue
        chunk_words = chunk_divide(chunk)
        magnitude_index = len(chunks) - i - 1
        if magnitude_index > 0 and magnitude_index < len(magnitudes):
            words_parts.append(chunk_words + " " + magnitudes[magnitude_index])
        else:
            words_parts.append(chunk_words)

    return " ".join(words_parts)

def wordsToNumber(words):
    parts = words.strip().split()
    if len(parts) == 1 and parts[0].capitalize() == "Zero":
        return 0 
    total = 0
    current = 0
    for word in parts:
        word = word.capitalize()
        if word in words_to_num:
            current += words_to_num[word]
        elif word == 'Hundred':
            current *= 100
        elif word in multipliers:
            current *= multipliers[word]
            total += current
            current = 0
        else:
            return None
    return total + current

while True:
    user_input = input("Enter number or words (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break
    if user_input.isdigit():
        num = int(user_input)
        print(amountInWords(num))
    else:
        result = wordsToNumber(user_input)
        if result is None:
            print("Invalid input. Try again.")
        else:
            print(result)
