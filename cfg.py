from tsc_cfg import Cfg


class test(Cfg):
    a: int = 1
    class test(Cfg):
        a = (1,)


class test2(Cfg):
    b = 2
