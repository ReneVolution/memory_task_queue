from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from mock import Mock

from memory_task_queue import MemoryTaskQueue


class TestMemoryTaskQueue(object):

    def setup_method(self, test_method):
        pass

    def teardown_method(self, test_method):
        pass

    def test_init_memory_task_queue(self):

        def cb(item):
            pass

        mtq = MemoryTaskQueue(cb)
        assert isinstance(mtq, MemoryTaskQueue)

    def test_called_with_string(self):
        cb = Mock()

        mtq = MemoryTaskQueue(cb)
        mtq.put('some_string')
        mtq.wait()

        cb.assert_called_once_with('some_string')

    def test_max_retries(self):

        cb = Mock()
        cb.side_effect = Exception()

        mtq = MemoryTaskQueue(cb, max_retries=3)

        mtq.put('hello')
        mtq.wait()

        assert cb.call_count == 4

    def test_on_max_retries(self):
        cb = Mock()
        cb.side_effect = Exception()

        fb = Mock()

        mtq = MemoryTaskQueue(cb, on_max_retries=fb, max_retries=3)

        mtq.put('hello')
        mtq.wait()

        fb.assert_called_once_with('hello')
