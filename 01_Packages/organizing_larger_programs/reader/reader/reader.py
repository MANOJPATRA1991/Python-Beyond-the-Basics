import os

from reader.compressed import bzipped, gzipped

extension_map = {
  '.bz2': bzipped.opener,
  '.gz': gzipped.opener,
}

class Reader:
  def __init__(self, filename):
    """Some docstring"""
    extension = os.path.splitext(filename)[1]
    # Use default file opener if no opener found for the requested file
    opener = extension_map.get(extension, open)
    self.filename = filename
    self.f = opener(self.filename, 'rt')

  def close(self):
    self.f.close()

  def read(self):
    return self.f.read()
