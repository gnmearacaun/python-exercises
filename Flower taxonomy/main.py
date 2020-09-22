iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    dict_ = {id_n, species, petal_length, petal_width}
    for key, value in dict_:
        dict_.update(kwargs)
    iris.update({id_n: dict_})
#        dict_[id_n][key] = value
#    iris[id_n] = dict_


add_iris(id_n=0, species='Iris versicolor', petal_length=.0, petal_width=.3, petal_hue='pale lilac')
print(iris)
    # if kwargs is not None:
            # dict_.get([id_n][key] = value)
            # dict_.update({key: value})
    # return dict_
# eg. humans = {"Laura": {"next appointment": "Tuesday"},
#              "Robin": {"next appointment": "Friday"}}
