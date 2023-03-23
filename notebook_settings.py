'''
usefull notebook settings. 
'''

# ignore all warnings
import warnings; warnings.filterwarnings('ignore')

# ignoring specific warnings
ignore_warnings = [DeprecationWarning, FutureWarning, DataConversionWarning, ConvergenceWarning]
for w in ignore_warnings: warnings.filterwarnings('ignore', category=w)

# use 4 decimal places in output display
pd.set_option('display.precision', 4)

# don't wrap repr(DataFrame) across additional lines
pd.set_option('display.expand_frame_repr', False)

# set max row and column display
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)

# plot pretty figures and avoid blurry images
%config InlineBackend.figure_format = 'retina'

# larger scale for plots in notebooks:
sns.set_context('notebook')

# to run multiple commands in a single cell, so can show `df.head()` and `df.info()` form the same cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# reload modules into notebook
%load_ext autoreload

