import gzip
import shutil

with gzip.open("kdd/kddcup.data_10_percent_corrected", "rb") as f_in:
    with open("kdd/kddcup.data_10_percent.csv", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

import gzip
import shutil

with gzip.open("kdd/kddcup.names", "rb") as f_in:
    with open("kdd/kddcup.names.csv", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)






