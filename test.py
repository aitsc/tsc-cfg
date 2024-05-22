from tsc_cfg import *
import cfg
from datetime import datetime
from typing import Any, Dict


def test_cfg():
    Cfg_ = Cfg
    
    class MyClass(Cfg_):
        static_var: bool = False

        class NestedClass(Cfg_, object):
            nested_var: datetime = datetime.now()

            class NestedClass(Cfg_):
                nested_var = 10*2

            class NestedClass2(Cfg_):
                nested_var: Any = '20'

        class Test(Cfg_):
            ...
        static_var1: Dict[str, Any] = {
            'a': {},
            'b': '2',
            'c': (3,),
        }

    x = MyClass._get_('NestedClass', t=MyClass.NestedClass).nested_var
    print(MyClass.model_dump_code(keep_class_newline=True))
    # print(Cfg_.model_dump_code())
    print(MyClass._len_)
    print()

    MyClass2 = MyClass.model_deepcopy('MyClass2')
    MyClass.static_var1['a'][1] = 100
    MyClass2.static_var1['a'][1] = 101
    print(MyClass.static_var1)
    print(MyClass2.static_var1)
    print()
    
    print(create_unduplicated_key('a', {'a'}))
    
    MyClass2.NestedClass._set_('nested_var2', [{'a': [1, 2]}, 1], create_new=True)
    MyClass2._set_(0, 1)
    MyClass2._insert_(123, 2)
    MyClass2._insert_([2, {'abc': {'test': 123}}, 4], 3, ['test', None, None])
    print(MyClass2.model_dump_code())
    print(MyClass._get_(1))
    print()
    
    MyClass._set_(None, [1, 2, 3])
    print(MyClass.model_dump_code())
    print(MyClass._get_('a1234', allow_default=True))
    
    print('---------meta test---------')
    # KEY_NOT_FOUND.use_raise = True
    print(MyClass.abcdefg, MyClass[-1])
    MyClass.abcdefg = MyClass['abcdefg'] = 1234
    print(MyClass['abcdefg'])
    print(MyClass['static_var1.a'])
    print(KEY_NOT_FOUND.abc.asd)


def test_cfg_utils():
    cfg_handler = ReloadCfgHandler(cfg).add_yaml(
        'cfg.yaml',
        'cfg2.yaml'
    )
    print(cfg_handler.yaml_paths)
    cfg_handler.del_yaml('cfg.yaml')
    
    while True:
        print(cfg.test.model_dump_code())
        print(cfg.test2.model_dump_code())
        input('Press Enter to print cfg...\n')

if __name__ == '__main__':
    # test_cfg()
    test_cfg_utils()
