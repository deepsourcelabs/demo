from demo_code import RandomNumberGenerator


def test_random_number_generator():
    """Test random number generator."""
    assert RandomNumberGenerator().get_number()
