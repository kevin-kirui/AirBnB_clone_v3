#!/usr/bin/python3
"""Test cases for DBStorage class."""

import unittest
from models import storage
from models.state import State


class TestDBStorage(unittest.TestCase):
    """Test cases for the DBStorage class."""

    def test_get(self):
        """Test the get() method."""
        new_state = State(name="Test State")
        storage.new(new_state)
        storage.save()
        retrieved_state = storage.get(State, new_state.id)
        self.assertEqual(retrieved_state, new_state)

    def test_count(self):
        """Test the count() method."""
        initial_count = storage.count()
        new_state = State(name="Test State")
