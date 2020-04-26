from .BookletHelper import BookletHelper

helper = BookletHelper()
assert helper.setpages(8).booklet_pages() == [8, 1, 2, 7, 6, 3, 4, 5], "Wrong output for pages = 8"
assert helper.setpages(14).booklet_pages() == [None, 1, 2, None, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9], "Wrong output for pages = 14"