# This file is part of the Volt package and is governed by its license.
# See Volt's LICENSE file for details.
# 
# (c) Wibowo Arindrarto <bow@bow.web.id>

import codecs
import os
import re

import yaml


_MARKUP = {
           '.markdown': 'markdown', '.md': 'markdown',
           '.rst': 'rst', '.textile': 'textile',
           '.html': 'html'
          }


class ParseError(Exception):
    pass


class Content(object):
    """Class that represents a content object in volt.

    At the moment it is only for text content (blog posts, pages).
    Support for other content types (e.g. images) is planned for
    future releases.

    """
    
    def __init__(self, filename):
        """Initializes the Content object.

        Args:
          filename: filename of text content.

        """
        self.filename = filename
        with codecs.open(filename, 'r', 'utf8') as source:
            self._parse_text_content(source)
        self.markup = self._get_markup_lang()

    def _get_markup_lang(self):
        """Returns the content markup language.

        Markup language is guessed first and foremost based on the 
        file extension. Failing that, the method checks if the header 
        specifies 'markup'. If no 'markup' is specified or if the 
        specified markup is not implemented, a ParseError exception is raised.

        """
        ext = os.path.splitext(self.filename)[1]
        if ext in _MARKUP:
            return _MARKUP[ext]
        else:
            if 'markup' in self.metada and \
                    self.metada['markup'].lower() in _MARKUP.values():
                return self.metada['markup'].lower()
            else:
                raise ParseError("Markup language unknown or unimplemented in \
                        %s(filename)." % self.filename)

    def _parse_text_content(self, source):
        """Parses the content of a text file.

        Parsing results are stored in self.metadata (for the header)
        and self.content (for the content itself).

        Args:
          source: file object that implements read()

        """
        pattern = re.compile(r'^---$', re.MULTILINE)
        parsed = filter(None, pattern.split(source.read()))
        header = yaml.load(parsed.pop(0))
        if not isinstance(header, dict):
            raise ParseError("Header format unrecognizable in %(filename)." \
                    % self.filename)
        self.metadata = header
        self.content = parsed.pop(0).strip()