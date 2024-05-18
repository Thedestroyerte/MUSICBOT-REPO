# Power By @Zero_Nxz & @Professor7x 
# Join https://t.me/+BWruaT7T_iE5ZGJl For More Update
# Join @Zero_Nxz For Hack
# Join Our Chats https://t.me/+BWruaT7T_iE5ZGJl & @Zero_Nxz

import glob
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]



# Power By @Zero_Nxz & @Professor7x 
# Join https://t.me/+BWruaT7T_iE5ZGJl For More Update
# Join @Zero_Nxz For Hack
# Join Our Chats https://t.me/+BWruaT7T_iE5ZGJl & @Zero_Nxz