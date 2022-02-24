"""Unit tests for bank.py"""

from todo_app.item import Item
import pytest
from todo_app.view_model import ViewModel


def test_get_ToDo_Trello():
    viewModel = ViewModel(items=[Item( "60afa040b07e9a4371098530","title", "To Do")])
    list= viewModel.todo_items
    assert len(list)==1

def test_get_Doing_Trello():
    viewModel = ViewModel(items=[Item("60bf89d905749b885a39b6ec","title","Doing")])
    list= viewModel.doing_items
    assert len(list)==1
    
def test_get_Done_Trello():
    viewModel = ViewModel(items=[Item("60b7fe3a74f9c35594741e71","title","Done")])
    list= viewModel.done_items
    assert len(list)==1
