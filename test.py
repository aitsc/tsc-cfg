from tsc_cfg import *
import cfg


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
    test_cfg_utils()
