//см. батники или спроси меня, инструкция не совсем актуальна (команды, куда что положить etc.), сами логи не выкладываю
//reqs.py - парсил сайты, которые с пустым не парсились(hh бтв и так не спарсится, хочешь запариться - заводи вебдрайвер и вперед) еще когда на минте старые данные нам логи пытался разбирать
//post analysis - это почти все можно и маллетом делать, даже из консоли (как и stopwwords убрать, регистр переганть etc.), но пох, нам удобнее так
Крч вкратце: в директорию kek (отдельную офк, не к обучающей) закинуть новых так же обработанных(спарсил->нижнийрегистр->лемматор->хуйню убрал) файлов, которые мы еще не парсили(из логов взять автоматически, то есть),
несколько сотен ну или я хз, на твое усмотрение, хоть все, потом выполнить подряд 4 команды и заэкспортить в эксель 3 файла: tutorial_keys.txt, tutorial_composition.txt, testtopics.txt

//импорт обучающей выборки, в /data лежат полностью обработанные файлы с сайтов  в одной куче(только .parsed.txt файлы)
bin\mallet import-dir --input C:\Users\802925\Downloads\mallet-2.0.8RC3\kek1\data --output tutorial.mallet --keep-sequence 


//обучение выборки и сохранение в виде модели и инференсера, который будет выдавать нам %, composition и keys лучше экспортнуть в эксель, чтобы сортировать/смотреть/etc, 20 топиков.
bin\mallet train-topics  --input tutorial.mallet  --num-topics 20 --optimize-interval 20 --output-state topic-state.gz  --output-topic-keys tutorial_keys.txt --output-doc-topics tutorial_composition.txt --output-model hui.model --inferencer-filename infer.inferencer

// в директории новые файлы, которые нам надо прочекать по топикам, не должно быть написано .txt(.*).txt, маллет не видит файлы .txt.parsed.txt вроде
bin\mallet import-dir --input C:\Users\802925\Downloads\mallet-2.0.8RC3\kek --output test.mallet --keep-sequence 

//doc name topic proportion, тоже удобнее заэкспортить в эксель, чтобы потом смотреть
bin\mallet infer-topics --input test.mallet --inferencer infer.inferencer --output-doc-topics testtopics.txt  

