gcc tests/src/test.c -o tests/bin/c_test -mmanual-endbr
gfortran tests/src/test.f90 -o tests/bin/fort_test
gccgo tests/src/test.go -o tests/bin/go_test