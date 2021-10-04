def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.
    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    '''
    
    new_text = ''
    inside_tag = False
    for i in range(len(text)):
        if text[i] == '<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        else:
            if inside_tag == False:
                new_text += text[i]

    return new_text