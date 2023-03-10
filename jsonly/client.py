import json
from typing import Dict, Any, Union
from .error import PathException, GetExcetion, UpdateExcetion


class Connect:
    """
    This class provides convenient functions while connected with json file.

    Return PathException() when json file doesn't exist.
    """

    def __init__(
        self, path: str, encoding: str = "utf-8", ensure_ascii: bool = False
    ) -> None:
        """
        Connects with json file with the preferences provieded from parameter.

        :param path: path of json file
        :param encoding: set encoding of json file
        :param ensure_ascii: prevent corruption of none-ascii letter
        """
        try:
            with open(path, "r", encoding=encoding) as f:
                json.load(f)
        except Exception as exception:
            raise PathException(exception)
        else:
            self.path = path
            self.encoding = encoding
            self.ensure_ascii = ensure_ascii

    def get(self, path: str = None) -> Dict[str, Any]:
        """
        Load data from the database.

        :param path: nested path expressed as '/' separators , bring all data by default
        :return: loaded data
        """
        try:
            with open(self.path, "r", encoding=self.encoding) as f:
                data = json.load(f)
            if path != None:
                path = path.split("/")
                for i in path:
                    data = data[str(i)]
            return data
        except Exception as exception:
            raise PathException(exception)

    def set(self, data: Dict[str, Any]) -> bool:
        """
        Overwrite the entire database with new data.

        :param data: overwrite the entire database with data
        :return: return True if saving was successful
        """
        try:
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)

    def update(self, data: Dict[str, Any]) -> bool:
        """
        Add to the root of database with new value.

        :param data: add to the root of database with data
        :return: return True if update was successful
        """
        get_data = self.get()
        key_list = list(data.keys())
        try:
            for i in key_list:
                get_data[i] = data[i]
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(get_data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)

    def insert(self, data: Dict[str, Any], path: str = "/") -> bool:
        """
        Add data to the path.

        :param path: nested path expressed as '/' separators
        :param data: data to be added to the path
        :return: return True if inserting was successful
        """
        get_data = self.get()
        try:
            if path != None:
                path = path.split("/")

                def nested_set(dic, keys, value):
                    for key in keys[:-1]:
                        dic = dic.setdefault(key, {})
                    dic[keys[-1]] = value

                nested_set(get_data, path, data)
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(get_data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)
