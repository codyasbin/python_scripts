class Codyasbin:
    def __init__(self):
        self.name = "Asbin Magar"
        self.version = "0.1.0"
        self.author = "Asbin Magar"
        self.description = "Codyasbin is a Python library that provides a simple interface to interact with the Codyasbin API."
        self.github_url = "https://github.com/codyasbin"

    def get_info(self):
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
            "github_url": self.github_url
        }

    def help(self):
        return """
        Codyasbin Library Help:
        
        Methods:
        - get_info(): Returns information about the library.
        - help(): Displays this help message.
        
        Usage:
        1. Create an instance of the Codyasbin class.
        2. Call the desired methods to interact with the library.
        
        Example:
        >>> cody = Codyasbin()
        >>> info = cody.get_info()
        >>> print(info)
        """

    