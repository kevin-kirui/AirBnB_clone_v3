import unittest
from models import storage
from models.state import State

class TestFileStorageGetCountMethods(unittest.TestCase):
    def test_get(self):
        """Test the get() method."""
        # Create a new State object and add it to storage
        new_state = State(name="Test State")
        storage.new(new_state)
        storage.save()

        # Retrieve the State object using get()
        retrieved_state = storage.get(State, new_state.id)

        # Assert that the retrieved object is the same as the created object
        self.assertEqual(retrieved_state, new_state)

    def test_count(self):
        """Test the count() method."""
        # Get the initial count of all objects
        initial_count = storage.count()

        # Create a new State object and add it to storage
        new_state = State(name="Test State")
        storage.new(new_state)
        storage.save()

        # Check the count of all objects after adding a new State object
        updated_count = storage.count()
        self.assertEqual(updated_count, initial_count + 1)

        # Check the count of State objects specifically
        state_count = storage.count(State)
        self.assertEqual(state_count, 1)

if __name__ == '__main__':
    unittest.main()
