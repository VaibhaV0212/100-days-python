# employee - id, name, city_id
# city - id, name

# select e.name, c.city
# from employee e
# join  city c
# on e.id = c.id


def test(str, chara):
    if len(str) > 0:
        for i in str:
            s = []
            if i == ' ':
                break
            else:
                s.append(i)
                print(s)
                if chara in s:
                    print('Found')
                else:
                    print('Not Found')


str = 'this is my car'
character = input('Enter the character= ')
test(str, character)
    
