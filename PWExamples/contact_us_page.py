class ContactUsPage:
    def __init__(self, page):
        self.page = page
        
    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")
        
    def test_submite_form(self, name, address, email, phone, subj, message):
        self.page.fill("[placeholder=\"Enter your name\"]", name)
        self.page.fill("[placeholder=\"Enter your address\"]", address)
        self.page.fill("[placeholder=\"Enter your email\"]", email)
        self.page.fill("[placeholder=\"Enter your phone number\"]", phone)
        self.page.fill("[placeholder=\"Type the subject\"]", subj)
        self.page.fill("textarea", message)
        
       #self.page.press()
    