def palindrome_check(string):

    return string == string[::-1]

def palindrome_check_manual(string):
    
    reversed_string = ""
    
    for char in reversed(string):
        reversed_string += char

    return string == reversed_string

def main():
    
    string= "abcdcba"
    
    print(palindrome_check(string))
    print(palindrome_check_manual(string))
    
if __name__ == "__main__":
    main()