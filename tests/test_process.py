import src.process
import pandas as pd


def add(x, y):
    return x + y


def test_add():
    # Arrange
    x = 2
    y = 3

    expected = 5
    # Act
    output = add(x, y)

    # Assert
    assert output == expected


def test_aggregate_data():
    # Arrange
    merged_data = pd.DataFrame(
        {"product_id": [1, 1, 2, 2], "quantity": [10, 20, 30, 40]}
    )

    expected = pd.DataFrame({"product_id": [1, 2], "total_quantity": [30, 70]})

    # Act
    output = src.process.aggregate_data(merged_data)

    # Assert
    pd.testing.assert_frame_equal(output, expected)
