class KeyNotFoundError(Exception):
    """
    Raised when the given key was not found in the language file.
    """

    def __init__(self, key, language, default_language=None):
        Exception.__init__(self,
                           f"The given key - {key} was not found in the {language}"
                           f"{f' and {default_language}' if default_language and default_language != language else ''} "
                           f"language")
