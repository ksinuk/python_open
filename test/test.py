#-------------------------------------------------------
# print("""
# a
# b
# c\
# d""")
# print("\
# a\
# b\
# c\
# d")
# even_cubic_list=[x**3 for x in range(1,11) if x%2 == 0]
# even_cubic_dict = {x:x**3 for x in range(1,11) if x%2==0}
# print(even_cubic_list)
# print(even_cubic_dict)

#---------------------------------------------------------------
# def sign_up(username, password, password_confirmation):
#     if password == password_confirmation :
#         print("회원가입 되었습니다.")
#     else :
#         print("비밀번호를 다시 입력하세요")


# # 사용자 정보를 dictionary로 만들어 넘겨보세요.
# sign_up('kin','111','1111')
# my_account = {'password_confirmation':'1234','username':'kang', 'password':'1234'}
# sign_up(**my_account)


# -------------------------------------------
# class Person:
#     name ='kang'
#     def greeting(self):
#         print(f'hello {self.name}')
#     # str : 사용자를 위한 것 print()에서 호출
#     def __str__(self):
#         return f'name : {self.name}'
#     # repr : idle, jupyter,python
#     # str이 업스면 repr 호출
#     # repr없어도 str 호출 안함
#     def __repr__(self):
#         return f'name\n : {self.name}'

# kang = Person()
# print(kang)

#-------------------------------------------------
# class p:
#     name = 'ksinuk'
#     score = 0
#     def __init__(self,age):
#         self.age = age
#         p.score += 1
#     def print(self):
#         print(f'name : {self.name} , age : {self.age})
#     @staticmethod
#     def print_Static():
#         print(f"static name : {p.name} score : {p.score}")
#     @classmethod
#     def print_class(cls):
#         print(f"static name : {cls.name} score : {cls.score}")

# k =p(5)
# k.print()
# k.name = 'fake'
# k.print()
# k.print_Static()
# k.print_class()
# p.print_Static()
# p.print_class()
# print("--------------------------")
# a = k
# a.name = 'star'
# a.print()
# k.print()
# print("--------------------------")
# p.name='p trun'
# p.print_class()
# a.print_class()
# a.print()
# print("--------------------------")
# l =p(3)
# l.print_class()
# p.print(l)

#-----------------------------------------------------------------

def func():
    # global out_1
    # out_1='2'
    print(out_1)
    return 0
out_1='out1'
func()
print(out_1)