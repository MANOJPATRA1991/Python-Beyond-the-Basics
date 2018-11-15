from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

# Only show what is specified here when this module is imported by any other module
__all__ = ['bz2_opener', 'gzip_opener']