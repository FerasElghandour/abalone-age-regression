# Data and input preparation

The full notebook expects a local `abalone.csv` in the repository root, with a header and these columns in this order:

```text
Sex,Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight,Rings
```

Download `abalone.data` from the [UCI Abalone dataset](https://archive.ics.uci.edu/dataset/1/abalone), retain the observation rows unchanged, and prepend the header above when saving it as `abalone.csv`. The notebook removes zero-height rows, splits the remaining data and fits preprocessing only on the training portion. `Rings` is the prediction target; it is not a direct age-in-years measurement.

The [small example](examples/quickstart.py) uses generated measurements and does not require this download. It demonstrates the baseline pattern rather than reproducing the dataset results in `results/reproduction.json`.

Nash, W., Sellers, T., Talbot, S., Cawthorn, A., & Ford, W. (1994). Abalone. UCI Machine Learning Repository. https://doi.org/10.24432/C55C7W. CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. Data preparation adds canonical CSV column names; the observation values are not modified.
