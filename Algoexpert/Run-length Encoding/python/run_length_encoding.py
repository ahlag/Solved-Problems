# O(n) time | O(n) space - where n is the length of the input string
def run_length_encoding(string):
    
	encoded_string_characters, current_run_length = [], 1
	
	n = len(string)

	for i in range(1, n):
		
		current_character = string[i]
		previous_character = string[i-1]
		
		if current_character != previous_character or current_run_length == 9:
			encoded_string_characters.append(str(current_run_length))
			encoded_string_characters.append(previous_character)
			current_run_length = 0
			
		current_run_length += 1


	# Handle the last run
	encoded_string_characters.append(str(current_run_length))
	encoded_string_characters.append(string[len(string)-1])
		
	return "".join(encoded_string_characters)
		
def main():
    
    string = "AAAAAAAAAAAAABBCCCCDD"
    
    print(run_length_encoding(string))    
    
if __name__ == "__main__":
    main()