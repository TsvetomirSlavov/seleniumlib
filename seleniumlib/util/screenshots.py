import os


class Screenshots(object):

    PNG_FORMAT = ".png"

    def __init__(self, driver, dir_path, folder="", media_format=PNG_FORMAT):
        self.driver = driver
        self.dirPath = dir_path
        self._safe_set_folder('folder', folder)
        self.format = media_format

        if not os.path.isdir(self.dirPath):
            os.mkdir(self.dirPath)

    def _safe_set_folder(self, attribute, folder):
        if folder:
            if folder[-1] != "/" and folder[-1] != "\\":
                folder += "/"

            if not os.path.isdir(self.dirPath + folder):
                os.mkdir(self.dirPath + folder)

        setattr(self, attribute, folder)

    def set_folder(self, folder):
        self._safe_set_folder('folder', folder)

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(self.dirPath + self.folder + file_name + self.format)
