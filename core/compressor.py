from compressor.filters.css_default import CssAbsoluteFilter

class NonSuffixCSSAbsoluteFilter(CssAbsoluteFilter):

    def add_suffix(self, url):
        """ Prevent adding suffix to be able to preload certain resources """
        return url
