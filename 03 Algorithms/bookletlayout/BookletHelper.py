class BookletHelper:
    """
    Constructs BookletHelper with the number of pages in a document.
    Number of pages defaults to 0.
    """
    def __init__(self, pages = 0):
        self.pages = pages

    """
    Changes the number of pages in a document. 
    Returns the current instance of BookletHelper.
    """
    def setPages(self, pages: int):
        self.pages = pages
        return self

    """
    Arranges the pages of a document for printing in booklet form, as provided by the constructor or by self.setpages().
    Returns a List[int] of the pages in said printing order.
    """
    def booklet_pages(self):
        new_list = []
        if self.pages == 0 or self.pages == 1:
            return [self.pages]
        else:
            psum = self.pages + 1 + self.pages % 4  # insert padding
            r = range(1, self.pages + 1)
            for i in r:
                if len(new_list) < self.pages:  # break out of loop if there is enough elements in new_list
                    first = i
                    if psum - first <= self.pages:  # ergo if psum-first is an element of r
                        second = psum - first
                    else:
                        second = None
                    ext = [first, second] if i % 2 == 0 else [second, first]  # reverse insertion order based on parity
                    new_list.extend(ext)
                else:
                    break
        return new_list
