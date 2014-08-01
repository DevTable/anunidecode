import sys


def translate_line(line):
  found = line.find('qq{')
  while found >= 0:
    closing = line.find('},', found)
    to_replace = line[found+3:closing]
    replaced = '\'%s\'' % to_replace.replace('\'', '\\\'')
    line = line[:found] + replaced + line[closing+1:]
    found = line.find('qq{')

  return line


for filename in sys.argv[1:]:
  output_filename = filename[:-2] + 'py'
  print 'processing: %s' % filename
  with open(filename, 'r') as perl_input:
    to_translate = perl_input.readlines()[2:-2]
    translations = [translate_line(line) for line in to_translate]

    checked = eval('[' + ''.join(translations) + ']')
    print 'Found %s translations' % len(checked)

    content = ['page = [\n'] + translations + ['\n]\n']

    with open(output_filename, 'w') as python_output:
      python_output.writelines(content)
