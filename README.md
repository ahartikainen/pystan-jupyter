Note: Not recommended approach and is currently broken

## pystan-jupyter
Enable PyStan3 use on Jupyter Notebook/Lab.

Module calls ```nest-asyncio```:

```python
import nest_asyncio
nest_asyncio.apply()
del nest_asyncio
```

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

On WSL2 remember to add (dynamic) IP address to the start command

    jupyter lab --ip $(hostname -I)
    
Users with multiple IP addresses

    jupyter lab --ip $(echo $(hostname -I) | rev | cut -d " " -f1 | rev)
    
And access the IP address, port and token combination given on the command window.

     http://192.168.222.17:8888/?token=<token-code-here>
