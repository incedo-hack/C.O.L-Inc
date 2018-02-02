from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

class JDparser(object):
    
    def __init__(self):
        pass
    
    def readJd(self):
        dct = {}
        # print infile
        with open('D:\workspace\C.O.L.Inc\inputs/JD.txt', 'r') as myfile:
            data = myfile.read()
        #print(data)
        splitted_data = data.split("\n")
        dct['Job_Description'] = self.parseJobDescription(data)
        for position, item in enumerate(splitted_data):
            #print(position,item)
            try:
                item = item.strip()
                checkitem = item[:-1]
                if checkitem=='Job Title':
                    dct['Job_Title'] = splitted_data[position+1].replace('Â\xa0','').strip()
                elif checkitem=='Key Skills':
                    dct['Key_Skills'] = splitted_data[position+1].replace('Â\xa0','').strip()
                elif checkitem=='Location':
                    dct['location'] = splitted_data[position+1].replace('Â\xa0','').strip()
                elif checkitem=='Required Experience':
                    dct['Required_Experience'] = splitted_data[position+1].replace('Â\xa0','').strip()
                elif checkitem=='Job Description':
                    pass
                    #dct['Job_Description'] = self.parseJobDescription(splitted_data[position+1].replace('Â\xa0','').strip())    

            except:
                pass    
        #print splitted_data
        return dct
    def parseJobDescription(self,job_descriptio):
        words = obj.removeCommonWords(job_descriptio)
        not_an_englishWords = []
        for word_to_test in words:
            if not wordnet.synsets(word_to_test):
                if len(word_to_test) > 1:
                    filter_word = word_to_test.replace('â','').strip()
                    filter_word = filter_word.replace('€¢','').strip()
                    filter_word = filter_word.replace('€™','').strip()
                    filter_word = filter_word.replace('€','').strip()
                    not_an_englishWords.append(filter_word)
        
        return not_an_englishWords
            
    def removeCommonWords(self, sentence):
        try:
            if sentence is not None:
                filter = set(stopwords.words('english'))
                #filter.update(mystropWords)
                filter.discard('haven')
                word_tokens = set(word_tokenize(sentence.lower()))
                filtered_sentence = [w for w in word_tokens if not w in filter]
                return filtered_sentence
            else:
                return None
        except:
            return None 
    
if __name__ == '__main__':

    obj = JDparser()
    print(obj.readJd())
         
         