@echo off
java -jar CTIFConverter-0.2.2.jar -m oc-tier3 -O 4 -o %~n1.ctif -P prewiew-%~n1.png %1