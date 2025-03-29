# Test Discovery Rules:

# Understand how Pytest identifies test files and functions.
# File names: Must start with test_ or end with _test.py.
# Function names: Must start with test_.

# test_example.py
# Running all tests using pytest:

# Running specific tests:
# pytest test_example.py
# pytest test_example.py::test_function_name
#pytest -v

import pytest

def test_addition():
    result = 2 + 3
    assert result == 5  # Assert that the result is as expected.

def test_string_contains():
    string = "pytest is awesome"
    assert "awesome" in string  # Assert that "awesome" is in the string.

def test_list_length():
    items = [1, 2, 3, 4]
    assert len(items) == 4  # Assert that the list has 4 elements.

def add(a,b):
    return a + b

def test_add_val():
    result = add(4,5)
    print(result)
    assert result == 9

    
# Assertions
def test_assert():
    assert 2 + 2 == 4  # Check equality
    assert "pytest" in "pytest is great"  # Check containment
    assert len([1, 2, 3]) == 3  # Validate length


def mul(a,b):
    return a * b

def test_mul_val():
    result = mul(4,5)
    print(result)
    assert result == 20
   
    

# Markers for Categorization
import pytest
@pytest.mark.smoke
def test_one():
    a, b = 4, 5
    result = a + b
    assert result == 9

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_addition():
    result = 2 + 3
    assert result == 5

@pytest.mark.smoke
def test_subtraction():
    result = 10 - 5
    assert result == 5

@pytest.mark.regression
def test_multiplication():
    result = 2 * 3
    assert result == 6

@pytest.mark.regression
@pytest.mark.slow
def test_division():
    result = 10 / 2
    assert result == 5
    
# Built-in Markers:

# @pytest.mark.skip: Skip a test.
# @pytest.mark.skipif(condition, reason): Conditionally skip a test.
# @pytest.mark.xfail: Mark a test as expected to fail.






# Fixtures in Pytest
# Fixtures in Pytest are used to manage setup and teardown logic for test functions. They are a powerful way to provide test dependencies, pre-configure the testing environment, and clean up resources after a test completes.

# Key Features of Fixtures
# Dependency Injection: Fixtures can inject data or setup logic directly into test functions by passing them as arguments.
# Reusable Setup Logic: Fixtures eliminate redundancy by reusing setup code across multiple tests.
# Scope Control: Fixtures can be scoped to a test function, module, class, or session.
# Teardown Support: Fixtures can include cleanup logic after the test execution.

#Fixtures
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Pytest", "type": "framework"}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Pytest"
    assert sample_data["type"] == "framework"

# Key Point	Description
# Setup	Prepare resources or state for tests.
# Dependency Injection	Fixtures are injected based on argument names.
# Reusability	Use the same fixture across multiple tests.
# Scope	Controls how often a fixture is executed (function, module, etc.).
# Teardown	Clean up or restore resources after tests.
# Parameterization	Provide multiple sets of data for tests.
# Autouse Fixtures	Automatically apply fixtures to tests without explicit reference.
# Fixture Composition	Combine fixtures to build complex setups.