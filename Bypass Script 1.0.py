import random

#Created by Liber
substitutions = {
    'a': '@',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '$',
    't': '7'
}

def obfuscate_text(text):
    obfuscated = []
    for char in text:
       
        if char.lower() in substitutions:
            obfuscated.append(substitutions[char.lower()])
        else:
            obfuscated.append(char)
    return ''.join(obfuscated)

def format_text(text):
    
    formatted = text
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    
    
    if random.choice([True, False]):
        index = random.randint(0, len(formatted) - 1)
        formatted = formatted[:index] + random.choice(special_chars) + formatted[index:]
    
    return formatted

def bypass_prompt(prompt):
    
    obfuscated_text = obfuscate_text(prompt)
    
    
    formatted_text = format_text(obfuscated_text)
    
    return formatted_text

def main():
    
    user_prompt = input("Enter the prompt to bypass: ")
    
    
    bypassed_prompt = bypass_prompt(user_prompt)
    
    # Output the result
    print("\nBypassed Prompt:")
    print(bypassed_prompt)

if __name__ == "__main__":
    main()
