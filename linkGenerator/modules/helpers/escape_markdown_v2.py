def escape_markdown(text, keep=None):
    """Escapes special characters in a Markdown_V2 string to prevent formatting issues.

    Args:
        text (str): The text you want to escape.
        keep (list, optional): A list of entity types whose characters should not be escaped.
                               Valid entity types are:
                               - 'bold' for bold characters (*)
                               - 'italic' for italic characters (_)
                               - 'underline' for underline characters (_)
                               - 'strikethrough' for strikethrough characters (~)
                               - 'code' for inline code characters (`)
                               - 'link' for link characters ([, ], (, ))

                               Defaults to None, meaning all special Markdown_V2 characters will be escaped.
        
    Returns:
        str: The text with Markdown_V2 special characters escaped. 
             Returns None if the input text is None.
    """     
    if text is None:
        return
    
    markdown_v2_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    escaped_text = ''
    
    for char in text:
        if char in markdown_v2_chars and (keep is None or char not in get_keep_chars(keep)):
            escaped_text += '\\' + char
        else:
            escaped_text += char
    
    return escaped_text

def get_keep_chars(keep):
    keep_chars = {
        'bold': ['*'],
        'italic': ['_'],
        'underline': ['_'],
        'strikethrough': ['~'],
        'code': ['`'],
        'link': ['[', ']', '(', ')']
    }
    
    chars = []
    for entity_type in keep:
        chars.extend(keep_chars.get(entity_type, []))
    
    return chars
