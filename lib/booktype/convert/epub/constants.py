# -*- coding: utf-8 -*-
from booktype.utils import config

IMAGES_DIR = 'Images'
STYLES_DIR = 'Styles'
FONTS_DIR = 'Fonts'
DOCUMENTS_DIR = 'Text'
DEFAULT_LANG = 'en'

EPUB_VALID_IMG_ATTRS = frozenset([
    "alt", "class", "dir", "height", "id", "ismap", "longdesc",
    "style", "title", "usemap", "width", "xml:lang", "src", "transform-data"
])

EPUB_DOCUMENT_WIDTH = config.get_configuration('EPUB_DOCUMENT_WIDTH')
