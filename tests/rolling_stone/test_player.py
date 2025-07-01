from geo_calculator.rolling_stone.player import Player
import pytest

@pytest.fixture
def new_player():
    return Player()

def test_player(new_player):
    player = Player()
    assert isinstance(new_player, Player)

def test_player_receive_score():
    # Arrange
    player = Player()
    RECEIVED_SCORE = 10
    assert player.score == 0
    # Act
    player.receive_score(RECEIVED_SCORE)
    # Assert
    assert player.score == RECEIVED_SCORE

    # Act again
    player.receive_score(RECEIVED_SCORE)
    # Assert again
    assert player.score == 2 * RECEIVED_SCORE

def test_player(new_player):
    assert isinstance(new_player, Player)
    assert new_player.score == 0


def test_input_name_for_player(mocker, new_player):
    # Arrange
    TEST_NAME = "Ola Nordmann"
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=TEST_NAME
    )
    assert new_player.name is None

    # Act
    new_player.prompt_for_name()

    # Assert
    assert new_player.name == TEST_NAME