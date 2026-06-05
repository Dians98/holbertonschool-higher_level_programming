class VerboseList(list):

    def append(self, item):

        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):

        items_to_add = list(iterable)
        super().extend(items_to_add)
        print(f"Extended the list with {len(items_to_add)} items.")

    def remove(self, item):

        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):

        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


if __name__ == "__main__":

    my_list = VerboseList()

    print("--- Testing append ---")
    my_list.append("Apple")
    my_list.append("Banana")

    print("\n--- Testing extend ---")
    my_list.extend(["Cherry", "Date", "Elderberry"])

    print("\nCurrent List State:", my_list)

    print("\n--- Testing pop (default index) ---")
    popped_item = my_list.pop()

    print("\n--- Testing pop (specific index) ---")
    popped_item_spec = my_list.pop(1)  # Pops "Banana"

    print("\n--- Testing remove ---")
    my_list.remove("Cherry")

    print("\nFinal List State:", my_list)
