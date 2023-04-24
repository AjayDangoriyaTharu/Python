class student:
    def __hello__(self,name):
        self.name=name
        class student1(student):
            def __hello__(self, name):
                return super().hello(name)
                s= student("Ajay")
                print(s.name)
