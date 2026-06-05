class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        return self

    def get_count(self):
        return self.counter


if __name__ == "__main__":
    languages = ["Python", "Java", "C++", "JavaScript", "Rust"]
    counted_iter = CountedIterator(languages)

    print("--- Step 1: Manual calls using next() ---")
    print(f"Fetched: {next(counted_iter)}")
    print(f"Fetched: {next(counted_iter)}")
    print(f"Current Count: {counted_iter.get_count()}")

    print("\n--- Step 2: Resuming iteration with a loop ---")
    for lang in counted_iter:
        print(f"Fetched via loop: {lang}")

    print(f"\nFinal Count: {counted_iter.get_count()}")

    print("\n--- Step 3: Verifying StopIteration is still raised ---")
    try:
        next(counted_iter)
    except StopIteration:
        print("StopIteration raised successfully! No more items left.")
