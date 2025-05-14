import pytest
import pandas as pd
from src.utils.helpers import perform_calculations

def test_perform_calculations():
    # Create sample dataframes for testing
    df1 = pd.DataFrame({
        'common_column': [1, 2, 3],
        'value1': [10, 20, 30]
    })
    
    df2 = pd.DataFrame({
        'common_column': [1, 2, 4],
        'value2': [100, 200, 400]
    })
    
    result = perform_calculations(df1, df2)
    
    assert result is not None
    assert len(result) == 2  # Only matching rows should be returned