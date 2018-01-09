from stats import generate_ability_scores


def test_classic_ability_gen(capsys):
    scores = generate_ability_scores('classic')
    out, err = capsys.readouterr()
    assert len(scores) == 6
    assert 'Generating ability scores using the classic method.' in out
    assert 'Rolling three six-sided die...' in out
    assert max(scores) <= 18
    assert min(scores) >= 3


def test_default_ability_gen(capsys):
    scores = generate_ability_scores()
    out, err = capsys.readouterr()
    assert len(scores) == 6
    assert 'Generating ability scores using the standard method.' in out
    assert 'Rolling four six-sided die...' in out
    assert 'Dropping the lowest value...' in out
    assert max(scores) <= 18
    assert min(scores) >= 4


def test_heroic_ability_gen(capsys):
    scores = generate_ability_scores('heroic')
    out, err = capsys.readouterr()
    assert len(scores) == 6
    assert 'Generating ability scores using the heroic method.' in out
    assert 'Rolling two six-sided die...' in out
    assert 'Adding six to the sum...' in out
    assert max(scores) <= 18
    assert min(scores) >= 7


def test_standard_ability_gen(capsys):
    scores = generate_ability_scores('standard')
    out, err = capsys.readouterr()
    assert len(scores) == 6
    assert 'Generating ability scores using the standard method.' in out
    assert 'Rolling four six-sided die...' in out
    assert 'Dropping the lowest value...' in out
    assert max(scores) <= 18
    assert min(scores) >= 4
