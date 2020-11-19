# Daily Challenge : Text Analysis
# Download my_text.txt

# Write a class called Text, it accepts a string as argument and store the text in a attribute.
# Implement the following:
# a method to return the frequency of a word in the text 
# (assume words are separated by whitespace) return None or meaningful message
# a method that returns the most common word in the text
# a method that returns a list of the unique words in the text
# a classmethod that returns a instance of Text but with a text file: >>> Text.from_file('my_text.txt')
# Write a TextModification class that inherits from Text
# Implement the following:
# a method that returns the text without punctuation
# a method that returns the text without english stop-words (check out what this is !!)
# a method that returns the text without special characters
# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

from collections import Counter  


with open('my_text.txt')as f:
    text = f.read()
    

class Text():

    def __init__(self, text):
        self.text = text.lower
    

    def frequency(self, word):
        return text.count(word)

        

    def mostCommon(self):
        text_split = text.split()
        counter_text = Counter(text_split)
        common_word= counter_text.most_common(1)
        return common_word
        
    def unique(self):
        words = self.text.split()
        word_check = set(words)
        counting_dict= {}
        key =1

        for word in words:
            
            if word[0] != word_check:
                key += 1
                word_check = word
            if  word == word_check:
                counting_dict[key] = word
            else:
                if not isinstance(counting_dict[key],list):
                    counting_dict[key] = [counting_dict[key]]
                counting_dict[key].append(word)
 

        print(counting_dict)









    @classmethod
    def textFile(cls, file_path):        
        with open(file_path, "r") as f:
            file_contente = f.read()
        
        return file_contente



class TextModification(Text):

    def __init__(self, text):
        Text.__init__(self, text)

    def noPonctuation(self):
        remove_ponctuation = text.replace('.', '').replace(',', '').replace(';', '')
        return remove_ponctuation

    def noStop(self):
        pass

    def noSpecialChar(self):
        pass


# GET element in DICT
# dict.get("name")>>> avoid to make a crash if there is ValueError

map and filters wirks on list 