from dataclasses import dataclass

from typing import Dict, Any, Type, TypeVar

T = TypeVar("T", bound="BaseDataModel")


@dataclass
class BaseDataModel:
    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """
        Create an instance of the class from a dictionary, filtering out extra keys.

        Args:
            data (Dict[str, Any]): The dictionary containing the data.

        Returns:
            T: An instance of the class.
        """
        filtered_data = {k: v for k,
                         v in data.items() if k in cls.__annotations__}
        return cls(**filtered_data)
