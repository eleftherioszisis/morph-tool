import nose.tools as nt

import mock
from mock import patch

import morph_tool.loader as test_module


def test_ensure_startswith_point():
    nt.assert_equal(
        test_module._ensure_startswith_point(".ext"),
        ".ext"
    )
    nt.assert_equal(
        test_module._ensure_startswith_point("ext"),
        ".ext"
    )


@patch('morphio.Morphology')
def test_loader(f_mock):
    f_mock.configure_mock(side_effect=lambda *args: object())
    loader = test_module.MorphLoader('/dir', file_ext='abc', cache_size=1)
    morph1 = loader.get('test')
    # should get cached object now
    nt.assert_is(
        loader.get('test'),
        morph1
    )
    # options are different => should not get cached object
    nt.assert_is_not(
        loader.get('test', options=42),
        morph1
    )
    # first cached object was evicted from the cache
    nt.assert_is_not(
        loader.get('test'),
        morph1
    )
    f_mock.assert_has_calls([
        mock.call('/dir/test.abc'),
        mock.call('/dir/test.abc', 42),
        mock.call('/dir/test.abc'),
    ])