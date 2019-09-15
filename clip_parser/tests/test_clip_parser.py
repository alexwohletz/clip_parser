import pytest
from clip_parser.clip_parser import parse_ranges,grab_codes,kill_program

def test_parse_ranges():
    txt = '99281-99282'
    assert parse_ranges(txt) == \
        '''(\n'99281',\n'99282',\n)'''
    txt_2 = 'L1234-L1235'
    assert parse_ranges(txt_2) == \
        '''(\n'L1234',\n'L1235',\n)'''
    txt_3 = '0345T-0347T'
    assert parse_ranges(txt_3) == \
        '''(\n'0345T',\n'0346T',\n'0347T',\n)'''
    txt_4 = 'somethin not a range'
    assert parse_ranges(txt_4) == '(\n)'

def test_grab_codes():
    txt = '''there is a random set of codes 
    in this block of text 97812
    and we don't know what is inside!
    A1534'''
    assert grab_codes(txt) == ['97812','A1534']

    txt_2 = 'blah'

    assert grab_codes(txt_2) == []


def test_kill_program():
    with pytest.raises(SystemExit):
        kill_program()