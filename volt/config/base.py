# Volt default configurations file

from os.path import join


class Config(dict):
    """Container class for storing configuration options.
    """
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        # set __dict__ to the dict contents itself
        # enables value access by dot notation
        self.__dict__ = self

class DefaultConfig(Config):
    """Container class for default configuration options.
    """
    def merge(self, conf_obj):
        for key in conf_obj.keys():
            if key in self:
                self[key] = conf_obj[key]


# Volt configurations
# Changing values in this Config is allowed but not recommended
VOLT = DefaultConfig(

    # User config file name
    # Used to determine project root
    USER_CONF = "voltconf.py",

    # Directory paths for content files, templates, and generated site
    # relative to a project root
    CONTENT_DIR = "content",
    TEMPLATE_DIR = "templates",
    SITE_DIR = "site",
)


# Default site configurations
SITE = DefaultConfig(

    # Site name, URL, and description
    TITLE = "My Volt Site",
    URL = "http://127.0.0.1",
    DESC = "",

    # Engines used in generating the site
    # Defaults to none
    ENGINES = [],

    # Date and time format used in site content headers
    # Used for parsing the headers
    # Default is e.g. "2004-03-13 22:10"
    CONTENT_DATETIME_FORMAT = "%Y-%m-%d %H:%M",
    # Date and time format displayed on the generated site
    # Default is e.g. "Saturday, 13 March 2004"
    DISPLAY_DATETIME_FORMAT = "%A, %d %B %Y",
)


# Default configurations for the blog engine
BLOG = DefaultConfig(

    # URL for all blog content relative to root URL
    URL = "blog",

    # Blog post permalink, relative to blog URL
    PERMALINK = "{%Y}/{%m}/{%d}/{slug}",

    # Blog posts author, can be overwritten in individual blog posts
    AUTHOR = "",

    # The number of displayed posts per pagination page
    POSTS_PER_PAGE = 10,

    # Default length (in words) of blog post excerpts
    EXCERPT_LENGTH = 50,

    # Directory path for storing blog content relative to a project root
    CONTENT_DIR = join(VOLT.CONTENT_DIR, "blog"),

    # File paths of blog template files relative to a project root
    SINGLE_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, "post.html"),
    MULTIPlE_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, "pagination.html"),

    # TODO
    # Sort order for paginated posts display
    # Valid options are 'date', 'title', 'category', 'author'
    # Default order is A-Z (for alphabets) and present-past (for dates)
    # To reverse order just add '-' in front, e.g. '-date'
    SORT = ('date', 'title', 'category', 'author', ),

    # Required properties
    # These properties must be defined in each individual blog post header
    REQUIRED = ('title', 'time', ),
)


# Default configurations for the page engine
PAGE = DefaultConfig(

    # URL for all page content relative to root URL
    URL = "page",

    # Page permalink, relative to page URL
    PERMALINK = "{slug}",

    # Directory path for storing page content relative to a project root
    CONTENT_DIR = join(VOLT.CONTENT_DIR, "page"),

    # File paths of page template files relative to a project root
    TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, "page.html"),

    # Required properties
    # These properties must be defined in each individual page item header
    REQUIRED = ('title', ),
)


# Default configurations for the collection engine
COLLECTION = DefaultConfig(

    # URL for all collection content relative to root URL
    URL = "collection",

    # Collection permalink, relative to collection URL
    PERMALINK = "{slug}",

    # Directory path for storing collection content relative to a project root
    CONTENT_DIR = join(VOLT.CONTENT_DIR, "collection"),

    # File paths of collection template files relative to a project root
    SINGLE_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, "single.html"),
    MULTIPLE_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, "multiple.html"),

    # Required properties
    # These properties must be defined for each collection item individually
    REQUIRED = ('title', 'item', ),
)
