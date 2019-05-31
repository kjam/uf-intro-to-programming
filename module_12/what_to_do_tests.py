import pytest
from datetime import datetime
from what_to_do import return_what_to_do

@pytest.mark.parametrize("time_now,output",[
    (datetime(2019, 1, 1, 0), "Go to bed!"),
    (datetime(2019, 1, 1, 1), "You should be asleep..."),
    (datetime(2019, 1, 1, 3), "You should be asleep..."),
    (datetime(2019, 1, 1, 8), "Why aren't you working??"),
    (datetime(2019, 1, 1, 17), "Relax!")])
def test_what_to_do(time_now, output):
    assert return_what_to_do(time_now) == output
