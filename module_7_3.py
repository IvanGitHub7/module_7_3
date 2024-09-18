class WordsFinder:
 
#Создаем объект класса WordsFinder

    def __init__(self, *args):
        self.file_names = []
        
#Проходим по названиям переданных файлов, собираем их в список

        for name in [args]:
           self.file_names += name
           
 #Создаём функцию, возвращающую словарь с ключом, содержащим названия файлов, и значением, содержащим список строк файлов без знаков препинания
 
    def get_all_words(self, *args):
        all_words = {}
        for index in self.file_names:   
            line2 = ''
            with open(index, encoding = 'utf-8') as file:
                 for line in file:
                     for char in line:
                         if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                             del(char)
                         else:
                             line2 += char.lower()
                 line2 = line2.split()
                 all_words[index] = line2
        return all_words

#Создаем функцию, находящую в файлах переданное слово, и возвращающую словарь с названиями файлов в качестве ключа и позицией первого искомого слова в качестве значения  
            
    def find(self, word):
        find_dict = {}
        find_dict_value = None
        for name, words in WordsFinder.get_all_words(self).items():
            for element in words:
                if word.lower() == element:
                    find_dict_value = words.index(element) +1
            find_dict[name] = find_dict_value
        return find_dict
        
#Создаем функцию, находящую в файлах переданное слово, и возвращающую словарь с названиями файлов в качестве ключа и количеством искомых слов в качестве значения  
        
    def count(self, word):
        find_dict = {}
        find_dict_value = 0
        for name, words in WordsFinder.get_all_words(self).items():
            for element in words:
                if word.lower() == element:
                    find_dict_value += 1
            find_dict[name] = find_dict_value
        return find_dict
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего   