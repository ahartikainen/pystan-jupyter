## pystan-jupyter
Enable PyStan3 use on Jupyter Notebook/Lab.

https://pypi.org/project/pystan-jupyter/

### Install

    pip install pystan-jupyter


### Usage

At the start of the Notebook

```ipython
import stan_jupyter as stan

...
posterior = stan.build(program_code)
fit = posterior.sample(num_chains=4)
```
