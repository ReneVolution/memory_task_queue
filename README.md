[![Build Status](https://travis-ci.org/ReneVolution/memory_task_queue.svg?branch=master)](https://travis-ci.org/ReneVolution/memory_task_queue)
[![Coverage Status](https://coveralls.io/repos/github/ReneVolution/memory_task_queue/badge.svg?branch=master)](https://coveralls.io/github/ReneVolution/memory_task_queue?branch=master)
[![Say Thanks](https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg)](https://saythanks.io/to/ReneVolution)


# MemoryTaskQueue

A simple Task Queue with a retry mechanism.

## Example

```python
from memory_task_queue import MemoryTaskQueue

def my_callback(item):
    print(item)

def my_fallback(item):
    print('Callback failed to run')

mtq = MemoryTaskQueue(my_callback, on_max_retries=my_fallback, delay=0.3, max_retries=3)

mtq.put({'message': 'hello world'})

```
