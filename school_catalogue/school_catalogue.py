class School:
  # constructor for school class
  def __init__(self,name,level,numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents

  #getter for school name
  def get_name(self):
    return self._name

  #getter for school level
  def get_level(self):
    return self._level

  #getter for school number of students
  def get_numberOfStudents(self):
    return self._numberOfStudents

  #setter for school numberOfStudents
  def set_numberOfStudents(self,new_number):
    self._numberOfStudents = new_number

  #repr method for school
  def __repr__(self):
    return "A {} school name {} with {} students".format(self._level,self._name,self._numberOfStudents)


#testing school class
s1 = School('Orange and Blue','Primary',5)
s1
print(s1.get_name())
print(s1.get_level())
s1.set_numberOfStudents(78)
print(s1.get_numberOfStudents())

class PrimarySchool(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,'Primary',numberOfStudents)
    self._pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self._pickupPolicy

  def __repr__(self):
     parentRepr= super().__repr__()
     return parentRepr + ". The pickup policy is {}".format(self._pickupPolicy)
    
print('\n')
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())
print(b)


#Create the highschool class
class highSchool(School):
  def __init__(self,name,numberOfStudents,sportsTeam):
    super().__init__(name,'High School',numberOfStudents)
    self._sportsTeam = sportsTeam

  def get_sportsTeam(self):
    return [x for x in self._sportsTeam]

  def __repr__(self):
    return "List of sport teams in {}".format(self._name)

print('\n')
c = highSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sportsTeam())
print(c)