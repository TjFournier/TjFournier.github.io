f1 = open('dracula.html', 'r')
f2 = open('izbicki.html', 'w')
check_words = ("dracula", "DRACULA", "D R A C U L A", "Dracula", "<strong>D R A C U L A</strong>", "<strong>dracula</strong>", "<strong>DRACULA</strong>", "D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A", "<big>D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A</big>", "<strong>D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A</strong>", "count", "Count", "count,", "Count,", "count.", "Count.", "Bram Stoker", "Bram&nbspStoker", "<big>Bram &nbsp; Stoker</big>")
rep_words = ("izbicki", "IZBICKI", "I Z B I C K I", "Izbicki", "<strong>I Z B I C K I</strong>", "<strong>izbicki</strong>","<strong>IZBICKI</strong>", "I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I", "<big>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</big>", "<strong>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>","professor", "Professor","professor,","Professor,","professor.","Professor.", "TJ Fournier", "TJ&nbspFournier", "<big>TJ &nbsp; Fournier</big>")

for line in f1:
    for check, rep in zip(check_words, rep_words):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()