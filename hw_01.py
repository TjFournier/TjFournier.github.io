'''
This script converts markdown documents into HTML documents.
Each function has its own doctests (just like in lab),
and you should begin this assignment by solving the doctests.
This will let you focus on completing just one small piece of the assignment at a time and not get lost in the "big picture".
Then, once all of these small pieces are complete,
the entire assignment will work "magically".
Dividing up a large project into smaller "doctestable" components is more of an art than a science.
As you get more experience programming,
you'll slowly learn how to divide up your code this way for yourself.
This is one of the main skills that separates senior programmers from junior programmers.
There's a handful of coding techniques in here that we haven't covered in class and you're not expected to understand.
This is intentional.
An important skill when learning a programming language is being able to work in an environment that you don't 100% understand.
(Again, this is similar to when learning a human language...
when we learn a new human languages,
we won't 100% understand everything in the new language,
but we still have to be able to work with the parts that we do understand.)
'''

################################################################################
#
# The functions in this section operate on only a single line of text at a time.
#
################################################################################


def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.
    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.
    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line[0:6] == '######':
        line = '<h6>' + line[6:] +'</h6>'
    if line[0:5] == '#####':
        line = '<h5>' + line[5:] +'</h5>'
    if line[0:4] == '####':
        line = '<h4>' + line[4:] +'</h4>'
    if line[0:3] == '###':
        line = '<h3>' + line[3:] +'</h3>'
    if line[0:2] == '##':
        line = '<h2>' + line[2:] +'</h2>'
    if line[0] == '#':
        line = '<h1>' + line[1:] +'</h1>'
    return line

def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".
    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.
    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i] == '*':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<i>' + line[start_index+1:stop_index] + '</i>' + line[stop_index+1:]
    else: 
        new_line = line

    return new_line

def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".
    HINT:
    This function is almost exactly the same as `compile_italic_star`.
    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i] == '_':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<i>' + line[start_index+1:stop_index] + '</i>' + line[stop_index+1:]
    else: 
        new_line = line

    return new_line


def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".
    HINT:
    The strikethrough annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.
    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i:i+2] == '~~':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<ins>' + line[start_index+2:stop_index] + '</ins>' + line[stop_index+2:]
    else: 
        new_line = line

    return new_line


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".
    HINT:
    This function is similar to the strikethrough function.
    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i:i+2] == '**':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<b>' + line[start_index+2:stop_index] + '</b>' + line[stop_index+2:]
    else: 
        new_line = line

    return new_line


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".
    HINT:
    This function is similar to the strikethrough function.
    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i:i+2] == '__':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<b>' + line[start_index+2:stop_index] + '</b>' + line[stop_index+2:]
    else: 
        new_line = line

    return new_line


def compile_code_inline(line):
    '''
    Add <code> tags.
    HINT:
    This function is like the italics functions because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.
    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('This example has a math formula in the  code: `1 + 2 < 4`')
    'This example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i:i+3] == '```':
            return line
        if line[i] == '`':
            if start_index == None:
                start_index = i
            else:
                stop_index = i
    if start_index is not None and stop_index is not None:           
        new_line = line[:start_index] + '<code>' + line[start_index+1:stop_index] + '</code>' + line[stop_index+1:]
    else: 
        new_line = line

    return new_line


def compile_links(line):
    '''
    Add <a> tags.
    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.
    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
    start_name_index = None
    stop_name_index = None
    start_site_index = None
    stop_site_index = None
    for i in range(len(line)):
        if line[i] == '[':
            if start_name_index == None:
                start_name_index = i
        if line[i] == ']':
            if stop_name_index == None:
                stop_name_index = i
        if line[i] == '(':
            if start_site_index == None:
                start_site_index = i
        if line[i] == ')':
            if stop_site_index == None:
                stop_site_index = i
    if start_site_index is not None and stop_site_index is not None:           
        new_line = line[:start_name_index] + '<a href="' + line[start_site_index+1:stop_site_index] + '">' + line[start_name_index+1:stop_name_index] + '</a>' + line[stop_site_index:]
    else: 
        new_line = line

    return new_line