# 1. Створення власного ітератора для зворотного читання файлу

class ReadFileReverse:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'r')
        self.lines = self.file.readlines()
        self.index = len(self.lines) - 1

    def __iter__(self):
        return self

    def __next__(self):
        """
        Зчитує файл у зворотному порядку — рядок за рядком з кінця файлу до початку.
        :return: str
        """
        if self.index < 0:
            self.file.close()
            raise StopIteration
        line = self.lines[self.index]
        self.index -= 1
        return line.strip()


if __name__ == "__main__":
    file = 'log.txt'
    try:
        for row in ReadFileReverse(file):
            print(row)
    except StopIteration as e:
        print(e)
