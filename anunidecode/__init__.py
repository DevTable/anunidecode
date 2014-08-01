import codecs
import importlib
import sys

from collections import defaultdict


class PageLoadingDictionary(defaultdict):
  def __init__(self):
    super(PageLoadingDictionary, self).__init__(list)

  def __missing__(self, page_name):
    page_module_name = 'anunidecode.' + page_name[1:]
    try:
      importlib.import_module(page_module_name)
      loaded = sys.modules[page_module_name]
      page = loaded.page
    except ImportError:
      page = []

    self[page_name] = page
    return page


all_pages = PageLoadingDictionary()


def _translate_char(one_char, errors):
  page = "{0:#0{1}x}".format(ord(one_char) >> 8, 4)
  offset = ord(one_char) & 0xFF
  try:
    return all_pages[page][offset]
  except IndexError:
    if errors == 'strict':
      raise ValueError('Charcter %s was not in transliteration tables.' % one_char)
    elif errors == 'replace':
      return '[?]'
    elif errors == 'ignore':
      return ''


def encode(input_str, errors='strict'):
  output = ''.join([_translate_char(one_char, errors) for one_char in input_str])
  return (output, len(input_str))


def decode(input_str, errors='strict'):
  raise NotImplementedError


def unidecode_search_function(codec_name):
  if codec_name == 'unidecode':
    return codecs.CodecInfo(encode, decode)
  return None


codecs.register(unidecode_search_function)
