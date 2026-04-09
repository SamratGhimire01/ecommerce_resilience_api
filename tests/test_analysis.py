from src.analysis import (
    load_data,
    get_content_type_distribution,
    get_top_countries,
    get_yearly_trend,
    get_rating_distribution,
    get_duration_stats
)

data = load_data()

def test_content_distribution():
    result = get_content_type_distribution(data)
    assert isinstance(result, dict)
    assert "Movies" in result
    assert "TV Shows" in result

def test_top_countries():
    result = get_top_countries(data)
    assert isinstance(result, dict)
    assert len(result) <= 10

def test_yearly_trend():
    result = get_yearly_trend(data)
    assert isinstance(result, dict)
    assert all(isinstance(k, int) for k in result.keys())

def test_rating_distribution():
    result = get_rating_distribution(data)
    assert isinstance(result, dict)

def test_duration_stats():
    result = get_duration_stats(data)
    assert "average_duration_minutes" in result
    assert "average_seasons" in result