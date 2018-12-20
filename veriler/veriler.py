import os
import json


def xp_ekle(user, xp):
    userID = str(user.id)

    level={
        "yeniüye" : 200,
        "üye" : 400,
        "eskiüye" : 600
    }

    if os.path.isfile("./veriler/kullanicilar.json"):
        with open("./veriler/kullanicilar.json", 'r') as fp:
            data = json.load(fp)
        if userID in data:
            data[userID]['name']=user.name
            data[userID]['xp']+=xp
            for lvl in level:
                if xp < level[lvl]:
                    data[userID]['level']=lvl
                    break
            with open("./veriler/kullanicilar.json", 'w') as fp:
                json.dump(data, fp, indent=4)
        else:
            data[userID]={}
            data[userID]['name']=user.name
            data[userID]['xp'] = xp
            for lvl in level:
                if xp < level[lvl]:
                    data[userID]['level']=lvl
                    break
            with open("./veriler/kullanicilar.json", 'w') as fp:
                json.dump(data, fp, indent=4)

    else:
        data = {}
        data[userID]={}
        data[userID]['name']=user.name
        data[userID]['xp'] = xp
        for lvl in level:
            if xp < level[lvl]:
                data[userID]['level']=lvl
                break
        with open("./veriler/kullanicilar.json", 'w') as fp:
            json.dump(data, fp, indent=4)


def xp_getir(user):
    userID = str(user.id)
    if os.path.isfile("./veriler/kullanicilar.json"):
        with open("./veriler/kullanicilar.json", 'r') as fp:
            data = json.load(fp)

        return data[userID]['xp']

    else:
        return None


def level_getir(user):
    userID = str(user.id)
    if os.path.isfile("./veriler/kullanicilar.json"):
        with open("./veriler/kullanicilar.json", 'r') as fp:
            data = json.load(fp)

        return data[userID]['level']

    else:
        return None