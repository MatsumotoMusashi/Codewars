def get_root_property(dict_,value):
    while True:
        new_dict_={}
        for key1 in dict_:
            if type(dict_[key1])==dict:
                for key2 in dict_[key1]:
                    new_dict_[f"{key1}/{key2}"]=dict_[key1][key2]
            else:
                if value in dict_[key1]:
                    return key1.split("/")[0]
                new_dict_[key1]=dict_[key1]
        if dict_==new_dict_:
            break
        dict_=new_dict_