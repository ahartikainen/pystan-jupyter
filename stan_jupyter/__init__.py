"""Run PyStan calls in a thread."""
import multiprocessing

multiprocessing.set_start_method("spawn", True)

from importlib import reload
import stan as _stan

# force reload
_stan = reload(_stan)

from concurrent.futures import ThreadPoolExecutor as _ThreadPoolExecutor


def _exec_async(func, *args, **kwargs):
    """Execute an async function in a thread."""
    with _ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
    return future.result()


# Inject posterior.sample with a wrapped function.
def _inject_posterior(posterior):
    """Inject posterior.sample with call in thread."""
    posterior._sample = posterior.sample

    def sample(**kwargs):
        """"""
        return _exec_async(posterior._sample, **kwargs)

    # Update sample function docstring with posterior.sample docstring.
    sample.__doc__ += posterior.sample.__doc__
    posterior.sample = sample


# Wrap stan.build function.
def build(program_code, data=None, random_seed=None):
    """"""
    posterior = _exec_async(
        _stan.build, program_code, data=data, random_seed=random_seed
    )
    _inject_posterior(posterior)
    return posterior


# Update build function docstring with stan.build docstring.
build.__doc__ += _stan.build.__doc__

try:
    __version__ = _stan.__version__
except:
    pass

del reload, multiprocessing
