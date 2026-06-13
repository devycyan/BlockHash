# test_blockhash.py
"""
Tests for BlockHash module.
"""

import unittest
from blockhash import BlockHash

class TestBlockHash(unittest.TestCase):
    """Test cases for BlockHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockHash()
        self.assertIsInstance(instance, BlockHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
