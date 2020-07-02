# -*- coding:utf-8 -*-
"""
test import_databases
"""
import os
import shutil
import unittest
from configparser import ConfigParser
from packageship import system_config

try:

    system_config.SYS_CONFIG_PATH = os.path.join(os.path.dirname(system_config.BASE_PATH),
                                                 'test',
                                                 'common_files',
                                                 'package.ini')

    system_config.DATABASE_FILE_INFO = os.path.join(os.path.dirname(system_config.BASE_PATH),
                                                    'test',
                                                    'init_system_files',
                                                    'database_file_info.yaml')

    system_config.DATABASE_FOLDER_PATH = os.path.join(os.path.dirname(system_config.BASE_PATH),
                                                      'test',
                                                      'init_system_files',
                                                      'dbs')

    from test.base_code.init_config_path import init_config

except Exception:
    raise
import warnings
import yaml

from packageship.application.initsystem.data_import import InitDataBase
from packageship.libs.exception import ContentNoneException, DatabaseRepeatException
from packageship.libs.configutils.readconfig import ReadConfig


class ImportData(unittest.TestCase):
    """
    test importdatabases
    """

    def setUp(self):

        warnings.filterwarnings("ignore")

    def test_empty_param(self):

        # If init is not obtained_ conf_ Path parameter
        try:
            InitDataBase(config_file_path=None).init_data()
        except Exception as e:
            self.assertEqual(
                e.__class__,
                ContentNoneException,
                msg="No init in package_ conf_ Path parameter, wrong exception type thrown")

        # Yaml file exists but the content is empty

        try:
            _config_path = ReadConfig().get_system('init_conf_path')
            shutil.copyfile(_config_path, _config_path + '.bak')

            with open(_config_path, 'w', encoding='utf-8') as w_f:
                w_f.write("")

            InitDataBase(config_file_path=_config_path).init_data()
        except Exception as e:
            self.assertEqual(
                e.__class__,
                ContentNoneException,
                msg="Yaml file exists, but the content is empty. The exception type is wrong")
        finally:
            # Restore files
            os.remove(_config_path)
            os.rename(_config_path + '.bak', _config_path)

        # Yaml file exists but DB exists_ The same with name
        try:
            _config_path = ReadConfig().get_system('init_conf_path')
            shutil.copyfile(_config_path, _config_path + '.bak')
            with open(_config_path, 'r', encoding='utf-8') as f:
                origin_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)
                for obj in origin_yaml:
                    obj["dbname"] = "openEuler"
                with open(_config_path, 'w', encoding='utf-8') as w_f:
                    yaml.dump(origin_yaml, w_f)

            InitDataBase(config_file_path=_config_path).init_data()
        except Exception as e:

            self.assertEqual(
                e.__class__,
                DatabaseRepeatException,
                msg="Yaml file exists but DB_ Name duplicate exception type is wrong")
        finally:
            # Restore files
            os.remove(_config_path)
            os.rename(_config_path + '.bak', _config_path)

    def test_wrong_param(self):
        # If the corresponding current init_ conf_ The directory specified by
        # path is incorrect
        try:
            # Back up source files
            shutil.copyfile(system_config.SYS_CONFIG_PATH, system_config.SYS_CONFIG_PATH + ".bak")
            # Modify dbtype to "test"_ dbtype"
            config = ConfigParser()
            config.read(system_config.SYS_CONFIG_PATH)
            config.set("SYSTEM", "init_conf_path", "D:\\Users\\conf.yaml")
            config.write(open(system_config.SYS_CONFIG_PATH, "w"))

            _config_path = ReadConfig().get_system('init_conf_path')
            InitDataBase(config_file_path=_config_path).init_data()
        except Exception as e:
            self.assertEqual(
                e.__class__,
                FileNotFoundError,
                msg="init_ conf_ Path specified directory is empty exception type is wrong")
        finally:
            # To restore a file, delete the file first and then rename it back
            os.remove(system_config.SYS_CONFIG_PATH)
            os.rename(system_config.SYS_CONFIG_PATH + ".bak", system_config.SYS_CONFIG_PATH)

        # Dbtype error
        try:
            # Back up source files
            shutil.copyfile(system_config.SYS_CONFIG_PATH, system_config.SYS_CONFIG_PATH + ".bak")
            # Modify dbtype to "test"_ dbtype"
            config = ConfigParser()
            config.read(system_config.SYS_CONFIG_PATH)
            config.set("DATABASE", "dbtype", "test_dbtype")
            config.write(open(system_config.SYS_CONFIG_PATH, "w"))

            _config_path = ReadConfig().get_system('init_conf_path')
            InitDataBase(config_file_path=None).init_data()
        except Exception as e:
            self.assertEqual(
                e.__class__,
                Exception,
                msg="Wrong exception type thrown when dbtype is wrong")
        finally:
            # To restore a file, delete the file first and then rename it back
            os.remove(system_config.SYS_CONFIG_PATH)
            os.rename(system_config.SYS_CONFIG_PATH + ".bak", system_config.SYS_CONFIG_PATH)

    def test_true_init_data(self):
        '''
            Initialization of system data
        '''
        # Normal configuration
        _config_path = ReadConfig().get_system('init_conf_path')
        InitDataBase(config_file_path=_config_path).init_data()

        # In the correct case, an import will be generated under the initsystem
        # directory_ success_ databse.yaml
        path = system_config.DATABASE_FILE_INFO

        self.assertTrue(
            os.path.exists(path),
            msg="Import was not generated successfully "
                "after initialization_ success_ databse.yaml file")

        # And there is data in this file, and it comes from the yaml file of
        # conf
        with open(_config_path, 'r', encoding='utf-8') as f:
            yaml_config = yaml.load(f.read(), Loader=yaml.FullLoader)

        with open(path, 'r', encoding='utf-8') as f:
            yaml_success = yaml.load(f.read(), Loader=yaml.FullLoader)

        self.assertEqual(
            len(yaml_config),
            len(yaml_success),
            msg="The success file is inconsistent with the original yaml file")

        # Compare name and priority
        success_name_priority = dict()
        config_name_priority = dict()
        for i in range(len(yaml_config)):
            success_name_priority[yaml_success[i]["database_name"]] = \
                yaml_success[i]["priority"]
            config_name_priority[yaml_config[i]["dbname"]] = \
                yaml_config[i]["priority"]

        self.assertEqual(
            success_name_priority,
            config_name_priority,
            msg="The database and priority after initialization are inconsistent with the original file")


def test_import_data_suit():
    suite = unittest.TestSuite()
    suite.addTest(ImportData("test_empty_param"))
    suite.addTest(ImportData("test_wrong_param"))
    suite.addTest(ImportData("test_true_init_data"))
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    unittest.main()
