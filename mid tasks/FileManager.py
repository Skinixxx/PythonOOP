class FileManager:
    @staticmethod
    def write_to_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content)

    @staticmethod
    def read_from_file(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден"

FileManager.write_to_file("example.txt", "Привет, мир!")
print(FileManager.read_from_file("example.txt"))  