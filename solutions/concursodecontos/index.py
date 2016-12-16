# coding=utf-8

# Número de Palavras
N = 5
# Número máximo de linhas/página
L = 2
# Número máximo de caracteres/linha
C = 2

story = "a de i de o"

def contest(N, L, C, story):

  lines = []
  pages = []

  # Verifica as restrições da entrada
  if 2 > N or N > 100: return "N inválido!"
  if 1 > L or L > 30: return "L inválido!"
  if 1 > C or C > 70: return "C inválido!"

  words = story.split(" ")
  for word in words:
    #print word
    if 1 > len(word) or len(word) > C:
      return "Palavra com o comprimento fora do estabelecido!"

  count_line = 0
  count_page = 0

  line = []

  print story.replace(" ", "$#")

  words = story.replace(" ", "$#").split("#")
  for word in words:
    print "WORD", word
    #Total de caracteres da linha
    total = count_line + len(word)

    if total <= C:
      count_line = total
      line.append(word)
    else:
      print "N de linhas", len(lines)
      if len(lines) < L:
        lines.append("".join(line).replace("$", " "))
        print "Nova linha", line
        line = [word]
        count_line = len(word)
      else:
        print "Linhas",  lines
        pages.append(lines)
        line = [word]
        count_line = len(word)

  print pages
  return "Tudo verificado!"


print contest(N, L, C, story)






