from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass
    
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass
    
    def get_sections(self):
        return self.sections
    
    def add_sctions(self, section):
        return self.sections.append(section)

class LinkedIn(Profile):
    def create_profile(self):
        self.add_sctions(PersonalSection())
        self.add_sctions(PatentSection())
        self.add_sctions(PublicationSection())
    
class Facebook(Profile):
    def create_profile(self):
        self.add_sctions(PersonalSection())
        self.add_sctions(AlbumSection())

if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create?  [LinkedIn or Facebook]  ")
    profile = eval(profile_type)()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())

'''
output:
Which Profile you'd like to create?  [LinkedIn or Facebook]  Facebook
Creating Profile.. Facebook
Profile has sections 
'''