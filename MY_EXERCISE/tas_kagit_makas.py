user1 = input("Kullanıcı 1:")
user2 = input("Kullanıcı 2:")
user1_answer = input("%s, Kağıt, Taş, Makas?" % user1)
user2_answer = input("%s, Kağıt, Taş, Makas?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("Berabere")
    elif u1 == 'taş':
        if u2 == 'makas':
            return("Taş kazandı!")
        else:
            return("Kağıt kazandı")
    elif u1 == 'makas':
        if u2 == 'kağıt':
            return("Makas kazandı!")
        else:
            return("Taş kazandı")
    elif u1 == 'kağıt':
        if u2 == 'taş':
            return("Kağıt kazandı!")
        else:
            return("Makas kazandı")

print(compare(user1_answer, user2_answer))