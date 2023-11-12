cd C:\Users\Xeon_Fox\Documents\GitHub\DZDZDZDZDZDZ\11.11.23previousdz
#VN: ^^^ здесь лучше указывать относительный путь, а не абсолютный

ls
start previousdz.txt
#VN: в том каталоге должны быть .py файлы, и запускать их нужно по-другому

cd C:\Users\Xeon_Fox\Documents\GitHub\DZDZDZDZDZDZ\11.11.23
echo "" > runnercopy.ps1
#VN: ^^^ эта строка лишняя, так как команда cp сама создаст новый файл 
cp runner.ps1 runnercopy.ps1
ls