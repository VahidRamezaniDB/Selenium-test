from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://www.downloadha.com/")
        self.assert_title("دانلود ها - دانلود رایگان نرم افزار،بازی،فیلم و سریال")