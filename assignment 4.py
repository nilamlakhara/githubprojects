class Fibonacci:
    def __init__(self, n: int):
        self.n = n

    def recursive(self, n: int = None) -> int:
        """Computes nth Fibonacci number using recursion."""
        if n is None:
            n = self.n
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self.recursive(n - 1) + self.recursive(n - 2)

    def dynamic() -> int:
        """Computes nth Fibonacci number using dynamic (iterative DP) approach."""
        a, b = 0, 1
        for _ in range(self.n):
            a, b = b, a + b
        return a

    def display_sequence() -> list:
        """Generates and returns the full sequence up to n."""
        sequence = []
        a, b = 0, 1
        for _ in range(self.n):
            sequence.append(a)
            a, b = b, a + b
        return sequence


class MainProgram:
    @staticmethod
    def main():
        try:
            num = int(input("Enter n: "))
            fib = Fibonacci(num)

            print(f"Fib({num}) [Dynamic]   = {fib.dynamic()}")
            print(f"Fib({num}) [Recursive] = {fib.recursive()}")
            print(f"Sequence up to {num} terms = {fib.display_sequence()}")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    MainProgram.main()
