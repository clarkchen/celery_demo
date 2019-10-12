def mock_delay(self, *args, **kwargs):
    self._apply_immediately = lambda *args, **kwargs: True
    return self.apply(args, kwargs)
