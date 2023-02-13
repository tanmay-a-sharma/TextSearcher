import string


class TextSearcher(object):

    def __init__(self):
        # Initialize the instance variable 'text' to None
        self.text = None

    # Method to load a text file
    def load(self, file_path:str)->bool:
        # If the file path is None, return False
        if file_path is None:
            return False
    
        # Try to open and read the file, and store the contents in the 'text' instance variable
        try:
            with open(file_path, 'r') as f:
                self.text = f.read()
            return True

        # If the file is not found, return False
        except FileNotFoundError:
            return False
    

    def search(self, word:str, context:int=0)->list:
        # Searches for the given word in the text and returns the list of substrings

        # If the text is None, return an empty list
        if self.text is None:
            return []

        # Split the text into a list of words
        words = self.text.split()
        results = []

        # Iterate through the words in text
        for i, w in enumerate(words):
            # Check if the current word matches the searched word (case-insensitive)
            if w.lower() == word.lower():
                # Calculate the start and end indices for the substring to include the context
                start = max(0, i - context)
                end = min(len(words), i + context + 1)
                # Join the words in the substring to form a string
                result = ' '.join(words[start:end])
                results.append(result)
        
        # Remove punctuation from the results
        results = [result.translate(str.maketrans("", "", string.punctuation)) for result in results]
        
        # Return the list of substrings
        return results




    def search(self, word:str, context:int=0)->list:
        

        if self.text is None:
            return []

        words = self.text.split()
        results = []
    
        for i, w in enumerate(words):
            if w.lower() == word.lower():
                start = max(0, i - context)
                end = min(len(words), i + context + 1)
                result = ' '.join(words[start:end])
                results.append(result)
        return results

"""

def search(self, word:str, context:int=0)->list:


        #Failed: 
        #FAILED test_matches_quotes_correctly[Early-1-expected_result1] - assert ['an early pr...ery early in'] == ['Govinda: "E...ng. Early in']
        #FAILED test_matches_beginning_of_file[shade-4-expected_result0] - AssertionError: assert ['In the mang...he house, in'] == ['In the shad...to his black']
        #FAILED test_matches_end_of_file[universe-3-expected_result0] - AssertionError: assert [] == ['one with the universe.']
        #FAILED test_multiple_searches_on_one_file - AssertionError: assert ['In the mang...he house, in'] == ['In the shad...to his black']
        #FAILED test_matches_overlapping_results[universe-3-expected_result0] - AssertionError: assert [] == ['one with the universe.']
        # If the text is None, return an empty list
        if self.text is None:
            return []

        # Split the text into words
        words = self.text.split()
        results = []

        # Iterate through the words in the text
        for i, w in enumerate(words):
            # If the current word matches the search word (case-insensitive)
            if w.lower() == word.lower():
                # Calculate the start and end indices of the context
                start = max(0, i - context)
                end = min(len(words), i + context + 1)
                # Join the context words into a single string
                result = ' '.join(words[start:end])
                # Add the result to the list of results
                results.append((i, result))
    
        # Sort the results based on their proximity to the middle of the text
        results.sort(key=lambda x: abs(x[0] - len(words)//2))
        # Return a list of just the result strings
        return [result[1] for result in results]












        
    def search(self, word:str, context:int=0)->list:
    # If the text is None, return an empty list
    if self.text is None:
        return []

    # Split the text into words
    words = self.text.split()
    results = []

    # Iterate through the words in the text
    for i, w in enumerate(words):
        # If the current word matches the search word (case-insensitive)
        if w.lower() == word.lower():
            # Calculate the start and end indices of the context
            start = max(0, i - context)
            end = min(len(words), i + context + 1)
            # Join the context words into a single string
            result = ' '.join(words[start:end])
            # Add the result to the list of results
            results.append((i, result))
    
    # Sort the results based on their proximity to the middle of the text
    results.sort(key=lambda x: abs(x[0] - len(words)//2))
    # Return a list of just the result strings
    return [result[1] for result in results]








    def search(self, word:str, context:int=0)->list:    
        if self.text is None:
            return []

        word = word.lower()
        words = self.text.lower().split()
        results = []
        for i, w in enumerate(words):
            if w == word:
                start = max(0, i - context)
                end = min(len(words), i + context + 1)
                result = ' '.join(words[start:end])
                results.append(result)
        return results



text_searcher = TextSearcher()
file_path = "files/Siddhartha.opening.txt"
result = text_searcher.load(file_path)

if result:
    print("File loaded")
else:
    print("File not found")


    def load(self, file_path:str)->bool:
        try:
            with open(file_path, 'r') as f:
                self.text = f.read()
            return True
        except FileNotFoundError:
            return False
"""