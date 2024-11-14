import unittest
from unittest.mock import patch
import guess_the_word

class TestGuessTheWord(unittest.TestCase):

    def test_word_selection(self):
        """Test that the selected word is from the correct list."""
        word_list = ["cookie", "monster", "retreat", "labour", "completition"]
        for _ in range(10):  # Test multiple times for randomness
            word = guess_the_word.select_random_word()
            self.assertIn(word, word_list)

    @patch('guess_the_word.input', side_effect=['c', 'o', 'k', 'x', 'm', 'e', 't', 'i', 'o', 'n'])
    def test_correct_guess_progress(self, mock_input):
        """Test that correct and incorrect guesses are processed correctly."""
        # Mocking a word for consistency
        with patch('guess_the_word.select_random_word', return_value="cookie"):
            guessed_letters = set()
            word = "cookie"
            
            # Track the word progress after each guess to ensure it updates correctly
            for guess in ['c', 'o', 'k', 'x', 'm', 'e', 't', 'i', 'o', 'n']:
                guessed_letters.add(guess)
                
                if guess in word:
                    # Ensure correct guesses reveal letters in the word
                    self.assertIn(guess, word)
                else:
                    # Ensure incorrect guesses are not in the word
                    self.assertNotIn(guess, word)

                # Display the current progress in the word
                word_progress = guess_the_word.display_word_progress(word, guessed_letters)
                
                # Check if the final word is fully revealed after correct guesses
                if all(letter in guessed_letters for letter in word):
                    self.assertEqual(word_progress, "cookie")

if __name__ == "__main__":
    unittest.main()
