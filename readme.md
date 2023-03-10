# eda

a collection of scripts for exploratory data analysis.

## useful notebook settings

ignore all warnings:
```
import warnings
warnings.filterwarnings('ignore')
```

ignoring specific warnings:
```
ignore_warnings = [DeprecationWarning, FutureWarning, DataConversionWarning, ConvergenceWarning]
for w in ignore_warnings: warnings.filterwarnings('ignore', category=w)
```

data frame display:
```
# Use 2 decimal places in output display
pd.set_option('display.precision', 2)

# Don't wrap repr(DataFrame) across additional lines
pd.set_option('display.expand_frame_repr', False)

# Set max row and column display
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
```

note new `seaborn` theme setting syntax:
```
import seaborn as sns
sns.set_theme()
```

plot pretty figures and avoid blurry images:
```
%config InlineBackend.figure_format = 'retina'
```

larger scale for plots in notebooks:
```
sns.set_context('notebook')
```

to run multiple commands in a single cell, so can show `df.head()` and `df.info()` form the same cell:
```
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
```

reload modules into notebook:
```
%load_ext autoreload
```

