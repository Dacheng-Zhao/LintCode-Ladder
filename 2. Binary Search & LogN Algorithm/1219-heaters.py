# class Solution:
#     """
#     @param houses: positions of houses
#     @param heaters: positions of heaters
#     @return: the minimum radius standard of heaters
#     """
#     def findRadius(self, houses, heaters):
#         # Write your code here
#         # excceed time limit
#     #     if not houses:
#     #         return 0 
        
#     #     coverage = heaters[:]
#     #     radius = 0
#     #     increaseRadius = True
        
#     #     while increaseRadius:
#     #         if len(coverage) < len(houses):
#     #             radius += 1 
#     #             coverage = self.increase(coverage, heaters, radius)
#     #             continue
#     #         for i in range(len(houses)):
#     #             if houses[i] not in coverage:
#     #                 radius += 1 
#     #                 coverage = self.increase(coverage, heaters, radius)
#     #                 continue
#     #         increaseRadius = False
#     #     return radius
    
#     # def increase(self, coverage, heaters, radius):
#     #     for i in range(len(heaters)):
#     #         coverage.append(heaters[i] + radius)
#     #         if heaters[i] - radius > 0:
#     #             coverage.append(heaters[i] - radius)
#     #     return coverage
    
#         if not houses:
#             return 0
        
#         heaters.sort()
#         res = -sys.maxsize
#         for i in range(len(houses)):
#             res = max(res, self.findClosest(houses[i], heaters))
#         return res
        
#     def findClosest(self, singlehouse, heaters):
#         start = 0
#         end = len(heaters) - 1 
        
#         while start + 1 < end:
#             mid = start + (end - start) // 2 
#             if singlehouse > heaters[mid]:
#                 start = mid 
#             else:
#                 end = mid 
#         return min(abs(singlehouse - heaters[start]), abs(heaters[end] - singlehouse))
            
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
