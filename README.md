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

### Start notebook on WSL2

On WSL2 remember to add (dynamic) ip address to the start command

    jupyter lab --ip $(hostname -I)
    
And access the IP address, port and token combination given on the command window.

     http://192.168.222.17:8888/?token=d7b4e6828f99ed013f914fdbb04a2833ffc6733afc25abaf
