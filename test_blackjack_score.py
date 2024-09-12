from main import blackjack_score
import pytest

def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  expected_result = 7
  # Act
  score = blackjack_score(hand)
  # Assert <-- Write assert statement herede
  assert score == expected_result

def test_facecards_have_values_calculated_correctly():
  # Arrange
  hand = [3, 4, "King"]
  expected_result = 17
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  # Arrange
  hand = [3, 4, 'Ace']
  expected_result = 18
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_calculates_aces_as_1_where_11_would_bust():
  # Arrange
  hand = ['Ace', 3, 4, 'King']
  expected_result = 18
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_returns_invalid_for_invalid_cards():
  # Arrange
  hand = ['Ace', 3, 4, 'Joker']
  expected_result = "Invalid"
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_returns_invalid_for_list_length_greater_than_5():
    # Arrange
  hand = ['Ace', 2, 3, 2, 2, 2]
  expected_result = "Invalid"
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_returns_bust_for_scores_over_21():
    # Arrange
  hand = ['Ace', 'King', 'Queen', 'Jack']
  expected_result = "Bust"
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

def test_returns_12_for_ace_ace_king():
  #Arrange
  hand = ['Ace', 'Ace', 'King']
  expected_result = 12
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result

@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  #Arrange
  hand = ['Ace', 'Ace', 'Ace', 'Ace']
  expected_result = 14
  #ACT
  score = blackjack_score(hand)
  #Assert
  assert score == expected_result