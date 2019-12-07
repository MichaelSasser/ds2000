import pytest
from oscilloscope import DS2000


def test_blocking_io_error():
    with pytest.raises(BlockingIOError):
        dev: DS2000 = DS2000("192.0.2.1")
        dev.connect()

def test_connection_refused():
    with pytest.raises(ConnectionRefusedError):
        dev: DS2000 = DS2000("127.0.0.1")
        dev.connect()
