class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # Заполняем поле логин
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        # Нажимаем кнопку логина
        wd.find_element_by_css_selector('input[type="submit"]').click()
        # Заполняем поле пароль
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        # Нажимаем кнопку логина
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('span[class="user-info"]').click()
        wd.find_element_by_css_selector('a[href="/mantisbt-2.24.1/mantisbt-2.24.1/logout_page.php"]').click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('span[class="user-info"]')) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        return self.get_logget_user() == username

    def get_logget_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector('ul.breadcrumb span').text
