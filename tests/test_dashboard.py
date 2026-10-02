from release.dashboard import report, load

def test_release_is_go():
    assert report(load())["decision"]=="GO"
