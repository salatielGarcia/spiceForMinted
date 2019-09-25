from setuptools import setup, find_packages
 
setup (
  name='spice',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  spice = spice.lexer:SpiceLexer
  """,
)
