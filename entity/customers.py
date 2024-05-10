class customers:
    def _init_(self, customer_id,customer_name, email,customer_password):
        self.customer_id = customer_id
        self.customer_name =customer_name
        self.email = email
        self.customer_password =customer_password

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name


    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


    def get_customer_password(self):
        return self.customer_password

    def set_customer_password(self, customer_password):
        self.customer_password = customer_password
