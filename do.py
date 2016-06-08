age = 18


def do(do_this, if_true, do_that):
    if if_true:
        do_this()
    else:
        do_that()


do(lambda: print("you are legal age!"), (age >= 18), lambda: print("you are not legal age!"))
