"""Unit tests for bank.py"""

import pytest
from todo_app.app import get_ToDo_Trello, get_Doing_Trello, get_Done_Trello


def test_get_ToDo_Trello():
    list = get_ToDo_Trello(trelloList=[{"idList": "60af9248e87283184d346aa9", "id": "60afa040b07e9a4371098530","name":"ToDo"}])
    assert len(list)==1

def test_get_Doing_Trello():
    list = get_Doing_Trello(trelloList=[{"idList": "60af9248e87283184d346aaa", "id": "60bf89d905749b885a39b6ec","name":"Doing"}])
    assert len(list)==1
    
def test_get_Done_Trello():
    list1 = get_Done_Trello(trelloList=[{"idList": "60af9248e87283184d346aab", "id": "60b7fe3a74f9c35594741e71","name":"Done"}])
    assert len(list)==1
