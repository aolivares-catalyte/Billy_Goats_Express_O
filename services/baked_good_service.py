from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository
from exceptions import (
    DuplicateBakedGoodError,
    BakedGoodNotFoundError,
)


class BakedGoodService:
    """
    Provides business logic for baked good operations.

    The service validates baked goods before storing them and
    delegates data storage to the repository.
    """

    def __init__(self, repository: BakedGoodRepository) -> None:
        """
        Initializes the service with a baked good repository.

        Args:
            repository (BakedGoodRepository):
                Repository used for data storage.
        """
        self._repository = repository

    def get_all_baked_goods(self) -> list[BakedGood]:
        """
        Retrieves all baked goods.

        Returns:
            list[BakedGood]:
                A list containing every baked good.
        """
        return self._repository.get_all()

    def get_baked_good(self, name: str) -> BakedGood | None:
        """
        Retrieves a baked good by name.

        Args:
            name (str):
                Name of the baked good.

        Returns:
            BakedGood | None:
                The baked good if found, otherwise None.
        """
        return self._repository.get_by_name(name)

    def create_baked_good(self, baked_good: BakedGood) -> BakedGood:
        """
        Creates a new baked good.

        Args:
            baked_good (BakedGood):
                The baked good to add.

        Raises:
            DuplicateBakedGoodError:
                If a baked good with the same name already exists.

        Returns:
            BakedGood:
                The newly created baked good.
        """
        if self._repository.get_by_name(baked_good.name) is not None:
            raise DuplicateBakedGoodError(
                f"Baked good '{baked_good.name}' already exists."
            )

        return self._repository.add(baked_good)

    def update_baked_good(
        self,
        name: str,
        baked_good: BakedGood,
    ) -> BakedGood:
        """
        Updates an existing baked good.

        Args:
            name (str):
                Name of the baked good to update.

            baked_good (BakedGood):
                Updated baked good information.

        Raises:
            BakedGoodNotFoundError:
                If the baked good does not exist.

        Returns:
            BakedGood:
                The updated baked good.
        """
        updated = self._repository.update(name, baked_good)

        if updated is None:
            raise BakedGoodNotFoundError(
                f"Baked good '{name}' was not found."
            )

        return updated

    def delete_baked_good(self, name: str) -> bool:
        """
        Deletes a baked good.

        Args:
            name (str):
                Name of the baked good to remove.

        Raises:
            BakedGoodNotFoundError:
                If the baked good does not exist.

        Returns:
            bool:
                True if the baked good was successfully deleted.
        """
        deleted = self._repository.delete(name)

        if not deleted:
            raise BakedGoodNotFoundError(
                f"Baked good '{name}' was not found."
            )

        return True