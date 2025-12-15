"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException
import random

""" random is used to kill mutants that modify the values of either a or b"""


@pytest.fixture
def calc():
    return Calculator()


def test_valid_input_raises_Invalid_Value_Error_with_correct_message1(calc):
    # Arrange
    expected_partial_message = f"Invalid values : a and b must be between {calc.MIN_VALUE} and  {calc.MAX_VALUE}"
    invalid_input = calc.MAX_VALUE + 1

    # Act
    with pytest.raises(InvalidInputException) as excinfo:
        calc.add(invalid_input, 2)

    # Assert
    assert expected_partial_message in str(excinfo.value)


def test_valid_input_raises_Type_Error_with_correct_message(calc):
    # Arrange
    expected_partial_message = "Give two values a and b"

    # Act
    with pytest.raises(TypeError) as excinfo:
        calc._validate_input(1)

    # Assert
    assert expected_partial_message in str(excinfo.value)


def test_valid_input_raises_Value_Error_with_correct_message2(calc):
    # Arrange
    expected_partial_message = "Cannot divide by zero"
    a = random.randint(1, calc.MAX_VALUE)

    # Act
    with pytest.raises(ValueError) as excinfo:
        calc.divide(a, 0)

    # Assert
    assert expected_partial_message in str(excinfo.value)


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange

        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(calc.MIN_VALUE, 0)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange

        a = random.randint(calc.MIN_VALUE, 0)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange

        a = random.randint(0, calc.MAX_VALUE)
        b = 0
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange

        a = 0
        b = random.randint(0, calc.MAX_VALUE)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange

        a = random.uniform(calc.MIN_VALUE, calc.MAX_VALUE)
        b = random.uniform(calc.MIN_VALUE, calc.MAX_VALUE)
        expected = a + b

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # TODO: Implement
        # Arrange

        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a - b

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # TODO: Implement
        # Arrange

        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a * b

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # TODO: Implement
        # Arrange

        a = random.randint(0, calc.MAX_VALUE)
        b = random.randint(0, calc.MAX_VALUE)
        expected = a / b

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)
