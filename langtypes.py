class Token:  
    """ Stores information about a word.
    Reference: https://cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.Token 
    """
 
    def __init__(self, content_input='', offset_input='0', lemma_input='', partofSpeech_tag = "UNKNOWN") -> None:
        """ Initialize token with basic attributes.

        Given text 'hello worlds'
        content_input    : a singular word (i.e. 'worlds' )
        offset_input     : 1-indexed offset of word (i.e. 6 for world)
        lemma_input      : lemma of word. i.e. 'world'
        partofSpeech_tag : only 'ADJ' or 'NOUN' supported.
        """
        self.lemma = lemma_input
        
        # TODO: throw exception if invalid tag. 
        self.partOfSpeech = PartOfSpeech()
        self.partOfSpeech.tag = partofSpeech_tag

        self.text = Text()
        self.text.beginOffset = offset_input
        self.text.content = content_input
    
    def __str__(self) -> str:
        return_string = "token : {\n"
        return_string += f"    lemma: {str(self.lemma)}\n"
        return_string += f"    {str(self.partOfSpeech)}\n"
        return_string += f"    {str(self.text)}\n"
        return_string += '}\n'

        return str(return_string)


class Sentence:
    """ Contains sentence information. Missing sentiment analysis ability.
    Reference:  
    https://cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.Sentence 
    """
    def __init__(self, content_input = '', offset_input = '0') -> None:
        """ Initialize sentence with basic attributes.

        Given text 'hello worlds. My name is Earth.'
        content_input    : a sentence (i.e. 'My name is Earth' )
        offset_input     : 1-indexed offset of sentence in entire text (i.e. 14)
        """
        self.text = Text()
        self.text.beginOffset = offset_input
        self.text.content = content_input

    def __str__(self) -> str:
        return_string = "sentence: {\n"
        return_string += f"    '{str(self.text)}'\n"
        return_string += '    }\n'

        return str(return_string)

class PartOfSpeech:
    def __init__(self) -> None:
        self.tag = ''
    
    def __str__(self) -> str:
        return_string = "partofspeech: {\n"
        return_string += f"    'tag' : '{self.tag}'\n"
        return_string += '    }\n'

        return str(return_string)

class Text:
    def __init__(self) -> None:
        self.content = ''
        self.beginOffset = 0
    
    def __str__(self) -> str:
        return_string = "text : {\n"
        return_string += f"    'content' : '{self.content}'\n"
        return_string += f"    'beginOffset' : '{str(self.beginOffset)}'\n"
        return_string += '}\n'

        return str(return_string)
