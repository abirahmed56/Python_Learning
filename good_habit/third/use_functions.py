def is_adult(age: int, has_id:bool)->bool:
      return age >= 21 and has_id

def is_bob(name:str)->bool:
      return name.lower() == 'bob'

def enter_club(name: str, age: int, has_id:bool)->None:
    # if name.lower() == 'bob':
    #     print('Get out of here, we don\'t want trouble.')
    
    # if age >= 21 and has_id:
    #     print('You may enter the club')
    # else:
    #     print('You are not allowed')

    # Use function instead of conditions
    if is_bob(name):          
        print('Get out of here, we don\'t want trouble.')

    if is_adult(age, has_id):
        print('You may enter the club')
    else:
        print('You are not allowed')

def main()->None:
        enter_club(name='bob', age=29, has_id=True)
        enter_club(name='Abir', age=25, has_id=True)
        enter_club(name='Apon', age=12, has_id=False)
        enter_club(name='Abit', age=25, has_id=False)

if __name__ == '__main__':
        main()